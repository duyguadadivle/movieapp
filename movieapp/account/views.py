from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from account.forms import CreateUserForm, LoginForm, UserPasswordChangeForm
from django.contrib import messages
# from movieapp.account.forms import UserPasswordChangeForm
#from movieapp.account.forms import CreateUserForm
#from movieapp.account.forms import LoginForm

# Create your views here.
def login_request(request):
    if request.user.is_authenticated:
        return redirect("home_page")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            remember_me = form.cleaned_data.get("remember_me")

            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                    request.session.modified = True
                return redirect("home_page")
            else:
                form.add_error(None, "Wrong email or password")
                return render(request, 'account/login.html', {'form': form})

            
        else:
            return render(request, 'account/login.html', {'form': form})


    form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def register_request(request):
    if request.user.is_authenticated:
        return redirect("home_page")

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = user.username
            # print(user.username)
            # username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home_page")
        else:
            form.add_error(None, "You must fill in the form completely.")
            return render(request, 'account/register.html', {"form":form})

    form = CreateUserForm()
    return render(request, 'account/register.html', {"form":form})

def change_password(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password is changed")
            return redirect("change_password")
        else:
            return render(request, 'account/change_password.html', {"form":form})

    form = UserPasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {"form": form})    

def profile(request):
    return render(request, 'account/profile.html')   

def watch_list(request):
    return render(request, 'account/watch-list.html')    
  
def logout_request(request):
    logout(request)
    return redirect("home_page")