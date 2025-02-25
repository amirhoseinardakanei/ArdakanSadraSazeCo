from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='RegisterPage'),
    path('login/', views.Login.as_view(), name='LoginPage'),
    path('logout/', views.Logout.as_view(), name='LogoutPage'),
    path('userpanel/', views.UserPanel.as_view(), name='UserPanelPage'),

]