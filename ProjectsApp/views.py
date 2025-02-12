from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProjectsOpenMine, ProjectsClosed, ProjectsOpen


# Create your views here.

class ProjectsOpenView(ListView):
    template_name = 'ProjectsApp/ProjectsOpenList.html'
    model = ProjectsOpen
    context_object_name = 'project'
    paginate_by = 1


class ProjectsOpenDetail(DetailView):
    template_name = 'ProjectsApp/ProjectsOpenDetail.html'
    model = ProjectsOpen


class ProjectsMineView(ListView):
    template_name = 'ProjectsApp/ProjectsMineList.html'
    model = ProjectsOpenMine
    context_object_name = 'project'
    paginate_by = 1


class ProjectsMineDetail(DetailView):
    template_name = 'ProjectsApp/ProjectsMineDetail.html'
    model = ProjectsOpenMine

class ProjectsClosedView(ListView):
    template_name = 'ProjectsApp/ProjectsClosed.html'
    model = ProjectsClosed
    context_object_name = 'project'

