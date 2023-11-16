from django.shortcuts import render

# Create your views here.
def ren(request):
    d={'assumption':'balu','assumption2':'mahesh'}
    return render(request,'r.html',context=d)