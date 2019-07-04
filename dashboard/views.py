from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm


# If the user is not logged in, this will redirect to the
# settings.LOGIN_URL
@login_required
def UserDashboard(request):
    context = {
        'current_user': request.user,
        'projects': request.user.project_set.all()
    }
    return render(request, 'dashboard.html', context)


@login_required
def CreateProject(request):
    if request.method == "POST":
        form = NewProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('dashboard')
    else:
        context = {
            'current_user': request.user,
            'projects': request.user.project_set.all(),
            'form': NewProjectForm(),
        }
        return render(request, 'newproject.html', context)
