from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.utils.translation import ugettext_lazy as _


from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class LoginForm(AuthenticationForm):

    #email = forms.EmailField(label=_("E-mail"), max_length=75)
    email = forms.CharField(label=_("Email:"), max_length=254, 
                    widget=forms.TextInput(attrs={'class': 'loginput'}))

    def __init__(self, *args, **kwargs): 
        super(LoginForm, self).__init__(*args, **kwargs) 
        self.fields['email'].required = True 
        # remove username
        self.fields.pop('username')
