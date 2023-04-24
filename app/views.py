from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.


def insert_topic(request):
    TMF=TopicForms()
    d={'TMF':TMF}
    if request.method=='POST':
        TFO=TopicForms(request.POST)
        TFO.save()
        return HttpResponse('inserted topic data successfully')
    
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WMF=WebpageForms()
    d1={'WMF':WMF}
    if request.method=='POST':
        WFO=WebpageForms(request.POST)
        WFO.save()
        return HttpResponse('inserted webpage data successfully')
    
    return render(request,'insert_webpage.html',d1)


def insert_AccessRecords(request):
    ASMF=AccessRecordsForms()
    d2={'ASMF':ASMF}
    if request.method=='POST':
        ASFO=AccessRecordsForms(request.POST)
        ASFO.save()
        return HttpResponse('inserted AccessRecords data successfully')
    
    return render(request,'insert_accessrecords.html',d2)

