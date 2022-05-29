""" Funcion para generar consecutivos de la factura """

# Models
from apps.factura.models import FactureLine


def create_consective(model, typeC) -> int:
    count = model.objects.all().count()
    consecutive = count + 1

    while model.objects.filter(n_invoice=consecutive).exists() if typeC=="invoice" else model.objects.filter(n_consecutive=consecutive).exists():
        consecutive = consecutive + 1
    
    return consecutive