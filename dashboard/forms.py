from django import forms
from django.apps import apps


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('frontpage', 'Project')
        fields = ('title', 'description')
