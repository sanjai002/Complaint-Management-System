from django.db.models import Q
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from datetime import date
from datetime import datetime, timedelta, time
import random

def index(request):
    return render(request, 'user_login.html')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'admin_login.html',d)


def changepassword_admin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == "POST":
        o = request.POST['password']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'changepassword_admin.html',d)


def add_category(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    category = Category.objects.all()
    if request.method=="POST":
        cat = request.POST['category']
        des = request.POST['description']
        try:
            Category.objects.create(catname=cat,catdes=des)
            error = "no"
        except:
            error = "yes"
    d = {'error':error,'category':category}
    return render(request, 'add_category.html', d)


def edit_category(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        cn = request.POST['category']
        cd = request.POST['description']
        category.catname = cn
        category.catdes = cd
        try:
            category.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'category':category}
    return render(request, 'edit_category.html',d)


def delete_category(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.get(id=pid)
    category.delete()
    return redirect('add_category')

def add_subcategory(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    if request.method=="POST":
        cat = request.POST['category']
        subcat = request.POST['subcategory']
        categoryid = Category.objects.get(id=cat)
        try:
            SubCategory.objects.create(categoryid=categoryid,subcategoryname=subcat)
            error = "no"
        except:
            error = "yes"
    d = {'error':error,'category':category,'subcategory':subcategory}
    return render(request, 'add_subcategory.html', d)


def edit_subcategory(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.all()
    subcategory = SubCategory.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        catid = request.POST['category']
        subcat = request.POST['subcategory']
        categoryid = Category.objects.get(id=catid)
        subcategory.categoryid = categoryid
        subcategory.subcategoryname = subcat
        try:
            subcategory.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'category':category,'subcategory':subcategory}
    return render(request, 'edit_subcategory.html',d)

def delete_subcategory(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    subcategory = SubCategory.objects.get(id=pid)
    subcategory.delete()
    return redirect('add_subcategory')


def add_state(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    state = State.objects.all()

    if request.method=="POST":
        s = request.POST['state']

        try:
            State.objects.create(statename=s)
            error = "no"
        except:
            error = "yes"
    d = {'error':error,'state':state}
    return render(request, 'add_state.html', d)


def edit_state(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    state = State.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        s = request.POST['state']
        state.statename = s

        try:
            state.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'state':state}
    return render(request, 'edit_state.html',d)


def delete_state(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    state = State.objects.get(id=pid)
    state.delete()
    return redirect('add_state')

def Logout(request):
    logout(request)
    return redirect('index')

def registration(request):
    error = ""
    if request.method=="POST":
        fn = request.POST['fullname']
        em = request.POST['email']
        pwd = request.POST['password']
        cn = request.POST['contactno']
        try:
            user = User.objects.create_user(first_name=fn, username=em, password=pwd,last_name=cn)
            tblUser.objects.create(user=user,regdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'registration.html', d)

def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=u, password=p)

        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"

    d = {'error': error}
    return render(request, 'user_login.html', d)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    tbluser = tblUser.objects.get(user=user)
    count1 = Complaint.objects.filter(status=None,userid=tbluser).count()
    count2 = Complaint.objects.filter(status="in process",userid=tbluser).count()
    count3 = Complaint.objects.filter(status="closed",userid=tbluser).count()
    d = {'count1': count1,'count2': count2,'count3': count3}
    return render(request, 'user_home.html',d)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    state = State.objects.all()
    userinfo = tblUser.objects.get(user=request.user)
    error = ""
    if request.method == 'POST':
        fn = request.POST['fullname']
        cn = request.POST['contactno']
        addr = request.POST['address']
        st = request.POST['state']
        ct = request.POST['country']
        pc = request.POST['pincode']
        user.first_name = fn
        user.last_name = cn
        userinfo.address = addr
        userinfo.state = st
        userinfo.country = ct
        userinfo.pincode = pc
        try:
            userinfo.save()
            user.save()
            error = "no"
        except:
            error = "yes"
    d = {'state': state,'userinfo':userinfo,'error':error}
    return render(request, 'profile.html',d)


def update_image(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    userinfo = tblUser.objects.get(user=request.user)
    error = ""
    if request.method == 'POST':
        img = request.FILES['image']
        userinfo.userimage = img
        try:
            userinfo.save()
            user.save()
            error = "no"
        except:
            error = "yes"
    d = {'userinfo':userinfo,'error':error}
    return render(request, 'update_image.html',d)



def changepwd_user(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    if request.method == "POST":
        o = request.POST['password']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'changepwd_user.html',d)

def register_complaint(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    complaint=None
    category = Category.objects.all()
    state = State.objects.all()
    user = request.user
    tbluser = tblUser.objects.get(user=user)
    if request.method=="POST":
        ct = request.POST['category']
        sct = request.POST['subcategory']
        comptype = request.POST['complaintype']
        s = request.POST['state']
        noc = request.POST['noc']
        cd = request.POST['complaindetails']
        cat = Category.objects.get(id=ct)
        scat = SubCategory.objects.get(id=sct)

        complaint = Complaint.objects.create(userid=tbluser,category=cat,subcategory=scat,complainttype=comptype,state=s,complaintdetail=cd,noc=noc,regdate=date.today())
        error = "no"
        try:
            cf = request.FILES['compfile']
            complaint.complaintfile=cf
            complaint.save()
        except:
            pass

    d = {'error':error,'category':category,'state':state,'complaint':complaint}
    return render(request, 'register_complaint.html', d)

def load_subcategory(request):
    category_id = request.GET.get('category')
    subcategory = SubCategory.objects.filter(categoryid=category_id).order_by('subcategoryname')
    return render(request, 'subcategory_list.html', {'subcategory': subcategory})


def complaint_history(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    tbluser = tblUser.objects.get(user=user)
    complaint = Complaint.objects.filter(userid=tbluser)
    d = {'complaint':complaint}
    return render(request, 'complaint_history.html', d)

def complaint_details(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')

    complaint = Complaint.objects.get(id=pid)
    d = {'complaint':complaint}
    return render(request, 'complaint_details.html', d)


def notprocess_complaint(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    complaint = Complaint.objects.filter(status=None)
    d = {'complaint':complaint}
    return render(request, 'notprocess_complaint.html', d)

def complaint_detailsadmin(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    complaint = Complaint.objects.get(id=pid)

    d = {'complaint':complaint}
    return render(request,'complaint_detailsadmin.html', d)

def update_complaint(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    complaint = Complaint.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        st = request.POST['status']
        rem = request.POST['remark']
        complaint.status = st
        complaint.remark = rem
        complaint.remarkdate = date.today()
        complaint.lastupdationdate = date.today()
        try:
            complaint.save()
            error = "no"
        except:
            error = "yes"
    d = {'complaint':complaint,'error':error}
    return render(request,'update_complaint.html', d)

def user_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = User.objects.get(id=pid)
    tbluser = tblUser.objects.get(user=user)
    d = {'tbluser':tbluser}
    return render(request,'user_profile.html', d)


def manage_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    tbluser = tblUser.objects.all()
    d = {'tbluser':tbluser}
    return render(request,'manage_users.html', d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('manage_users')

def inprocess_complaint(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    complaint = Complaint.objects.filter(status="in process")
    d = {'complaint':complaint}
    return render(request, 'inprocess_complaint.html', d)

def closed_complaint(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    complaint = Complaint.objects.filter(status="closed")
    d = {'complaint':complaint}
    return render(request, 'closed_complaint.html', d)