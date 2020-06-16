""" Platzigram views """
#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %d %Y - %H:%M hrs')
    return HttpResponse(f'Current server time: {str(now)}')


def hello(request):
    import pdb; pdb.set_trace()
    return HttpResponse('Hello')