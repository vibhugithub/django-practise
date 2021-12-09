from django.shortcuts import render
from email_sender.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

# Create your views here.
def Emaill(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Quote Of The Day'
        message = 'The best preparation for tomorrow is doing your best today.'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'send/success.html', {'recepient': recepient})
    return render(request, 'send/index.html', {'form':sub})