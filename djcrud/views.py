from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from django.shortcuts import redirect
from .models import Employee

def Home(request):
    return HttpResponse("<h2>Hello world</h2>")

def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("list")

    else:
        form = EmployeeForm()
    return render(request, "create.html", {"form":form})

def employee_list(request):
    employee = Employee.objects.all()
    number_of_employees = Employee.objects.count()
    return render(request, "list.html", {"employees":employee, "employees_number": number_of_employees})

def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        
        if form.is_valid():
            form.save()
            return redirect('list')

    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form':form})

def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == "POST":
        employee.delete()
        return redirect('list')