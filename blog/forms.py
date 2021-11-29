from django import forms

from .models import Post

#newadd 
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

#newadd 
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','password1','password2') #注意小写
