from django.shortcuts import render
from .models import Transaction

def transaction_list(request):
    transactions = Transaction.objects.all()
    context = {
        'transactions': transactions
    }
    return render(request, 'payments/transaction_list.html', context)
