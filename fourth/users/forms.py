from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)

        for fields in self.fields.values():
            fields.widget.attrs.update({'class':'input'})
            
    class Meta:
        model = User 
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'Name'}


class ProfileForm(ModelForm):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)

        for fields in self.fields.values():
            fields.widget.attrs.update({'class':'input'})

    class Meta:
        model = Profile
        fields = ['name','email','username', 'bio', 'short_intro', 'profile_image', 'social_github', 'social_youtube', 'social_website']