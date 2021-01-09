from django.shortcuts import render,HttpResponseRedirect
from .forms import ContactFrm,SignUpform,LoginFrm
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(req):
    return render(req,'vlog/index.htm',{"active":"home"})


def about(req):
    return render(req,'vlog/about.htm',{"active":"about"})

def contact(req):
    if req.method == 'POST':
        cf = ContactFrm(req.POST)
        if cf.is_valid():
           cf.save()
           messages.success(req,"Request Send Successfully,Our Team Contact Very Soon.")
           cf = ContactFrm()
    else:
        cf = ContactFrm()
    return render(req,'vlog/contact.htm',{"cf":cf,"active":"contact"})


def Signup(req):
    if req.method == 'POST':
        sf = SignUpform(req.POST)
        if sf.is_valid():
            sf.save()
            messages.success(req,'Account Create Successfully.')
            sf = SignUpform()
    else:
        sf = SignUpform()
    return render(req,'vlog/signup.htm',{"active":"signup","sf":sf})


def Login(req):
    if req.method == "POST":
        lf = LoginFrm(request = req,data=req.POST)
        if lf.is_valid():
            uname = lf.cleaned_data['username']
            passr = lf.cleaned_data['password']
            logdata = authenticate(username = uname , password = passr)
            if logdata:
                login(req,logdata)
                messages.success(req,'Thank You For Login')
                return HttpResponseRedirect('/Dashboard')
    else:
        lf = LoginFrm()
    return render(req,'vlog/login.htm',{"active":"login","lf":lf})

def Profile(req):
    return render(req,'vlog/dashboard.htm')


