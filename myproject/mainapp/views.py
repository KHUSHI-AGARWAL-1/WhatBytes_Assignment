from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *
@login_required
def dashboard(request):
    return render(request,'registration/dashboard.html',{'section':'dashboard'})

@login_required
def user_profile(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        'date_joined': user.date_joined,
        'last_login': user.last_login,
    }
    return render(request, 'registration/user_profile.html', context)

def custom_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

def register(request):
    if request.method=='POST':
        user_form= UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user= user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'registration/register_done.html',{'new_user': new_user})
    else:
        user_form=UserRegistrationForm()
    return render(request,'registration/register.html',{'user_form':user_form})