from django.contrib import admin
from .models import ProjectsOpenMine, ProjectsClosed, ProjectsOpen

# Register your models here.

admin.site.register(ProjectsOpen)
admin.site.register(ProjectsOpenMine)
admin.site.register(ProjectsClosed)