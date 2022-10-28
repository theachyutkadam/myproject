from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def loginUser(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
      login(request, user)
      return redirect('/')

  return render(request, "/login.html")

def logoutUser(request):
  logout(request)
  return redirect('/login')

def home(request):
  if request.user.is_authenticated:
    print("Logged in")
    return redirect("/home/contact.html")
  else:
    print("Not logged in")
    return redirect('/register')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('/login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
