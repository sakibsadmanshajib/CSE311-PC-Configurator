from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
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
                return redirect('pcconfig:home')
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
    return redirect('pcconfig:login')

def home(request):
    pc_list = PC.objects.all()

    return render(request, 'pcconfig/home.html', {'pc_list': pc_list})

@login_required
def createPC(request):
    # See Reference to add author https://www.youtube.com/watch?v=zJWhizYFKP0

    cpu_list = CPU.objects.all()
    ram_list = RAM.objects.all()
    gpu_list = GPU.objects.all()
    motherboard_list = Motherboard.objects.all()
    storage_list = Storage.objects.all()

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
            messages.success(request, "Successfully added a new PC!")
            return redirect('pcconfig:viewPC', PC_id=pc.pc_id)
        
        else:
            messages.warning(request, "Couldn't add a new entry!")
            return redirect('pcconfig:home')
        
    else:
        form = AddPC()
        return render(request, 'pcconfig/add.html', {'form': form, 'cpu_list': cpu_list, 'ram_list': ram_list, 'gpu_list': gpu_list, 'motherboard_list': motherboard_list, 'storage_list': storage_list})


def viewPC(request, PC_id):

    # View individual PC entries. If the request.user is equal to author of PC, they have the authorization to edit it. 

    pc = PC.objects.get(id=PC_id)
    
    return render(request, 'pcconfig/pc.html', {'pc': pc})

"""Use a decorator user_passes_test to verify only the author has the right to edit their entries.
Follow https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.decorators.user_passes_test for more info"""

# def checkAuthor(user, pc_id):
#     PC = PC.objects.get(id=pc_id)
#     return PC.author == user


# @user_passes_test(checkAuthor, pc_id=PC_id)

@user_passes_test(lambda u: u.is_superuser)  # Only Superusers can 
def editPC(request, PC_id):

    pc = PC.objects.get(id=PC_id)
    cpu_list = CPU.objects.all()
    ram_list = RAM.objects.all()
    gpu_list = GPU.objects.all()
    motherboard_list = Motherboard.objects.all()
    storage_list = Storage.objects.all()

    # edit PC entry.
    if request.method == 'POST':
        form = AddPC(request.POST)

        if form.is_valid():
            pc.cpu = form.cleaned_data['CPU']
            pc.ram = form.cleaned_data['RAM']
            pc.gpu = form.cleaned_data['GPU']
            pc.motherboard = form.cleaned_data['Motherboard']
            pc.storage = form.cleaned_data['Storage']
            pc.price = CPU.objects.get(id=form.cleaned_data['CPU']).price + RAM.objects.get(id=form.cleaned_data['RAM']).price + GPU.objects.get(id=form.cleaned_data['GPU']).price + Motherboard.objects.get(id=form.cleaned_data['Motherboard']).price + Storage.objects.get(id=form.cleaned_data['Storage']).price
            pc.save()
            messages.success(request, "Successfully edited the PC!")
            return redirect('pcconfig:viewPC', PC_id=pc.pc_id)

        else:
            messages.warning(request, "Couldn't add a new entry!")
            return redirect('pcconfig:home')
        
    else:
        form = AddPC()
        return render(request, 'pcconfig/add.html', {'form': form, 'pc': pc, 'cpu_list': cpu_list, 'ram_list': ram_list, 'gpu_list': gpu_list, 'motherboard_list': motherboard_list, 'storage_list': storage_list})