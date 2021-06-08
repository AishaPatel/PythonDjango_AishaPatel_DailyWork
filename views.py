from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return render(request,'home.html')

def aboutpageview(request):
    return render(request,'about.html')

def contactpageview(request):
    return render(request,'contact.html')

def myform(request):
    return render(request,'myform.html')

def process(request):
    print("Welcome")
    print(request.method)
    print(request.POST)
    a = int(request.POST['txt1'])
    b = int(request.POST['txt2'])
    c = a + b
    print(c)
    return render(request,'ans.html',{'mya':a,'myb':b,'mysum':c})

