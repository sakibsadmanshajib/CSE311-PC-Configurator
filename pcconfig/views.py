from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def user_login(request):
    context = {}
    next = request.GET.get('next')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if next:
                return redirect(next)
            else:
                messages.success(request, "You have successfully logged in!")
                return redirect('webapp:order')
        else:
            messages.error(request, "Provide valid credentials.")
            return render(request, 'auth/login.html')
    
    else:
        return render(request, 'auth/login.html', context)

def user_signup(request):
    
    # Follow link for reference video: https://www.youtube.com/watch?v=q4jPR-M0TAQ
    
    pass

def user_logout(request):
    messages.success(request, "You have been logged out!")
    logout(request)
    return redirect('webapp:login')

def home(request):
    pc_list = PC.objects.all()

    return render(request, 'pcconfig/home.html', {'pc_list': pc_list})

@login_required
def createPC(request):
    # See Reference to add user https://www.youtube.com/watch?v=zJWhizYFKP0

    if request.method == 'POST':

        form = AddPC(request.POST)
        if form.is_valid():
            pc = PC(
                cpu = CPU.objects.get(id=form.cleaned_data['CPU']),
                ram = RAM.objects.get(id=form.cleaned_data['RAM']),
                gpu = GPU.objects.get(id=form.cleaned_data['GPU']),
                motherboard = Motherboard.objects.get(id=form.cleaned_data['Motherboard']),
                storage = Storage.objects.get(id=form.cleaned_data['Storage']),
                price = CPU.objects.get(id=form.cleaned_data['CPU']).price + RAM.objects.get(id=form.cleaned_data['RAM']).price + GPU.objects.get(id=form.cleaned_data['GPU']).price + Motherboard.objects.get(id=form.cleaned_data['Motherboard']).price + Storage.objects.get(id=form.cleaned_data['Storage']).price,
                author = request.user
            )
            pc.save()


def viewPC(request, PC_id):

    # View individual PC entries. If the request.user is equal to author of PC, they have the authorization to edit it. 
    pass

"""Use a decorator user_passes_check to verify only the author has the right to edit their entries.
Follow https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.decorators.user_passes_test for more info"""
# @user_passes_test
def editPC(request, PC_id):

    # edit PC entry.

    pass