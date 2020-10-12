from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . forms import *
from . models import *

def homepage(request):
    return render(request, 'index.html')

def register_schooladmin(request):
    if request.method == 'POST':
        form = SchoolAdminForm(request.POST,request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.is_schooladmin=True
            form.email = form.username
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect(login)
        else:
            form = SchoolAdminForm()
            messages.error(request, 'Invalid ')
            return render(request, 'register_schooladmin.html', {'form': form})
    else:
        form = SchoolAdminForm()
        return render(request, 'register_schooladmin.html', {'form': form})



def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.is_student=True
            form.email = form.username
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect(login_user)
        else:
            form = StudentForm()
            messages.error(request, 'Invalid ')
            return render(request, 'register_student.html', {'form': form})
    else:
        form = StudentForm()
        return render(request, 'register_student.html', {'form': form})

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            login(request, user)
            if request.user.is_student==True:
                return redirect(homepage)
            else:
                return redirect(homepage)
        else:
            messages.error(request,'Invalid email or Password')
            return render(request, 'login.html')
    else:
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect(login_user)


def send_notes(request):
    if request.method == 'POST':
        form = TextnotesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully')
            return redirect(homepage)
        else:
            form = TextnotesForm()
            messages.error(request, 'Invalid ')
            return render(request, 'send_notes.html', {'form': form})
    else:
        form = TextnotesForm()
        return render(request, 'send_notes.html', {'form': form})


def see_notes(request):
    notes = Textnotes.objects.filter(student=request.user)
    return render(request, 'see_notes.html', {'notes': notes})


def admin_show_notes(request):
    notes = Textnotes.objects.all()
    return render(request, 'admin_show_notes.html', {'notes': notes})

def admin_delete_notes(request,id):
    obj = Textnotes.objects.get(id=id)
    obj.delete()
    return redirect(admin_show_notes)