from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Employee
from django.contrib import messages

# Create your views here.
def index(request):
    employee = Employee.objects.all()
    context = {
            'employee':employee,
        }
    return render(request,'index.html',context)

def employe(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data['first']
        last_name = data['last']
        email = data['email']
        print(first_name)
        emp = Employee(first_name=first_name,last_name=last_name,email=email)
        emp.save()
        messages.success(request, 'Employee has been added')
        return redirect('/')

    return render(request,'index.html',)

def employeUpdate(request, id):
    # print(id)
    emp = Employee.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        emp.first_name = data['first']
        emp.last_name = data['last']
        emp.email = data['email']
        emp.save()
        messages.success(request, 'Employee has been updated')
        return redirect('/')
    # return render(request,'index.html')

    context = {
        'employee': emp,
    }
    return render(request,'employee_update.html', context)

def employeDelete(request,id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    messages.warning(request, 'Employee has been removed')
    return redirect('/')