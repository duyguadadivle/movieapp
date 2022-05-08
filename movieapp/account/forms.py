from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
import random

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class":"form-control form-control-user", "placeholder":"Enter Email "}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-control-user", "placeholder":"Password"}))
    remember_me = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={"class":"custom-control-input"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not User.objects.filter(email=email).exists():
            self.add_error("email", "There are no registered users with the email entered.")

        return email


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control form-control-user", "placeholder":"Password"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control form-control-user", "placeholder":"Password again"})
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Name"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control form-control-user","placeholder":"LastName"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control form-control-user", "placeholder":"Email"})
        self.fields["email"].required = True
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        


    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error("email","There is already a user with this email address.")

        return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get("password1"))
        user.username = "{}_{}_{}".format(
            self.cleaned_data.get("first_name").replace("ç","c").replace("ğ","g").replace("ı","i").replace("ö","o").replace("ş","s").replace("ü","u").lower(),
            self.cleaned_data.get("last_name").replace("ç","c").replace("ğ","g").replace("ı","i").replace("ö","o").replace("ş","s").replace("ü","u").lower(),
            random.randint(11111,99999)
        )

        if commit:
            user.save()
        return user    