from django.shortcuts import render
from .models import Project


def FrontPage(request):
    context = {
        'APPNAME': "WorkingOn",
        'projects': Project.objects.all()
    }
    return render(request, 'frontpage.html', context)


# TODO(Dustin): Probably need to move this, not sure where...
def ProjectView(request, project_id):
    context = {
        'APPNAME': "WorkingOn",
        'project': Project.objects.get(id=project_id)
    }
    return render(request, 'project.html', context)
