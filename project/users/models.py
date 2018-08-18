from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    ### see https://stackoverflow.com/questions/37332190/django-login-with-email
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'),max_length=255,  unique=True) # changes email to unique and blank to false 
    is_staff = models.BooleanField(_('staff status'), default=False)

    ## to avoid :
   	### django.db.utils.IntegrityError: UNIQUE constraint failed: users_customuser.username
   	#### add (may be it better to say 'set' ?):
   	#####  username with unique=False
    username = models.TextField(_('user name'), max_length=255,  unique=False)
    REQUIRED_FIELDS = ['username',] # removes email from REQUIRED_FIELDS

    def __str__(self):
        return self.email
