from django.db import models
from django.utils import timezone

# User authors posts and projects
from django.contrib.auth.models import User


"""
NOTE: to access all projects for a certain user
user = User.objects.get(username='<username>')
user.project_set

NOTE: to get the User model
from django.contrib.auth.models import User

NOTE: to create a project/post fast
user.project_set.create(title='...',...)

"""


# A project is a child of the User
class Project(models.Model):
    # NOTE(Dustin): models.CASCADE deletes project if user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


# A post is a child of a project, when the project gets deleted
# all the posts for that project will too
class Post(models.Model):
    author = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=256)
    description = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"
