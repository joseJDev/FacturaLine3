""" Funcion para generar consecutivos de la factura """

# Models 
from pickle import TRUE
from tkinter import N
from apps.factura.models import FactureLine


def create_consective(model) -> int:
    count = model.objects.all().count()
    n_invoice = count + 1

    while model.objects.filter(n_invoice=n_invoice).exists():
        n_invoice = n_invoice + 1
    
    return n_invoice