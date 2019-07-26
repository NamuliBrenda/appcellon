from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from employee.models import *
import datetime
from datetime import datetime, timedelta
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives



def email(request, type_of_leave, leave_from, leave_to, leave_days, other_reason, to, subject, html_content):
    from_email = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def email_notification(to, subject, html_content):
    from_email = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

# ------ Check if leave already applied -----------------
def is_leave_applied(request, leave_from , leave_status, employee_name, department):
    obj_emp = LeaveForm.objects.get(email=request.user.email)
    obj_emp1 = LeaveApplicationDetails.get(email=request.user.email)

    counter = LeaveApplicationDetails.objects.filter(department=obj_emp.department).filter(leave_status='Approved').filter(leave_from=obj_emp.leave_from).count()
    if counter >=1:
        raise ValueError("Date is invalid")

    else:
        if obj_emp1.employee_name == obj_emp.employee_name:
            leave_count1 = LeaveApplicationDetails.objects.filter(employee_name=obj_emp.employee_name).filter(leave_status='Approved').count()
            days_used = 0
            for leave in range(leave_count):
                leave_days = (leave_from.date() - leave_to.date()).days + 1
                days_used = days_used + leave_days
            return days_used

            if days_used >=21:
                raise ValueError("Yearly Leave Days are done ")

            else:
                no_of_days = 21 - days_used
    return no_of_days



@login_required(login_url="/login/")
class ApplyLeaveView(View):
    template_name = 'applyleave.html'

    def get(self, request):
        context = {'form': LeaveApplicationForm}
        return render(request, self.template_name, context)

    def post(self, request):
        context = {}
        form = LeaveApplicationForm(request.POST)
        leave_from = datetime.strptime(request.POST.get('leave_from'), "%Y-%m-%d")
        leave_to = datetime.strptime(request.POST.get('leave_to'), "%Y-%m-%d")
        type_of_leave = request.POST.get('type_of_leave')
       
        #print("func", type_of_leave)
        if form.is_valid():
            if leave_from > leave_to:
                context['error_message'] = 'Invalid From Date !!!'
                context['form'] = LeaveApplicationForm(request.POST)
                return render(request, self.template_name, context)


            
           

