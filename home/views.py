from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def message(request,msg):

    return render(request,'message.html',{'msg':msg})


def contact(request):
    if request.method=="POST":
        email =request.POST['email']
        name=request.POST['name']
        subject = request.POST['subject']
        msg = request.POST['message']
        sendermail = 'lostandfound.helpdesk@gmail.com'
        send_mail(
                    subject,
                    msg + " send by " +name+ " senders email id is "+email,
                    'sa.stutiagrawal@example.com',
                    [sendermail],
                    fail_silently=False,
                )

        info = 'Your message has been sent to the organization helpdesk. We will contact you soon.'
           
        return render(request,'message.html',{'msg':info})
        
    else:
        return render(request,'contact.html')

    