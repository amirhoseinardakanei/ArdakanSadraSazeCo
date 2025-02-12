from django.urls import path
from . import views

urlpatterns = [
    path('open/', views.ProjectsOpenView.as_view(), name='ProjectsOpenView'),
    path('open/<slug:slug>', views.ProjectsOpenDetail.as_view(), name='ProjectsOpenDetail'),

    path('mine/', views.ProjectsMineView.as_view(), name='ProjectsMineView'),
    path('mine/<slug:slug>', views.ProjectsMineDetail.as_view(), name='ProjectsMineDetail'),

    path('closed/', views.ProjectsClosedView.as_view(), name='ProjectsClosedView'),
]