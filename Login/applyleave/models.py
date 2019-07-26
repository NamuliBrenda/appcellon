from django.db import models
from employee.models import *
from datetime import datetime

# Create your models here.

class LeaveRegister(models.Model):
	January:'January'
	February:'February'
	March:'March'
	April:'April'
	May:'May'
	June:'June'
	July:'July'
	August:'August'
	September:'September'
	October:'October'
	November:'November'
	December:'December'

	

	FY_CHOICE=[
		('2018','2018'),
		('2019', '2019'),
	]


	MONTH_CHOICES=[
	    ('January','January'),
	    ('February', 'February'),
	    ('March', 'March'),
	    ('April', 'April'),
	    ('May', 'May'),
	    ('June', 'June'),
	    ('July', 'July'),
	    ('August', 'August'),
	    ('September', 'September'),
	    ('October', 'October'),
	    ('November', 'November'),
	    ('December', 'December'),
	   ]


	email=models.EmailField(max_length=70, unique=True)
	employee_name=models.CharField(max_length=100)
	department=models.CharField(max_length=20)
	financial_year =models.IntegerField( choices=FY_CHOICE, default=2018)
	#leave_month=models.CharField(max_length=30, choices=MONTH_CHOICES)
	leave_month = models.DateField(blank=True, null=True)
	line_supervisor_name=models.CharField(max_length=20)
	line_supervisor_email=models.CharField(max_length=20)

	def __str__(self):
		return self.employee_name
        

	
    
class LeaveApplication(models.Model):

	Approve: 'Approve'
	Reject: 'Reject'

	    
	Sick:'Sick'
	Annual_Leave:'Annual_Leave'
	Bereavement:'Bereavement'
	Personal_Leave:'Personal_Leave'
	Maternity_or_Paternity:'Maternity/Paternity'
	Study_Leave:'Study_Leave'
		

	Approved= 'Approved'
	Pending= 'Pending'
	Rejected= 'Rejected'

	TYPE_OF_LEAVE_CHOICES = [ 
		
	]

	FY_CHOICE=[
		('2018','2018'),
		('2019', '2019'),
	]

	APPROVE_CHOICES=[
		('Approve', 'Approve'),
		('Reject', 'Reject'),
	]

	MONTH_CHOICES=[
	    ('January','January'),
	    ('February', 'February'),
	    ('March', 'March'),
	    ('April', 'April'),
	    ('May', 'May'),
	    ('June', 'June'),
	    ('July', 'July'),
	    ('August', 'August'),
	    ('September', 'September'),
	    ('October', 'October'),
	    ('November', 'November'),
	    ('December', 'December'),
	   ]


	LEAVE_STATUS_CHOICES=[
	    ('Approved', 'Approved'),
	    ('Pending', 'Pending'),
	    ('Rejected', 'Rejected')
	]

	employee_name=models.CharField(max_length=100)
	email=models.EmailField(max_length=70, unique=True)
	department=models.CharField(max_length=20)
	type_of_leave=models.CharField(max_length=50, choices=TYPE_OF_LEAVE_CHOICES)
	leave_days=models.IntegerField(default=0)
	other_reason=models.CharField(max_length=100)
	financial_year =models.IntegerField( choices=FY_CHOICE, default=2018)
	date_of_leave=models.DateTimeField(default=datetime.now())
	leave_from = models.DateField()
	leave_to = models.DateField()
	return_date = models.DateField()
	no_of_days = models.IntegerField()
	line_supervisor_name=models.CharField(max_length=20)
	line_supervisor_email=models.CharField(max_length=20)
	leave_status = models.CharField(max_length=50, choices=LEAVE_STATUS_CHOICES)
	approve_category = models.CharField(max_length=50, choices=APPROVE_CHOICES)
	line_supervisor_remarks = models.CharField(max_length=200, blank=True, null=True, help_text="Maximum Limit is 200 Characters")

	def __str__(self):
		return self.employee_name


