from django.shortcuts import render
from comp.forms import CompManageForm, CompCreateForm, CompEditForm, HomeEditForm, CompRedactForm, FormBupass, FormSurvey
from usermanag.models import Home, Company, Bupass, Survey, CompanyData

# Create your views here.

def mycomp(request):
	if request.method == 'GET':
		comp_dat_id = CompanyData.objects.filter(user_comp__id=request.user.id)
		uniq_id = []
		for n in comp_dat_id:
			if n.comp_num_id not in uniq_id:
				uniq_id.append(n.comp_num_id)

		uniq_id.sort()
		comp_dat = Company.objects.filter(id_company__in=uniq_id)
		return render(request, 'mycomp.html', {'comp': comp_dat})

	elif request.method == 'POST':
		form = CompManageForm(request.POST)
		if form.is_valid():
			comp = form.save()
			return render(request, 'mycomp.html')
		else:
			data = form.errors
			return render(request, 'error.html', {'data': data})


def createcomp(request):
	if request.method == 'POST':
		form_com_create = CompCreateForm(request.POST)
		create_comp_data = CompanyData.objects.create()
		if form_com_create.is_valid():
			form_com_create = form_com_create.save()
			create_comp_data.comp_num = form_com_create
			create_comp_data.user_comp = request.user
			create_comp_data.save()
		else:
			data =form_com_create.errors
			return render(request, 'error.html', {'data': data})

	form_com_create = CompCreateForm()
	data_com = {'form_com_create': form_com_create}
	
	return render(request, 'createcomp.html', data_com)


def comps(request):
	comp_data = Company.objects.all()
	

	return render(request, 'comps.html', {'data': comp_data})


def showcomp(request, id_company):
	comp_data = Company.objects.filter(id_company=id_company)
	all_data = CompanyData.objects.filter(comp_num_id=id_company)
	return render(request, 'showcomp.html', {'data': comp_data, 'all_data': all_data})


def editcomp(request, id_company):
	comp_data = Company.objects.get(id_company=id_company)
	data = CompanyData.objects.filter(comp_num_id=id_company)

	if request.method == 'POST':
		form_comp = CompEditForm(request.POST, instance=comp_data)

		if form_comp.is_valid():
			form_comp.save()

		else:
			print(form_comp.errors)
			print('Ошибка')

	forms_comp = CompEditForm()
	forms_comp.fields['company_name'].initial = comp_data.company_name
	forms_comp.fields['company_description'].initial = comp_data.company_description
	
	return render(request, 'editcomp.html', {'data': data, 'forms_comp': forms_comp, 'comp_data': comp_data})


def homeedit(request, id_company):
	form = HomeEditForm()
	comp = Home.objects.all()
	if request.method == 'POST':
		form = HomeEditForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			print(form.errors)
			print('ERROR')
	comp = Home.objects.all()
	return render(request, 'homeedit.html', {'form': form, 'comp': comp})



def bupassedit(request, id_company):
	form = FormBupass()
	bupass = Bupass.objects.all()
	if request.method == 'POST':
		form = FormBupass(request.POST)
		if form.is_valid():
			form.save()
		else:
			print(form.errors)
			print('ERROR')
	bupass = Bupass.objects.all()
	return render(request, 'bupassedit.html', {'form': form, 'bupass': bupass})


def formbupass(request, id_company):
	form = FormSurvey()
	bupass_form = Survey.objects.all()

	if request.method == 'POST':
		form = FormSurvey(request.POST)

		if form.is_valid():
			form.save()

		else:
			print(form.errors)
			print('ERROR')

	bupass_form = Survey.objects.all()
	return render(request, 'formbupass.html', {'form': form, 'bupass_form': bupass_form})


def showbupass(request, id_bupass):
	bupass_data = Bupass.objects.get(id_bupass=id_bupass)
	return render(request, 'showbupass.html', {'bupass_data': bupass_data})

def showhome(request, id_home):
	home_data = Home.objects.get(id_home=id_home)
	return render(request, 'showhome.html', {'home_data': home_data})

def showsurveyform(request, id_form):
	survey_form_data = Survey.objects.get(id_form=id_form)
	return render(request, 'showsurveyform.html', {'survey_form_data': survey_form_data})

