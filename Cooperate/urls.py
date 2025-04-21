from . import views
from django.urls import path


urlpatterns = [
    path('redirect-step/', views.Redirect_Step, name='Redirect_Step'),
    path('step1/', views.CooperateStep_1.as_view(), name='CooperateStep_1'),
    path('step2/', views.CooperateStep_2.as_view(), name='CooperateStep_2'),
    path('step3/', views.CooperateStep_3.as_view(), name='CooperateStep_3'),
    path('step4/', views.CooperateStep_4.as_view(), name='CooperateStep_4'),
]