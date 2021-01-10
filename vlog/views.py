from django.shortcuts import render,HttpResponseRedirect
from .forms import ContactFrm,SignUpform,LoginFrm,PostForm,ChangePwd,UpdateProfile
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from .models import Post

# Create your views here.

def index(req):
    All_post = Post.objects.all()
    return render(req,'vlog/index.htm',{"active":"home","All_post":All_post})


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
    if req.user.is_authenticated == False: 
        if req.method == 'POST':
            sf = SignUpform(req.POST)
            if sf.is_valid():
                sf.save()
                messages.success(req,'Account Create Successfully.')
                sf = SignUpform()
        else:
            sf = SignUpform()
        return render(req,'vlog/signup.htm',{"active":"signup","sf":sf})
    else:
        return HttpResponseRedirect('/Dashboard')

def Login(req):
    if req.user.is_authenticated == False: 
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
    else:
        return HttpResponseRedirect('/Dashboard')

def Profile(req):
    if req.user.is_authenticated:
        All_post = Post.objects.all()
        return render(req,'vlog/dashboard.htm',{"active":"profile","All_post":All_post})
    else:
        return HttpResponseRedirect('/Signin')


def Logout(req):
    logout(req)
    return HttpResponseRedirect('/Signin')


def AddPost(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
           pf = PostForm(req.POST)
           if pf.is_valid():
                pf.save()
                messages.success(req,"Post Created Successfully.")
        
        else:
            pf = PostForm()
        return render(req,'vlog/add_post.htm',{'active':'profile',"pf":pf})
        
    else:
        return HttpResponseRedirect('/Signin')



def DelRecor(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            id = req.POST.get('id')
            DelRec = Post.objects.get(id=id)
            DelRec.delete()
            messages.success(req,"Record Deleted Successfully.")
            # Post.objects.get(id = )
        return HttpResponseRedirect('/Dashboard')
    else:
        return HttpResponseRedirect('/Signin')


def Edit(req,editid):
    if req.user.is_authenticated:
        Pdata =  Post.objects.get(id=editid)
        # print(editid)
        if req.method == "POST":
            ep = PostForm(req.POST,instance = Pdata) 
            if ep.is_valid():
                ep.save()
                messages.success(req,"Post Updated Successfully.")
        else:
            ep = PostForm(instance = Pdata)
        return render(req,'vlog/edit_post.htm',{'active':'profile','ep':ep})
    else:
        return HttpResponseRedirect('/Signin')



def ChangePass(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            cp = ChangePwd(user = req.user,data = req.POST)
            # print('run')
            if cp.is_valid():
                cp.save()
                messages.success(req,"Password Reset Successfully.")
        else:
            cp = ChangePwd(user = req)
        return render(req,'vlog/change_pass.htm',{'active':'profile',"cp":cp})
    else:
        return('/Sinin')


def ChangeProfile(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            pro_up = UpdateProfile(req.POST,instance = req.user)
            if pro_up.is_valid():
                pro_up.save()
                messages.success(req,'Profile Updated Successfully.')
        else:   
            pro_up = UpdateProfile(instance = req.user)
        return render(req,'vlog/profile.htm',{'active':'profile',"pro_up":pro_up})






