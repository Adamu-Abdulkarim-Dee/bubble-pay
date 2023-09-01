from django.shortcuts import render, redirect
from .models import Bvn, Nin, UserInformation, NextOfKin
from bank.models import Account
from .forms import NextOfKinForm, UserInformationForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


def home_page(request):

    return render(request, 'home.html')

def user_informations(request):
    user_bvn = Bvn.objects.filter(user=request.user)
    user_nin = Nin.objects.filter(user=request.user)
    user_informations = UserInformation.objects.filter(user=request.user)
    user_next_of_kin = NextOfKin.objects.filter(user=request.user)
    accounts = Account.objects.filter(user=request.user)
    context = {
        'user_bvn': user_bvn,
        'user_nin': user_nin,
        'user_informations': user_informations,
        'user_next_of_kin': user_next_of_kin,
        'accounts': accounts
    }
    return render(request, 'UserInformation/user_information.html', context)

def create_nin(request):
    if request.method == 'POST':
        national_identification_number = request.POST.get('national_identification_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        new_nin_create = Nin.objects.create(
            user=request.user,
            national_identification_number=national_identification_number,
            first_name=first_name, last_name=last_name
        )
        new_nin_create.save()
        return redirect('BVN')
    return render(request, 'UserInformation/create_nin.html')

def create_bvn(request):
    if request.method == 'POST':
        bank_verification_number = request.POST.get('bank_verification_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        surename = request.get('surename')

        new_bvn_create = Bvn.objects.create(
            user=request.user,
            bank_verification_number=bank_verification_number,
            first_name=first_name, last_name=last_name,
            surename=surename
        )
        new_bvn_create.save()
        return redirect('Create-State-Information')
    return render(request, 'UserInformation/create_bvn.html')

def create_state_information(request):
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('Create-Next-Of-Kin')
    else:
        form = UserInformationForm()
    return render(request, 'UserInformation/create_state_informtion.html', {'form':form})

def create_next_of_king(request):
    if request.method == 'POST':
        form = NextOfKinForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
    else:
        form = UserInformationForm()
    return render(request, 'UserInformation/create_next_of_king.html', {'form':form})

def create_account(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = CustomUserCreationForm()
    return render(request, 'create_account.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('Albums')
    else:
        form = AuthenticationForm()        
    return render(request, 'login_hotel.html', {'form':form})