""" Views Financial Box """
# Django
from django.views import View, generic
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.conf import settings

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Models 
from apps.factura.models import (
    FactureLine,ProductsFacture,
    PaymentsFacture
)

# Forms
from apps.factura.forms import FormFinancialBox

# Python
import json

# Utils
from core.utils.generate_pdf import render_pdf_docraptor
from core.utils.create_consecutive import create_consective
from core.utils.format_date import format_dates



class ReportBoxTemplateView(View):
    template_name = 'financial_box/report_box.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ReportBoxView(View):
    def get(self, request, *args, **kwargs):
        first_date = request.GET.get('first_date')
        last_date = request.GET.get('last_date')

        f_first_date, f_last_date = format_dates(first_date, last_date)
        
        query = PaymentsFacture.objects.filter(
            created__date__range = [f_first_date, f_last_date]
        )

        data = []
        total_value = 0

        for q in query:
            total_value += q.total_payment
            data.append({
                "id": q.id,
                "client_fullname": "{} - {}".format(
                    q.facture.client.first_name if q.facture else "",
                    q.facture.client.last_name if q.facture else ""
                ),
                "consultory": q.facture.client.name_consultory if q.facture else "",
                "date": q.created,
                "value": q.total_payment
            })

        # Convert to json

        response = JsonResponse({'data': data, "total": total_value})
        response.status_code = 200
        
        return response

class FinancialBoxDetailView(View):
    template_name = 'financial_box/financial.html'

    def get(self, request, *args, **kwargs):
        facture = FactureLine.objects.filter(id=kwargs.get('pk')).first()
        products = ProductsFacture.objects.filter(facture__id = facture.id)
        data = {
            'facture': facture,
            'products': products,
            'type_payment': PaymentsFacture.TYPE_PAYMENT
        }
        return render(request, self.template_name, data)


class CreateFinancialBoxView(View):
    form_class = FormFinancialBox

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = self.form_class(data)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            
            # Guardar registro de pago
            cleaned_data['n_consecutive'] = create_consective(PaymentsFacture, 'payment')
            facuture_payment = PaymentsFacture.objects.create(**cleaned_data)

            # Actualizar saldo
            facture = facuture_payment.facture
            facture.balance = facture.balance - facuture_payment.total_payment
            facture.save()

             # URL para descargar PDF
            url_financial = settings.DOMAIN+"financial-gen-pdf/?facturePayment={}".format(facuture_payment.id)

            return JsonResponse({
                "url_financial": url_financial
            })
        else:
            errors = form.errors.as_json()
            errors = json.loads(errors)
            
            response = JsonResponse(errors)
            response.status_code = 400
            return response



class GeneratePDFFinancial(View):
    def get(self, request, *args, **kwargs):
        id_facture_payment = request.GET.get('facturePayment', None)
        facture_payment = PaymentsFacture.objects.filter(id=id_facture_payment).first()
        products_facture = ProductsFacture.objects.filter(facture__id = facture_payment.facture.id)

        if not facture_payment:
            return redirect('/')
        
        # Generar PDF
        filename = "{}_{}_factura.pdf".format(
            facture_payment.facture.client.first_name,
            facture_payment.facture.client.last_name,
        )

        # Data Render
        data_render = {
            "facture_payment": facture_payment,
            "products_facture": products_facture
        }

        pdf = render_pdf_docraptor('financial_box/pdf/report_financial.html', filename, data_render)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        return response

class ReportDeleteView(View):
    template_name = 'report-box-delete/report_delete.html'
    form_class = FormFinancialBox


    def post(self, request, *args, **kwargs):
        box = self.get_object(kwargs.get('pk'))
        facture = box.facture 

        # Actualizaci??n del saldo
        facture.balance = facture.balance + box.total_payment
        facture.save()
        
        box.delete()
        response = JsonResponse({'message': 'El recibo de caja ha sido eliminado exitosamente'})
        response.status_code = 200
        return response
        
    def get_object(self, pk):
        return PaymentsFacture.objects.filter(id=pk).first()        