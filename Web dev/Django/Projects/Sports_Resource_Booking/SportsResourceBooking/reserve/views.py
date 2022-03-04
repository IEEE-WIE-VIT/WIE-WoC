from django.shortcuts import render
from .models import addDetails
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.


def addInfo(request):
   
    try:
       noOfitems = request.POST['no_of_items']
    except MultiValueDictKeyError:
       noOfitems = 0
    try:
       times = request.POST['timings']
    except MultiValueDictKeyError:
        times="00:00"
    try:
        equipment_type = request.POST['equipment_type']
    except MultiValueDictKeyError:
        equipment_type = "none"

    obj = addDetails(idno=request.user.username,phno = request.user.last_name,equipment_type=equipment_type,noOfitems=noOfitems,times=times)
    obj.save()
    return render(request,'form.html') 

