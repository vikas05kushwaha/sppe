# example/urls.py
from django.urls import path

from example import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('quotation', views.newInvoice, name='quotation'),

    path('generate-quotation/', views.generate_quotation, name='generate_quotation'),
    ]