class LeaveApplicationDetails(models.Model):
	January:'January'
	February:'February'
	March:'March'
	April:'April'
	May:'May'
	June:'June'
	July:'July'
	August:'August'
	September:'September'
	October:'October'
	November:'November'
	December:'December'

	Approve: 'Approve'
	Reject: 'Reject'

	    
	Sick:'Sick'
	Annual_Leave:'Annual_Leave'
	Bereavement:'Bereavement'
	Personal_Leave:'Personal_Leave'
	Maternity_or_Paternity:'Maternity/Paternity'
	Study_Leave:'Study_Leave'
		

	Approved= 'Approved'
	Pending= 'Pending'
	Rejected= 'Rejected'

	TYPE_OF_LEAVE_CHOICES = [ 
		
	]

	FY_CHOICE=[
		('2018','2018'),
		('2019', '2019'),
	]

	APPROVE_CHOICES=[
		('Approve', 'Approve'),
		('Reject', 'Reject'),
	]


	LEAVE_STATUS_CHOICES=[
	    ('Approved', 'Approved'),
	    ('Pending', 'Pending'),
	    ('Rejected', 'Rejected')
	]

	employee_name=models.CharField(max_length=100)
	email=models.EmailField(max_length=70, unique=True)
	department=models.CharField(max_length=20)
	type_of_leave=models.CharField(max_length=50, choices=TYPE_OF_LEAVE_CHOICES)
	leave_month = models.DateField()
	leave_days=models.IntegerField(default=0)
	other_reason=models.CharField(max_length=100)
	financial_year =models.IntegerField( choices=FY_CHOICE, default=2018)
	date_of_leave=models.DateTimeField(default=datetime.now())
	leave_from = models.DateField()
	leave_to = models.DateField()
	return_date = models.DateField()
	no_of_days = models.IntegerField()
	line_supervisor_name=models.CharField(max_length=20)
	line_supervisor_email=models.CharField(max_length=20)
	leave_status = models.CharField(max_length=50, choices=LEAVE_STATUS_CHOICES)
	approve_category = models.CharField(max_length=50, choices=APPROVE_CHOICES)
	line_supervisor_remarks = models.CharField(max_length=200, blank=True, null=True, help_text="Maximum Limit is 200 Characters")

	def __str__(self):
		return self.employee_name

class EmployeeName(models.Model):
    employee_name = models.CharField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
    	return self.employee_name
        

class Email(models.Model):
    email = models.EmailField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return self.email


class Department(models.Model):
    department = models.CharField(max_length=50, unique=True, primary_key=True)

    def __str__(self):
        return self.department

class LeaveMonth(models.Model):
    leave_month = models.DateField(unique=False, primary_key=True)

    def __str__(self):
        return self.leave_month

class LineSupervisor(models.Model):
    line_supervisor = models.CharField(max_length=20, unique=True, primary_key=True)

    def __str__(self):
        return self.line_supervisor

class TypeOfLeave(models.Model):
    type_of_leave = models.CharField(max_length=20, unique=True, primary_key=True)

    def __str__(self):
        return self.type_of_leave

class LeaveDays(models.Model):
    leave_days = models.IntegerField(max_length=20, unique=True, primary_key=True)

    def __str__(self):
        return self.leave_days

class OtherReason(models.Model):
	other_reason = models.CharField(max_length=100, unique=False, primary_key=True)

	def __str__(self):
		return self.other_reason

class FinancialYear(models.Model):
	financial_year = models.IntegerField( unique=False, primary_key=True)
	set_current = models.CharField(choices=(('YES', 'YES'), ('NO', 'NO')), max_length=3)

	def __str__(self):
		return self.financial_year

class DateOfLeave(models.Model):
    date_of_leave = models.DateField(unique=True, primary_key=True)

    def __str__(self):
        return self.date_of_leave

class LeaveFrom(models.Model):
    leave_from = models.DateField(unique=True, primary_key=True)

    def __str__(self):
        return self.leave_from

class LeaveTo(models.Model):
    leave_to = models.DateField(unique=True, primary_key=True)

    def __str__(self):
        return self.leave_to


class NumberOfDays(models.Model):
    no_of_days = models.IntegerField( unique=True, primary_key=True)

    def __str__(self):
        return self.no_of_days

class ReturnDate(models.Model):
    return_date = models.DateField(unique=True, primary_key=True)

    def __str__(self):
        return self.return_date

class LineSupervisorEmail(models.Model):
    line_supervisor_email = models.EmailField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return self.line_supervisor_email

class LeaveStatus(models.Model):
    leave_status = models.EmailField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return self.leave_status

class Remarks(models.Model):
    line_supervisor_remarks = models.EmailField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return self.line_supervisor_remarks