from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Student

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

def signup(request):
    return render(request,'signup.html')

def page(request):
    print("Done!")
    print(request.method)
    print(request.POST)
    fn = str(request.POST['fname'])
    ln = str(request.POST['lname'])
    gn = str(request.POST['gender'])
    dt = str(request.POST['date'])
    ei = str(request.POST['email_id'])
    ph = str(request.POST['phone_number'])
    ad = str(request.POST['address'])
    ct = str(request.POST['city'])
    st = str(request.POST['state'])
    zp = str(request.POST['zip'])
    cn = str(request.POST['country'])

    return render(request,'details.html',{'fname':fn, 'lname':ln, 'gender':gn, 'date':dt, 'email_id': ei,
        'phone_number':ph, 'address':ad, 'city':ct, 'state':st, 'zip':zp, 'country':cn })
    
def registration(request):
    return render(request,'registration.html')

class studentlist(ListView):
    model = Student
    template_name = 'slist.html'