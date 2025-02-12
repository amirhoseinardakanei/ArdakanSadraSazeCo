from django.urls import path
from . import views

urlpatterns = [
    path('', views.Barcode, name='Barcode'),

    path('fall/', views.Fall, name='Fall'),
    path('angizeshi/', views.Angizeshi, name='Angizeshi'),
    path('shear/', views.Shear, name='Shear'),

]