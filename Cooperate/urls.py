from . import views
from django.urls import path


urlpatterns = [
    path('', views.Cooperate.as_view(), name='cooperate-view'),
]