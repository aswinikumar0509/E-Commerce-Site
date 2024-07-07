from django.shortcuts import render,redirect

# Create your views here.
from django.contrib import messages
from .forms import RegisterForm

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request , f"Welcome {username} to the store")
            return redirect('login')    
    else:
        form = RegisterForm()
    return render(request , 'users/register.html',{'form':form})


def profilePage(request):
    return render(request , 'users/profile.html')
