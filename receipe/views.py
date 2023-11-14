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
from django.contrib.auth import get_user_model
User = get_user_model()
from mypro.seen import *

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
        email=request.POST.get('email')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        password=request.POST.get('password')
        image=request.FILES['image']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'User already exists.')
            return redirect('register')
        


        name=fname+lname
        a=registered_mail(name, email)
        if a==0:
            messages.error(request, 'Please provide a valid Email address!')
            return redirect('register')


        if a==1:
            user=User.objects.create(first_name=fname, last_name=lname, email=email, image=image)
            user.set_password(password)
            user.save()
            messages.success(request, 'User registered successfully!')
            return redirect('login')  

    
    return render(request, 'receipe/register.html')

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(email=email).exists():
            messages.error(request,'user not exist')
            return redirect('login')

        user = authenticate(email=email, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')

        else:
            login(request, user)
            return redirect('home')
    return render(request, 'receipe/login.html')

def logout_page(request):
    logout(request)
    return redirect('login')


def receipe_detail(request,rId):
    obj=receipes.objects.get(id=rId)
    dic={'rec':obj}
    return render(request, 'receipe/detail_receipe.html', dic)



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
    from .seed import Report
    querySet = Marks.objects.filter(student__studentId__sReg=sId)
    print(querySet.values_list('marks', flat=True))  # Debugging line
    total_Marks = querySet.aggregate(total_Marks=Sum('marks'))['total_Marks']

    student = Student.objects.filter(studentId__sReg=sId).first()
    rank = studentReport.objects.filter(student=student).values('Rank').first()

    return render(request, 'studentResult.html', {'student': querySet, 'sum': total_Marks, 'Rank': rank['Rank']})


from receipe.tasks import *
def test(request):
    # text1.delay()
    return HttpResponse("celery is okay")