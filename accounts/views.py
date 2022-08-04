from django.contrib.auth import authenticate,login
from django.shortcuts import redirect,render
from django.contrib.auth import logout as django_logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
          user = form.save()
          return redirect('accounts:login')
    else:
        form = SignupForm()
        
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

def login_check(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
        
    return render(request, 'accounts/login.html', {"form":form})

def logout(request):
  django_logout(request)
  return redirect('/')