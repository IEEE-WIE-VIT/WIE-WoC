from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from myapp.models import Patient
from myapp.forms import PatientForm

# Create your views here.
def create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            pid = request.POST.get('pid', '')
            name = request.POST.get('name', '')
            contact = request.POST.get('contact', '')
            address = request.POST.get('address', '')
            doc = request.POST.get('doc', '')
            reference = request.POST.get('reference', '')
            date = request.POST.get('date', '')
            time = request.POST.get('time', '')
            p_obj = Patient(pid=pid, name=name, contact=contact, address=address, doc=doc, reference=reference, date=date, time=time)
            p_obj.save()
            return redirect('/display')
        else:
            form = PatientForm()
    return render(request,'AddData.html',{'form':Patient})

def edit(request, id):
    employee = Patient.objects.get(id=id)
    return render(request,'edit.html', {'patient1':employee})

def update(request, id):
    employee = Patient.objects.get(id=id)
    form = PatientForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/display")
    else:
        return redirect('/home')
    return render(request, 'edit.html', {'patient1': employee})

def display(request):
    patient1 = Patient.objects.all()
    return render(request, 'display.html', {'patient1': patient1})

def destroy(request, id):
    patient2 = Patient.objects.get(id=id)
    patient2.delete()
    patient1 = Patient.objects.all()
    return render(request, 'display.html', {'patient1': patient1})

def app2(request, id):
    patient1 = Patient.objects.get(id=id)
    return render(request, 'app2.html', {'patient1': patient1})

def invoice(request, id):
    patient1 = Patient.objects.get(id=id)
    return render(request, 'invoice.html', {'patient1': patient1})

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def log(request):
    return render(request,'log.html')

def display_doc(request):
    patient1 = Patient.objects.all()
    return render(request, 'display_doc.html', {'patient1': patient1})
  
