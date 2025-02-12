from django.shortcuts import render
from django.views.generic import TemplateView, View, DetailView
from .models import SettingWeb, TeamCo, CeoSpeech, ServiceWeb, LogoCompani, TruckOne, TruckTow, TruckTree
from ProjectsApp.models import ProjectsOpen
# Create your views here.

class HomePage(View):
    def get(self, request):
        setting_web = SettingWeb.objects.filter(ok_no=True).first()
        service_web = ServiceWeb.objects.filter().all
        ceo_speech = CeoSpeech.objects.filter().first()
        team_co = TeamCo.objects.filter().all
        logo_compani = LogoCompani.objects.filter().all()
        projects = ProjectsOpen.objects.filter(boolean=True)
        return render(request, 'HomeApp/HomePage.html', {
            'setting_web': setting_web,
            'service_web': service_web,
            'ceo_speech': ceo_speech,
            'team_co': team_co,
            'logo_compani': logo_compani,
            'projects': projects,
        })

class ServiceDetail(DetailView):
    template_name = 'HomeApp/ServiceDetail.html'
    model = ServiceWeb

class GoalsCom(TemplateView):
    template_name = 'HomeApp/GoalsCom.html'

class Truck(View):
    def get(self, request):
        truck_one = TruckOne.objects.filter().all()
        truck_tow = TruckTow.objects.filter().all()
        truck_tree = TruckTree.objects.filter().all()

        return render(request, 'HomeApp/Trucks.html', {
            'truck_one': truck_one,
            'truck_tow': truck_tow,
            'truck_tree': truck_tree,

        })



def SiteNavbar(request):
    service_web = ServiceWeb.objects.filter().all
    return render(request, 'Base/Navbar.html',{
        'service_web': service_web,
    })


def SiteFooter(request):
    service_web = ServiceWeb.objects.filter().all
    return render(request, 'Base/Footer.html',{
        'service_web': service_web,
    })