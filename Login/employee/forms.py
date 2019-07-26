from django.forms import ModelForm
from .models import *
from django import forms
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class RawLeaveForm(forms.ModelForm):
	employee_name = forms.CharField(max_length=20, label='Employee Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'name': 'employee_name'}))
	department = forms.CharField(max_length=20, label='Department', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'department', 'name': 'department'}))
	email= forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email Address', 'name': 'email',}))
	line_supervisor = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supervisor', 'name': 'line_supervisor',}))
	user_type = forms.ModelChoiceField(queryset=UserType.objects.all().distinct(), label='User Type', widget=forms.Select(attrs={'class': 'form-control', 'name': 'user_type', 'id': 'user_type'}), required=True)
	leave_days = forms.IntegerField(label='Yearly Leave Days', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total Leave Days', 'name': 'leave_days'}))
	type_of_leave = forms.ModelChoiceField(queryset=TypeOfLeave.objects.all().distinct(), label='Type of Leave', widget=forms.Select(attrs={'class': 'form-control',  'name': 'type_of_leave'}), required=True)
	date_of_leave = forms.DateTimeField(label='Date of Leave' ,widget=forms.DateInput(attrs={'class':'form-control', 'placeholder': 'yyyy-mm-dd', 'name':'date_of_leave'}))
	leave_from = forms.DateField(label='From' ,widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'name': 'leave_from', 'data-date-format':'yyyy-mm-dd'}))
	leave_to = forms.DateField(label='To', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'name':'leave_to', 'data-date-format':'yyyy-mm-dd'}))
	return_date = forms.DateField(label='Return Date', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'name':'return_date', 'data-date-format':'yyyy-mm-dd'}))
	no_of_days = forms.IntegerField(label='Number of Days', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Remaining Leave days', 'name':'no_of_days'}))
	employee_status = forms.ModelChoiceField(queryset=EmployeeStatus.objects.all().distinct(), label='Employee Status', widget=forms.Select(attrs={'class': 'form-control', 'name': 'employee_status', 'id': 'employee_status'}), required=True)

	
	class Meta(object):
		model = LeaveForm
		fields = [ 'employee_name', 'email', 'department', 'line_supervisor', 'user_type', 'type_of_leave', 'date_of_leave', 'leave_from', 'leave_to', 'return_date', 'no_of_days', 'employee_status']
        #exclude = []