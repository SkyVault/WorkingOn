from django.shortcuts import render
from .models import Project


def FrontPage(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'frontpage.html', context)
