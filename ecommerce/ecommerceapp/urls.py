from django.urls import path
from .views import index, contact, about, checkout, handlerequest

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('checkout/', checkout, name='Checkout'),
    path('handlerequest/',handlerequest, name="HandleRequest")
]
