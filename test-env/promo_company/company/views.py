from django.shortcuts import render
from django.http import HttpResponse
from .models import Company, House
from .forms import OrderForm
# Create your views here.

def my_company(request):

    if request.method == "GET":
        camp_dat_id = CampaignData.objects.filter(user_camp_id = request.user.id)
        uniq_id = []
        for n in camp_dat_id:
            if n.camp_num_id not in uniq_id:
                uniq_id.append(n.camp_num_id)
        uniq_id.sort()
        camp_dat = Campaing.objects.filter(id_campaign__in=uniq_id)

        return render(request, "my_company.html", {"company": camp_dat})
    elif request.method == "POST":
        form = CampManageForm(request.POST)
        if form.is_valid():
            camp = form.save()
            return render(request, "my_company.html")
        else:
            data = form.errors
            return render(request, "no((.html", {'data' : data})

def create_company(request):
    if request.method == "POST":
        form_cam_create = CampCreateForm(request.POST)
        create_camp_data = CampaignData.objects.create()
        if form_cam_create.is_valid():
            form_cam_create = form_cam_create.save()
            create_camp_data.camp_num = form_cam_create
            create_camp_data.user_camp = request.user
            create_camp_data.save()
        else:
            data = form_cam_create.errors
            return render(request, "no((.html", {'data' : data})
    form_cam_create = CampCreateForm()
    data_cam = {'form_cam_create': form_cam_create}
    return render(request, "my_company.html", data_cam)

def edit_company(request, id_campaign):
    camp_data = Campaing.objects.get(id_campaign=id_campaign)
    data = CampaignData.objects.filter(camp_num_id = id_campaign)
    if request.method == "POST":
        form_camp = CampEditForm(request.POST, instance=camp_data)
        if form_camp.is_valid():
            form_camp.save()
        else:
            print(form_camp.errors)
            print('EROR')
        
    
    form_camp = CampEditForm()
    form_camp.fields['campaign_name'].initial = camp_data.campaign_name
    form_camp.fields['campaign_description'].initial = camp_data.campaign_description

    return render(request, "edit_company.html", {"data" : data, "form_camp" : form_camp, "camp_data" : camp_data})

def edit_home(request, id_campaign):
    form = CampRedactForm()
    camp = Campaing.objects.get(id_campaign=id_campaign)

    if request.method == "POST":
        form = CampRedactForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_camp = request.user
            obj.camp_num = camp
            obj.save()
            print (form)
        else:
            print(form.errors)
            print('EROR')

    return render(request, "edit_home.html", {"form" : form})

def poll_info(request, id_poll):
    poll_data = Poll.objects.get(id_poll=id_poll)
    return render(request, "poll_info.html", {"poll_data" : poll_data} )

def poll_form(request, id_form):
    poll_form_data = PoolForm.objects.get(id_form=id_form)
    return render(request, "poll_form.html", {"poll_form_data" : poll_form_data})

def poll (request, id_campaign):
    form = FormPollForm()
    poll_form = PoolForm.objects.all()

    if request.method == "POST":
        form = FormPollForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            print('EROR')

    poll_form = PoolForm.objects.all()
    return render(request, "poll.html", {"form": form, "poll_form": poll_form})

def main (response):
	data = Company.objects.all()
	return render (response, "main/main.html",{'Кампании':data})

def user (response):
	return render (response, "main/user.html")
	data1 = {'theme': 'Python','name': 'Project 1', 'descr' : 'all about python'}
def product (response, comp_id):
	data = Company.objects.get (id_company = comp_id)
	return render (response, "main/product.html", {'data':data})
def contact (request):
	if request.method == 'POST':
		form = OrderForm (request.POST)
		if form.is_valid ():
			form.sasve ()
	form = OrderForm()
	data = {'form' : form}
	return render (request, "main/contact.html", data)
def company (response):
	data = Company.objects.all()
	return render (response, "main/company.html",{'data':data})
	