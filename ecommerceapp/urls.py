from django.urls import path
from .views import index, contact, about, checkout, handlerequest, profile

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('profile', profile, name='profile'),
    path('checkout/', checkout, name='Checkout'),
    path('handlerequest/',handlerequest, name="HandleRequest")
]
