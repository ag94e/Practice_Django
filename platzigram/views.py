""" Platzigram views """
#Django
from django.http import HttpResponse, JsonResponse

#Utilities
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %d %Y - %H:%M hrs')
    return HttpResponse(f'Current server time: {str(now)}')


def sorted_intergers(request):
    #import pdb; pdb.set_trace()
    num = [int(i) for i in request.GET['numbers'].split(',')]
    num_sorted = sorted(num)
    resp = JsonResponse(num, safe=False)

    return HttpResponse(resp)


def say_hi(request, name, age):
    if age < 12:
        message = f'Sorry {name} you are not allowed here'
    else:
        message = f'Welcome to platzigram {name}'
    return HttpResponse(message)