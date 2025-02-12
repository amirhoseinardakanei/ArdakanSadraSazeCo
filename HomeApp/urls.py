from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='HomePage'),
    path('goals/', views.GoalsCom.as_view(), name='GoalsCom'),
    path('trucks/', views.Truck.as_view(), name='Truck'),
    path('<slug:slug>', views.ServiceDetail.as_view(), name='ServiceDetail'),
]