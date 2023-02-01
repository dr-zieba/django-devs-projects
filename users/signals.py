from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

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
            user=user, username=user.username, email=user.email, name=user.first_name
        )
        subject = "Welcome message v2"
        message = "Account created"

        message = Mail(
            from_email=Email(settings.DEFAULT_FROM_EMAIL),
            to_emails=To('dev.sender.django@gmail.com'),
            subject=subject,
            plain_text_content=Content("text/plain", "and easy to do anywhere, even with Python"))
        try:
            mail_json = message.get()
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.client.mail.send.post(request_body=mail_json)
            print(response.status_code)
            print(response.headers)
        except Exception as e:
            print(e.message)


@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    # method should be executed only on none existing user
    # user model is updated with data from profile
    # profile is created with signal createProfile when user is created
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)
