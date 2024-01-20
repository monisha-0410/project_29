from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from app.models import *

def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse("insert_topic is done successfully")
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=Webpageform()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse("insert_webpage is done successfully")
        else:
            return HttpResponse("invalid data")
    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    EARFO=AccessRecordform()
    d={'EARFO':EARFO}
    if request.method=='POST':
        ARFDO=AccessRecordform(request.POST)
        if ARFDO.is_valid():
            ARFDO.save()
            return HttpResponse("insert_accessrecord is done successfully")
    return render(request,'insert_accessrecord.html',d)