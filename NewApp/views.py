from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.conf import settings
from .models import jjcuser


   
def indexView(request):
    #return HttpResponse("Home Page")
    if request.method == 'GET':
        return render(request,'NewApp/index.html')
    elif request.method == 'POST':
        name = request.POST.get('name',False)
        email = request.POST['email']
        variety = request.POST['number-guests']
        message = request.POST['message']
        res = send_mail(
            'Request for Enquiry',
            'There has been a enquiry from ' + str(name) + ', message - ' + str(message), 
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently = False

        )
        if(res==1):
            messages.success(request,'Your request is sent successfully')

            display = "Your request is sent successfully"
        else:
            display =  "An unexpected error occured."
            messages.error(request,'Unepected error!')
        usermessage = jjcuser(Name=name,Email=email,variety=variety,messg=message,display=display)
        usermessage.save()
        #return HttpResponse(display,content_type = 'text/plain')
        #return render(request,'NewApp/index.html',{'display':display})
        return HttpResponseRedirect(request.path)
    else:
        return



