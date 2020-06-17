""" Platzigram views """
#Django
from django.http import HttpResponse, JsonResponse

#Utilities
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %d %Y - %H:%M hrs')
    return HttpResponse(f'Current server time: {str(now)}')


def hello(request):
    #import pdb; pdb.set_trace()
    num = request.GET['numbers'].split(',')
    num.sort()
    resp = JsonResponse(num, safe=False)
    return HttpResponse(resp)