from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from .models import Project


# If the user is not logged in, this will redirect to the
# settings.LOGIN_URL
@login_required
def UserDashboard(request):
    context = {

    }
    return render(request, 'dashboard.html', context)
