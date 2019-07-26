from django import forms
from django.forms import ModelForm
from applyleave.models import *

class LeaveApplicationForm(forms.ModelForm):
	employee_name = forms.CharField(max_length=20, label='Employee Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'name': 'employee_name'}))
	department = forms.CharField(max_length=20, label='Department', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'department', 'name': 'department'}))
	email= forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email Address', 'name': 'email',}))
	type_of_leave = forms.ModelChoiceField(queryset=TypeOfLeave.objects.all().distinct(), label='Type of Leave', widget=forms.Select(attrs={'class': 'form-control',  'name': 'type_of_leave'}), required=True)
	leave_days = forms.IntegerField(label='Leave Days', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Leave Days', 'name':'leave_days'}))
	other_reason = forms.CharField(label='Other Reasons For Leave', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Please Specify', 'name':'other_reason' }))
	financial_year = forms.ModelChoiceField(queryset=FinancialYear.objects.all().distinct(), label='Financial Year', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'current year', 'name':'financial_year' }))
	date_of_leave = forms.DateTimeField(label='Date of Leave' ,widget=forms.DateInput(attrs={'class':'form-control', 'placeholder': 'yyyy-mm-dd', 'name':'date_of_leave'}))
	leave_from = forms.DateField(label='From' ,widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'name': 'leave_from', 'data-date-format':'yyyy-mm-dd'}))
	leave_to = forms.DateField(label='To', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'name':'leave_to', 'data-date-format':'yyyy-mm-dd'}))
	return_date = forms.DateField(label='Return Date', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'name':'return_date', 'data-date-format':'yyyy-mm-dd'}))
	no_of_days = forms.IntegerField(label='Number of Days', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Remaining Leave days', 'name':'no_of_days'}))
	line_supervisor = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supervisor', 'name': 'line_supervisor',}))
	line_supervisor_email = forms.EmailField(label='Supervisor Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Supervisor Email ', 'name': 'line_supervisor_email',}))
	leave_status = forms.ModelChoiceField(queryset=LeaveStatus.objects.all().distinct(), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Leave Status', 'name': 'leave_status',}))
	line_supervisor_remarks = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Remarks', 'name': 'line_supervisor_remarks',}))

	class Meta(object):
		model = LeaveApplication
		fields = '__all__'
		exclude = ['employee_name', 'department', 'email', 'financial_year', 'line_supervisor', 'line_supervisor_email']

class LeaveRegisterForm(forms.ModelForm):
	employee_name = forms.CharField(max_length=20, label='Employee Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'name': 'employee_name'}))
	department = forms.CharField(max_length=20, label='Department', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'department', 'name': 'department'}))
	email= forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email Address', 'name': 'email',}))
	leave_month=forms.ModelChoiceField(queryset=LeaveMonth.objects.all().distinct(), widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Leave Month', 'name':'leave_month'}))
	financial_year = forms.ModelChoiceField(queryset=FinancialYear.objects.all().distinct(), label='Financial Year', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'current year', 'name':'financial_year' }))
	line_supervisor = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supervisor', 'name': 'line_supervisor',}))
	line_supervisor_email = forms.EmailField(label='Supervisor Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Supervisor Email ', 'name': 'line_supervisor_email',}))

	class Meta(object):
		model = LeaveRegister
		fields = '__all__'
		