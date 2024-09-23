from django.shortcuts import render
from .models import Account, Transfer

from django.db.models import Q

from django.http import HttpResponseRedirect, HttpResponse
import json

# Create your views here.
def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)


def register_account(request):
    account_name = request.GET.get('account_name')
    account_type = request.GET.get('account_type')
    remarks = request.GET.get('remarks')

    new_account = Account()

    # Auto Increment
    last_account = Account()

    for x in Account.objects.order_by('account_id'):
        last_account = x


    account_num = int(last_account.account_id.replace('MSME',''))
    account_num += 1
    new_account.account_id = 'MSME' + f"{account_num:07d}"
    new_account.account_name = account_name
    new_account.account_type = account_type
    new_account.remarks = remarks

    new_account.save()

    list = [{
                'account_id': new_account.account_id,
                'account_name': new_account.account_name,
                'account_type': new_account.account_name,
                'remarks': new_account.remarks,
                'result': 'Success',
    }]
    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')


def transfer(request):
    from_account = request.GET.get('from_account')
    to_account = request.GET.get('to_account')
    amount  = request.GET.get('amount')
    remark = request.GET.get('remark')


    new_transfer = Transfer()

    # Auto Increment
    last_transfer = Transfer()

    for x in Transfer.objects.order_by('transfer_id'):
        last_transfer = x

    if Transfer.objects.exists():
        transfer_num = int(last_transfer.transfer_id.replace('NLB', ''))  # Norhlan Bank
        transfer_num += 1
    else:
        transfer_num = 1

    new_transfer.transfer_id = 'NLB' + f"{transfer_num:08d}"

    new_transfer.account_from = from_account
    new_transfer.account_to = to_account

    new_transfer.amount = float(amount)
    new_transfer.remark = remark


    new_transfer.save()

    list = [{
            'transfer_id': new_transfer.transfer_id,
            'from_account' : new_transfer.account_from,
            'to_account' : new_transfer.account_to,
            'amount' : str(new_transfer.amount),
            'remark' : new_transfer.remark,
            'result': 'Success',
    }]
    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')

