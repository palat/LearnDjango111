
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    message1 = 'TestVar1'
    message2 = 'TestVar2'
    template = loader.get_template('weather/index.html')
    context = {'message1': message1, 'message2': message2}
    return HttpResponse(template.render(context, request))
