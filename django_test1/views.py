from django.shortcuts import render
from django.http import HttpResponse
from django_test1.models import ArtiInfo
from django_test1.models import IpInfo

def index(request):
    arti_info = ArtiInfo.objects[1024]
    context={
        'title':arti_info.date,
        "des":arti_info.aluminium_price,
        "score":arti_info.coper_price,
    }
    # return HttpResponse("&lt;p&gt;Hello World&lt;/p&gt;")
    return render(request,'index.html',context=context)

def ip(request):
    ip_info = IpInfo.objects[0]
    ip = ip_info["ip"]
    return HttpResponse("ip:{}".format(ip))

# Create your views here.
