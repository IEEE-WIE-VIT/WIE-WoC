from django.shortcuts import render
from twilio.rest import Client

from reserve.models import addDetails

# Create your views here.

account_sid = 'AC6e85aac2ca9db2127e4552ef26a03a78'
auth_token = '6122eb3426d57373e15a02197affb384'
client = Client(account_sid, auth_token)

def requests(request):
    values = addDetails.objects.all()
    return render(request, 'adminRequests.html' , {"values":values})

def reject(request,value):    
    message = client.messages \
                .create(
                    body="Sorry your required sports equipment are not available ! Try again after some time",
                    from_='+18509203345',
                    to=value
                ) 
    values = addDetails.objects.all()
    return render(request, 'adminRequests.html' , {"values":values})

def accept(request,value):

    message = client.messages \
                .create(
                    body="Your required sports equipments are available ! You can take from sports room",
                    from_='+18509203345',
                    to=value
                ) 
                
    values = addDetails.objects.all()
    return render(request, 'adminRequests.html' , {"values":values})
