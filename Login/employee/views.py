from django.shortcuts import render
from employee.forms import RawLeaveForm
from employee.models import *
from django.contrib.auth.models import User
 

# Create your views here.
#@login_required(login_url='/login/')
def add_employee_view(request):
    context = {
        'form': RawLeaveForm(),
        'obj_Employee_Name': EmployeeName.objects.all(),
        'obj_Email': Email.objects.all(),
        'obj_Department': Department.objects.all(),
        'obj_Line_Supervisor': LineSupervisor.objects.all(),
        'obj_Leave_Days': LeaveDays.objects.all(),
        'obj_Type_Of_Leave': TypeOfLeave.objects.all(),
        'obj_User_Type': UserType.objects.all(),
        'obj_Emp_Status': EmployeeStatus.objects.all(),
        'obj_Date_of_Leave': DateOfLeave.objects.all(),
        'obj_Leave_From': LeaveFrom.objects.all(),
        'obj_Leave_To': LeaveTo.objects.all(),
        'obj_Number_Of_Days': NumberOfDays.objects.all(),
        'obj_Return_Date': ReturnDate.objects.all(),
            }

    if request.method == 'POST':
        form =RawLeaveForm(request.POST)
        if form.is_valid():
            # form.save()
            employee_name = re.sub(' +', ' ', request.POST.get('employee_name', '')).strip()
            department = re.sub(' +', ' ', request.POST.get('department', '')).strip()
            email = re.sub(' +', ' ', request.POST.get('email', '')).strip()
            leave_days = re.sub(' +', request.POST.get('leave_days', '')).strip()
            type_of_leave = request.POST.get('type_of_leave', '')
           	
            user_type = request.POST.get('user_type', '')
            line_supervisor = re.sub(' +', ' ', request.POST.get('line_supervisor', '')).strip()
            date_of_leave = request.POST.get('date_of_leave', '')
            leave_from = request.POST.get('leave_from', '')
            leave_to = request.POST.get('leave_to', '')
            return_date = request.POST.get('return_date', '')
            employee_status = request.POST.get('employee_status')

            emp_obj = LeaveForm(employee_name=employee_name,department=department,email=email,leave_days=leave_days, 
            						  type_of_leave=type_of_leave,user_type=user_type,line_supervisor=line_supervisor, 
                                      date_of_leave=date_of_leave, leave_from=leave_from, leave_to=leave_to, 
                                      return_date=return_date ,employee_status=employee_status)

            emp_obj.save()
            context = {
                'save_message': 'Data has been Saved. !!!'
            }
            return render(request, 'employee/add_employee.html', context)
       	else:
           	form = RawLeaveForm()
           	return render(request, 'employee/add_employee.html', context)
    else:
        return render(request, 'employee/add_employee.html', context)

def employee_list_view(request):
    context = {
        'obj_emp': LeaveForm.objects.all().order_by('employee_name'),
    }
    return render(request, 'employee/list_employee.html', context)

def employee_details_view(request, id=None):
    context = {}
    obj_emp = LeaveForm.objects.get(employee_name=id)
    context['obj_emp'] = obj_emp
    return render(request, 'employee/view_employee.html', context)

def employee_edit_view(request, id=None):
    context = {
        'form': RawLeaveForm(),
        'obj_Employee_Name': EmployeeName.objects.all(),
        'obj_Email': Email.objects.all(),
        'obj_Department': Department.objects.all(),
        'obj_Line_Supervisor': LineSupervisor.objects.all(),
        'obj_Leave_Days': LeaveDays.objects.all(),
        'obj_Type_Of_Leave': TypeOfLeave.objects.all(),
        'obj_User_Type': UserType.objects.all(),
        'obj_Emp_Status': EmployeeStatus.objects.all(),
        'obj_Date_of_Leave': DateOfLeave.objects.all(),
        'obj_Leave_From': LeaveFrom.objects.all(),
        'obj_Leave_To': LeaveTo.objects.all(),
        'obj_Number_Of_Days': NumberOfDays.objects.all(),
        'obj_Return_Date': ReturnDate.objects.all(),
    }

    obj_emp = LeaveForm.objects.get(employee_name=id)
    context['obj_emp'] = obj_emp
    if request.method == 'POST':
        form = RawDataForm(request.POST, instance=obj_emp)
        context['form'] = form
        if form.is_valid():
            form.save()
            context['form'] = RawDataForm(request.POST, instance=obj_emp)
            context['save_message'] = 'Updated Successfully !!!'
            return render(request, 'employee/edit_employee.html', context)
        else:
            context['save_message'] = 'Invalid Input !!!'
            return render(request, 'employee/edit_employee.html', context)
    return render(request, 'employee/edit_employee.html', context)

def employee_delete_view(request, id=None):
    context = {
        'form': RawLeaveForm(),
         'obj_Employee_Name': EmployeeName.objects.all(),
        'obj_Email': Email.objects.all(),
        'obj_Department': Department.objects.all(),
        'obj_Line_Supervisor': LineSupervisor.objects.all(),
        'obj_Leave_Days': LeaveDays.objects.all(),
        'obj_Type_Of_Leave': TypeOfLeave.objects.all(),
        'obj_User_Type': UserType.objects.all(),
        'obj_Emp_Status': EmployeeStatus.objects.all(),
        'obj_Date_of_Leave': DateOfLeave.objects.all(),
        'obj_Leave_From': LeaveFrom.objects.all(),
        'obj_Leave_To': LeaveTo.objects.all(),
        'obj_Number_Of_Days': NumberOfDays.objects.all(),
        'obj_Return_Date': ReturnDate.objects.all(),
        }

    obj_emp = LeaveForm.objects.get(employee_name=id)
    context['obj_emp'] = obj_emp
    if request.method == 'POST':
        form = RawDataForm(request.POST, instance=obj_emp)
        context['form'] = form
        obj_emp.delete()
        context['save_message'] = 'Deleted Successfully !!!'
        return render(request, 'employee/delete_employee.html', context)
    return render(request, 'employee/delete_employee.html', context)

#@login_required(login_url='/login/')
def profile_view(request):
     context = {}
#    user_obj = User.objects.get(email=request.user.email)
#    obj_emp = LeaveForm.objects.get(email=user_obj.email)
#    context['obj_emp'] = obj_emp
     return render(request, 'employee/view_profile.html', context)