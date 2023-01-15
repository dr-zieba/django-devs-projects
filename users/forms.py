from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "email",
            "username",
            "password1",
            "password2",
        ]  # can be list with fields names of model or as '__all__ for all fields'
        labels = {"first_name": "First name"}

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        [
            self.fields[k].widget.attrs.update({"class": "input"})
            for k, v in self.fields.items()
        ]
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'add ...'})


class CustomProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(CustomProfileCreationForm, self).__init__(*args, **kwargs)

        [
            self.fields[k].widget.attrs.update({"class": "input"})
            for k, v in self.fields.items()
        ]


class CustomSkillAdd(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]

    def __init__(self, *args, **kwargs):
        super(CustomSkillAdd, self).__init__(*args, **kwargs)

        [
            self.fields[k].widget.attrs.update({"class": "input"})
            for k, v in self.fields.items()
        ]
