from django.forms import ModelForm
from .models import post, category, contact, advert, comment, AddVideo
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'snippet', 'details', 'post_category', 'image', 'link')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
            'post_category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddVideoForm(forms.ModelForm):
    class Meta:
        model = AddVideo
        fields = ('image','title','link','snippet', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))




class CatForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ('category_name', )

        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ('name','email', 'subject', 'message', )

class ads_fileForm(forms.ModelForm):
    class Meta:
        model = advert
        fields = ('ads_file', )
        widgets = { 
            'ads_file': forms.FileInput(attrs={'class': 'form-control'}),
        }

       
class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('name','email', 'message', )


       