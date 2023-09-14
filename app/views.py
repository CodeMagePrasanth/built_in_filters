from django.shortcuts import render

# Create your views here.
import datetime

def builtin_filters(request):
    data='AnJum is good Girl'
    d={'data' : data}
    dt=datetime.datetime.now()
    return render(request,'builtin_filters.html',d)


