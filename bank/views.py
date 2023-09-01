from django.shortcuts import render, redirect
from .models import Wallet, Transaction, Account

def dashboard(request):
    wallets = Wallet.objects.filter(user=request.user)
    context = {
        'wallets':wallets
    }
    return render(request, 'Profile/dashboard.html', context)

def transfer(request):

    return render(request, 'Profile/transfer.html')

def history(request):
    transactions = Transaction.objects.filter(user=request.user)
    context = {
        'transactions':transactions
    }
    return render(request, 'Profile/history.html', context)

def make_transfer(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        name = request.POST.get('name')
        amount = request.POST.get('amount')

        sender_wallet = Wallet.objects.get(user=request.user)

        if sender_wallet.amount >= amount:
            sender_wallet.balance -= amount
            sender_wallet.save()
        else:
            messages.success('Insufficient funds')
    return render(request, 'Profile/make_transfer.html')

def transfer_to_other(request):

    return render(request, 'transfer-to-other')