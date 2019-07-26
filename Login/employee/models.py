from django.db import models
from django.utils import timezone
from django import forms
#you have to import the apply for leave model
#from applyleave.models import LeaveCategory
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class LeaveForm(models.Model):
	Onleave: 'Onleave'
	Working: 'Working'

	Manager:'Manager'
	HR:'HR'
	Admin:'Admin'
	User= 'User'
    
	SICK= 'SICK'
	ANNUAL_LEAVE='ANNUAL_LEAVE'
	BEREAVEMENT='BEREAVEMENT'
	PERSONAL_LEAVE='PERSONAL_LEAVE'
	MATERNITY_OR_PATERNITY='MATERNITY_OR_PATERNITY'
	STUDY_LEAVE='STUDY_LEAVE'

	TYPE_OF_LEAVE_CHOICES = [ 
	(SICK, 'sick'),
	(ANNUAL_LEAVE,'Annual-Leave'),
	(BEREAVEMENT,'Bereavement'),
	(PERSONAL_LEAVE,'Personal-Leave'),
	(MATERNITY_OR_PATERNITY,'Maternity/Paternity'),
	(STUDY_LEAVE,'Study-Leave'),
	]

	USER_TYPE_LIST = [
    ('User', 'User'),
    ('Manager', 'Manager'),
    ('HR', 'HR'),
    ('Admin', 'Admin'),
	]

	EMPLOYEE_STATUS_LIST = [
    ('Onleave', 'Onleave'),
    ('Working', 'Working'),
    ]

	employee_name=models.CharField(max_length=100)
	email=models.EmailField(max_length=70, unique=True)
	department=models.CharField(max_length=20)
	line_supervisor=models.CharField(max_length=20)
	user_type = models.CharField(max_length=20, default='User', choices=USER_TYPE_LIST)
	leave_days = models.PositiveIntegerField(default=21, validators=[MinValueValidator(0), MaxValueValidator(21)])
	type_of_leave=models.CharField(max_length=50, choices=TYPE_OF_LEAVE_CHOICES, default=SICK)
	date_of_leave=models.DateTimeField(default=timezone.now())
	leave_from = models.DateField()
	leave_to = models.DateField()
	return_date = models.DateField()
	no_of_days = models.IntegerField()
	employee_status = models.CharField(max_length=10, default='Active', choices=EMPLOYEE_STATUS_LIST)


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


class LineSupervisor(models.Model):
    line_supervisor = models.CharField(max_length=20, unique=True, primary_key=True)

    def __str__(self):
        return self.line_supervisor


class LeaveDays(models.Model):
    leave_days = models.IntegerField( unique=True, primary_key=True)

    def __str__(self):
        return self.leave_days


class UserType(models.Model):
    user_type = models.CharField(max_length=20, unique=True, primary_key=True)

    def __str__(self):
        return self.user_type


class TypeOfLeave(models.Model):
    type_of_leave = models.CharField(max_length=2, unique=True, primary_key=True)

    def __str__(self):
        return self.type_of_leave

class EmployeeStatus(models.Model):
    employee_status = models.CharField(max_length=10, unique=True, primary_key=True)

    def __str__(self):
        return self.employee_status

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