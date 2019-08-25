
#django
from django.http import HttpResponse

#utilities
from datetime import datetime
import json 


def hello_world(request):
    
    return HttpResponse("oh, hi! , Current server time is {now}".format(
        now= datetime.now().strftime('%b %dth, %y - %H:%M hrs')
    ))

def sorted_integers(request):
    #return a json response with sorted integers
    numbers        = [int (i) for i in request.GET['numbers'].split(',')]
    sorted_ints  = sorted(numbers)
    #data que será mostrada
    data = {
        'status' : 'ok',
        'numbers': sorted_ints,
        'message': 'Integer sorted succesfully'
    }
    return HttpResponse(
        json.dumps(data),
        content_type='application/json'
    )

def say_hi(request, name, age):
    """"Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you not allowed here'.format(name)
    else:
        message = 'Hello, welcome to pettygram'.format(name)

    return HttpResponse(message)




