from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)