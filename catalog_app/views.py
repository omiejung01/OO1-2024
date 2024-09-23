from django.shortcuts import render
from .models import Product
from django.http import HttpResponseRedirect, HttpResponse
import json

# Create your views here.
def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)

def product_list(request):
    #qs = PlayVideo.objects.all()
    list = [{'id': x.product_id, 'title': x.product_title, 'price': str(x.display_price),
             'image': str(x.product_pic),
         }
            for x in Product.objects.filter(void=0).order_by('-created_time')]
    #qs_json = serializers.serialize('json', list)
    qs_json = json.dumps(list)
    return HttpResponse(qs_json, content_type='application/json')


def product_detail(request):
    id = request.GET.get('id')
    list = [{

             'id': x.product_id, 'title': x.product_title, 'price': str(x.display_price),
        'unit': x.product_unit, 'description': str(x.description), 'image': str(x.product_pic),
             'updated_time': x.updated_time.strftime('%Y-%m-%d %H:%M:%S'),
             'created_time': x.created_time.strftime('%Y-%m-%d %H:%M:%S'),
             }
            for x in Product.objects.filter(product_id=id).filter(void=0).order_by('-created_time')]


    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')

