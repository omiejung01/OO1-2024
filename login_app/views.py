from django.shortcuts import render

from .models import AppUser
from django.http import HttpResponseRedirect, HttpResponse
import json
import bcrypt

def my_salt():
    return ('$2b$12$tUimG74HOCBiAA7sm3QX9e').encode('utf-8')

# Create your views here.
def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)

def user_list(request):
    #qs = PlayVideo.objects.all()
    list = [{'display_name': x.display_name, 'email': x.email
         }
            for x in AppUser.objects.filter(void=0).order_by('-created_time')]
    #qs_json = serializers.serialize('json', list)
    qs_json = json.dumps(list)
    return HttpResponse(qs_json, content_type='application/json')


def login(request):
    list2 = [{
        'email': 'invalid',
        'display_name': 'not specified',
        'result': 'Failure',
    }]

    login_email = request.GET.get('email')
    login_password = str(request.GET.get('password'))

    bytePwd = login_password.encode('utf-8')
    hash = bcrypt.hashpw(bytePwd, my_salt())

    decoded_password = hash.decode('utf-8')

    list = [{

        'display_name': x.display_name,
        'updated_time': x.updated_time.strftime('%Y-%m-%d %H:%M:%S'),
        'created_time': x.created_time.strftime('%Y-%m-%d %H:%M:%S'),
    }
    for x in AppUser.objects.filter(email=login_email).filter(password=decoded_password).filter(void=0).order_by('-created_time')]

    if (len(list) > 0):
        display_name_temp = ''
        for i in list:
            #print(i)
            display_name_temp = i['display_name']

        list2 = [{
            'email': login_email,
            'display_name': display_name_temp,
            'result': 'Failure',
        }]

    qs_json = json.dumps(list2)
    return HttpResponse(qs_json, content_type='application/json')
