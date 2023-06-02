from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from usermanag.models import ExtendedUser, Home, Company, Bupass, Survey, CompanyData
from django.forms import ModelForm
from django.contrib.auth import get_user_model

from django.forms.models import model_to_dict
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404

class CompManageForm(ModelForm):

	class Meta(UserCreationForm.Meta):
		fields = ['id_company', 'company_description']
		model = Company


class CompCreateForm(ModelForm):
	company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	company_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta(UserCreationForm.Meta):
		fields = ['company_name', 'company_description']
		model = Company


class CompRedactForm(ModelForm):
	
	
	class Meta(UserCreationForm.Meta):
		fields = '__all__'
		model = CompanyData


class CompEditForm(ModelForm):
		company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'card-text'}))
		company_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

		class Meta(UserCreationForm.Meta):
			fields = ['company_name', 'company_description']
			model = Company


class HomeEditForm(ModelForm):
	address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta(UserCreationForm):
		fields = ['id_home', 'address']
		model = Home


class FormBupass(ModelForm):
	door_open = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox', 'id': 'door_open'}))
	date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'id': 'date'}))
	time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'id': 'time'}))
	reaction = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'reaction'}))

	class Meta(UserCreationForm.Meta):
		fields = '__all__'
		model = Bupass


class FormSurvey(ModelForm):
	resp_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'resp_name'}))
	resp_phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'resp_phone_number'}))
	comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'comment'}))

	class Meta(UserCreationForm):
		fields = ['resp_name', 'resp_phone_number', 'comment', 'id_form']
		model = Survey
		