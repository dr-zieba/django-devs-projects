from django.forms import ModelForm
from .models import Project
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "featured_image",
            "demo_link",
            "source_link",
            "tags",
        ]  # can be list with fields names of model or as '__all__ for all fields'
        widgets = {"tags": forms.CheckboxSelectMultiple()}

        # DONE to be able to add css class for styling

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        [
            self.fields[k].widget.attrs.update({"class": "input"})
            for k, v in self.fields.items()
        ]
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'add ...'})
