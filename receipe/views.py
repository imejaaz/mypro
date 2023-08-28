from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.http import HttpResponse
from receipe.models import receipes
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q,Sum
from receipe.models import *


import time
@login_required(login_url='login')
def index(request):
    rec = receipes.objects.all()
    dic = {'r': rec}
    print(dic)
    return render(request, 'receipe/index.html',dic)
@login_required(login_url='login')
def forms(request):
    return render(request, 'receipe/form.html')
def formSubmit(request):
    if request.method=='POST':
        img=request.FILES.get('receipeImg')
        name=request.POST.get('receipeName')
        desc=request.POST.get('receipeDisc')
        data=receipes(name=name, desc=desc, img=img)
        data.save()
    return redirect('home')


    # return render(request, 'receipe/form.html')
@login_required(login_url='login')
def delete_receipe(request,id):
    d=receipes.objects.get(id=id)
    d.delete()
    return redirect('home')
@login_required(login_url='login')
def update_receipe(request,id):
    qset=receipes.objects.get(id=id)
    d={'rec': qset}
    if request.method == 'POST':
        name=request.POST.get('receipeName')
        desc=request.POST.get('receipeDisc')
        img=request.FILES.get('receipeImg')
        if img:
            qset.img=img
        if name:
            qset.name=name
        qset.desc=desc
        qset.save()
        return redirect('home')

    return render(request, 'receipe/update_receipe.html', d)

@login_required(login_url='login')
def search(request):
    sk=(request.GET.get('search_key'))
    print(sk)
    qs=receipes.objects.filter(name__icontains = sk)
    dc={'r':qs}
    return render(request, 'receipe/index.html',dc)

def register_form(request):
    if request.method =='POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        password=request.POST.get('password')


        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists.')
            return redirect('register')

        user=User.objects.create(first_name=fname, last_name=lname, username=username)
        user.set_password(password)
        user.save()
        messages.success(request,'registered successfully')
        return redirect('login')
    return render(request, 'receipe/register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'user not exist')
            return redirect('login')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')

        else:
            login(request, user)
            return redirect('home')
    return render(request, 'receipe/login.html')

def logout_page(request):
    logout(request)
    return redirect('login')



# student record list.....
def get_student(request):
    so = Student.objects.all()

    if request.GET.get('search'):
        searchkey=request.GET.get('search')
        result=Student.objects.filter(
            Q(studentName__icontains = searchkey) |
            Q(department__department__icontains = searchkey) |
            Q(studentAddress__icontains = searchkey) |
            Q(studentAge__icontains = searchkey) |
            Q(studentEmail__icontains = searchkey)

        )

        dic = {'student': result}
        return render(request, 'studentList.html', dic)

    paginator = Paginator(so, 10)
    page_number = request.GET.get("page",1)
    so = paginator.get_page(page_number)
    dic = {'student': so}
    return render(request, 'studentList.html', dic)



def studentResult(request, sId):
    querySet = Marks.objects.filter(student__studentId__sReg=sId)
    print(querySet.values_list('marks', flat=True))  # Debugging line
    total_Marks = querySet.aggregate(total_Marks=Sum('marks'))['total_Marks']
    return render(request, 'studentResult.html', {'student': querySet, 'sum': total_Marks})
