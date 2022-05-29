# Django
from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from .views import (
    HomeView, ClientListTemplate,
    ClientListView, ClientCreateView,
    ClientUpdateView, ClientDeleteView,
    ProductListTemplate, ProductListView,
    ProductCreateView, ProductUpdateView,
    ProductDeleteView, FactureView,
    GetInfoClientView, GenerateQuotes,
    GeneratePDF, ReportClientTemplate,
    GetReportView, DetailFactureView,
    FinancialBoxDetailView, CreateFinancialBoxView, 
    GeneratePDFFinancial, ReportBoxTemplateView, 
    ReportBoxView , ReportDeleteView,DeleteReportFactureView,
)

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    
    # Clientes
    path('client/', login_required(ClientListTemplate.as_view()), name='list_client'),
    path('client-list/', login_required(ClientListView.as_view()), name='list_client_ajax'),
    path('client-create/', login_required(ClientCreateView.as_view()), name='create_client'),
    path('client-update/<int:pk>',login_required( ClientUpdateView.as_view()), name='update_client'),
    path('client-delete/<int:pk>',login_required( ClientDeleteView.as_view()), name='delete_client'),

    # Productos
    path('product/', login_required(ProductListTemplate.as_view()), name='list_product'),
    path('product-list/', login_required(ProductListView.as_view()), name='list_product_ajax'),
    path('product-create/', login_required(ProductCreateView.as_view()), name='create_product'),
    path('product-edit/<int:pk>', login_required(ProductUpdateView.as_view()), name='edit_product'),
    path('product-delete/<int:pk>', login_required(ProductDeleteView.as_view()), name='delete_product'),

    # Factura
    path('facture/', login_required(FactureView.as_view()), name='facture'),
    path('facture-get-client/', login_required(GetInfoClientView.as_view()), name='facture_get_client'),
    path('facture-gen-quotes/', login_required(GenerateQuotes.as_view()), name='facture_gen_quotes'),
    path('facture-gen-pdf/', login_required(GeneratePDF.as_view()), name='facture_gen_pdf'),
    path('detail-facture/<int:pk>', login_required(DetailFactureView.as_view()), name='detail_facture'),
     
    
    # Reportes 
    path('report/', login_required(ReportClientTemplate.as_view()), name='report'),
    path('get-report/', login_required(GetReportView.as_view()), name='get_report'),

    # Caja
    path('financial-box/<int:pk>', login_required(FinancialBoxDetailView.as_view()), name='financial_box'),
    path('financial-box-create/', login_required(CreateFinancialBoxView.as_view()), name='financial_box_create'),
    path('financial-gen-pdf/', login_required(GeneratePDFFinancial.as_view()), name='financial_box_pdf'),
    path('report-box-delete/<int:pk>', login_required(ReportDeleteView.as_view()), name='report_box_delete'),
    path('report-client-delete/<int:pk>', login_required(DeleteReportFactureView.as_view()), name='report_client_delete'),
    path('report-box/', login_required(ReportBoxTemplateView.as_view()), name='report_box'),
    path('get-report-box/', login_required(ReportBoxView.as_view()), name='get_report_box'),
]
