from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Signals triggers action for particular operations on model stated as sender
# Function is triggered with decorator receiver or with call like:
# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)

# To work from seperate file config needs to be updated
# In app apps.py file / here it will be users/apps.py
# add function inside UsersConfig class:
#     def ready(self):
#         import users.signals


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )

@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)