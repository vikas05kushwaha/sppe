
#   new code 
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,HttpResponseRedirect
from .models import Employee
from .forms import EmployeeForm
from api.helpers import validate_email,validate_mobile_number

# from .serializers import EmployeeSerializer

def index(request):
    return render(request, 'employee_list.html')


# Get list of all employees
def getEmployeeList(request):
    try:
        employees = Employee.objects.all()
        employeeList = [{"id": emp.id, "name": f"{emp.name} ", "email": emp.email,"age": emp.age,"phone_no": emp.phone_no,"gender": emp.gennder } for emp in employees]
        return JsonResponse({"status": "success", "employees": employeeList})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

from django.db.models import Q

# Create a new employee
def createEmployee(request):
    if request.method == 'POST':
        try:
            form = EmployeeForm(request.POST)
            emailId=request.data.get('email')
            mobile=request.data.get('phone_no')
            email,phone=validate_email(emailId),validate_mobile_number(mobile)
            employee = Employee.objects.filter(Q(email=emailId) | Q(phone_no=mobile)).first()
            if employee:
                return JsonResponse({"status": "error", "message": "User Already registered"})

            if (email and phone) is False:
                print("wrong data")
                return JsonResponse({"status": "error", "message": "Invalid {0}".format("email" if email is False else "Mobile")})

            if form.is_valid():
                form.save()
                return JsonResponse({"status": "success", "message": "Employee created successfully!"})
            else:
                return JsonResponse({"status": "error", "message": "Invalid form data!"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})


# Update an employee's information
def updateEmployee(request, id):
    if request.method == 'POST':
        try:
            employee = get_object_or_404(Employee, id=id)
            form = EmployeeForm(request.POST, instance=employee)

            if form.is_valid():
                form.save()
                return JsonResponse({"status": "success", "message": "Employee updated successfully!"})
            else:
                return JsonResponse({"status": "error", "message": "Invalid form data!"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})




def get_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        # serializer = EmployeeSerializer(employee)
        return JsonResponse({'status': 'success', 'employee': employee.data})
    except Employee.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Employee not found.'})
        

# Delete an employee
def deleteEmployee(request, id):
    try:
        employee = get_object_or_404(Employee, id=id)
        employee.delete()
        return JsonResponse({"status": "success", "message": "Employee deleted successfully!"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
