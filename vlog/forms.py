from .models import Contact,Post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
class ContactFrm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']
        widgets = {
            "name":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter Your Name"
            }),
            "email":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter Your Email"
            }),
            "subject":forms.Textarea(attrs={
                "class":"form-control",
                "placeholder":"Enter Your Subject",
                "cols":"0",
                "rows":"0"
            }),
             "message":forms.Textarea(attrs={
                "class":"form-control",
                "placeholder":"Enter Your Messages",
                 "cols":"0",
                 "rows":"0"
            }),
        } 

        error_messages = {
            "name":{"required":"Name Must Be Required."},
            "email":{"required":"Email Must Be Required."},
            "subject":{"required":"Subject Must Be Required."},
            "message":{"required":"Name Must Be Required."},
        }

class SignUpform(UserCreationForm):
    username = forms.CharField(label="Username",label_suffix="",widget = forms.TextInput(attrs={
         "class":"form-control",
        "placeholder":"Enter  Username"
    }),error_messages={"required":"Username Must Be Required"})
    password1 = forms.CharField(label="Password",label_suffix="",widget = forms.PasswordInput(attrs={
         "class":"form-control",
        "placeholder":"Enter  Password"
    }),error_messages={"required":"Password Must Be Required"})
    password2 = forms.CharField(label="Confirm Password ",label_suffix="",widget = forms.PasswordInput(attrs={
         "class":"form-control",
        "placeholder":"Enter  Confirm Password"
    }),error_messages={"required":"Confirm Password Must Be Required"})
    first_name = forms.CharField(required=True,label_suffix="",widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Enter First Name"
    }),error_messages={"required":"First Name Must Be Required"})
    last_name = forms.CharField(required=True,label_suffix="",widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Enter Last Name"
    }),error_messages={"required":"Last Name Must Be Required"})
    email = forms.EmailField(label="Email",label_suffix="",required=True,widget=forms.EmailInput(attrs={
        "class":"form-control",
        "placeholder":"Enter Email "
    }),error_messages={"required":"Email Must Be Required"})
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']



class LoginFrm(AuthenticationForm):
    username = forms.CharField(label="Username",label_suffix="",widget = forms.TextInput(attrs={
         "class":"form-control",
        "placeholder":"Enter  Username"
        }),error_messages={"required":"Username Must Be Required"})
    password = forms.CharField(label="Password",label_suffix="",widget = forms.PasswordInput(attrs={
            "class":"form-control",
            "placeholder":"Enter  Password"
        }),error_messages={"required":"Password Must Be Required"})
        


       
class PostForm(forms.ModelForm):
    title = forms.CharField(label_suffix="",error_messages = {"required":"Title Must Required"},widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Enter Title"
        }))
    auth = forms.CharField(label_suffix="",error_messages = {"required":"Auth Must Required"},widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Enter Auth"
        }))
    desc = forms.CharField(label_suffix="",error_messages = {"required":"Description Must Required"},widget=forms.Textarea(attrs={
            "class":"form-control",
            "placeholder":"Enter Description"
        }))
    class Meta:
        model = Post
        fields = ['title','auth','desc']

        
    