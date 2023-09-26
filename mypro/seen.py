from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
def index(request):
    return render(request,'index.html')


def about(request):
    return HttpResponse('this is ejaaz ')



def send_email(request):

    # return HttpResponse('send mail')
    subject = "Hello user! you have received this mail from Django server"
    message = "please let us know about our services"
    receiver = ["ijaz.professional@gmail.com","mustafakhan6816899@gmail.com"]

    send=send_mail(subject, message, settings.EMAIL_HOST_USER, receiver)

    if(send==1):
        result = "send successfully"
    else:
        result = "sending failed"
    return HttpResponse(result)

def send_emaal_attachment(request):
    # return HttpResponse('send mail')
    subject = "Hello user! you have received this mail from Django server"
    message = "please let us know about our services"
    receiver = ["ijaz.professional@gmail.com"]
    path = f"{settings.BASE_DIR}/invitation.png"
    mail=EmailMessage(subject, message, settings.EMAIL_HOST_USER, receiver)
    mail.attach_file(path)
    a=mail.send()
    if(a==1):
        result = "send successfully"
    else:
        result = "sending failed"
    return HttpResponse(result)

def registered_mail(name, email):

    subject = f"Hi {name},"
    message = "You are welcome on Receipe appp. Thanx for registering yourself"
    receiver = [email]

    send=send_mail(subject, message, settings.EMAIL_HOST_USER, receiver)
    print(send)
    if(send==1):
        return 1
    else:
        return 0