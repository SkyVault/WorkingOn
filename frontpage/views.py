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
    project = Project.objects.get(id=project_id)
    context = {
        'APPNAME': "WorkingOn",
        'project': project,
        'posts': project.post_set.all()
    }
    return render(request, 'project.html', context)
