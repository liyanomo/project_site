from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class ExtendedUser(AbstractUser):
	date_joinad = None
	Last_login = None
	groups = None
	user_permissions = None
	phone_number = models.CharField(max_length=50, verbose_name='Номер телефона')
	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app 'app_label'?"
		return True

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'



class Home(models.Model):
	id_home = models.AutoField(primary_key=True)
	address = models.CharField(max_length=400, verbose_name='Адрес', default='default title')

	class Meta:
		verbose_name = 'Дом'
		verbose_name_plural = 'Дома'

	def __str__(self):
		return self.address


class Company(models.Model):
	id_company = models.AutoField(primary_key=True)
	company_name = models.CharField(max_length=100, verbose_name='Название компании', unique=True)
	company_description = models.CharField(max_length=200, verbose_name='Описание компании')

	class Meta:
		verbose_name = 'Кaмпания'
		verbose_name_plural = 'Кaмпании'
	def __str__(self):
		return self.company_name


class Bupass(models.Model):
	id_bupass = models.AutoField(primary_key=True)
	door_open = models.BooleanField(verbose_name='Открыли дверь')
	date = models.DateField(verbose_name='Дата обхода')
	time = models.TimeField(verbose_name='Время обхода')
	reaction = models.CharField(max_length=300, verbose_name='Реакция')

	class Meta:
		verbose_name = 'Обход'
		verbose_name_plural = 'Обходы'

	def __str__(self):
		return str(self.date) + ' ' + str(self.time)


class Survey(models.Model):
	id_form = models.AutoField(primary_key=True)
	resp_name = models.CharField(max_length=70, verbose_name='Имя')
	resp_phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
	comment = models.CharField(max_length=400, null=True, verbose_name='Комментарий')

	class Meta:
		verbose_name = 'Протокол обходов'
		verbose_name_plural = 'Протоколы'

	def __str__(self):
		return self.resp_name


class CompanyData(models.Model):
	user_comp = models.ForeignKey('ExtendedUser', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
	home_comp = models.ForeignKey('Home', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Адрес')
	comp_num = models.ForeignKey('Company', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Компания')
	bupass_comp = models.ForeignKey('Bupass',blank=True, null=True, on_delete=models.CASCADE, verbose_name='Обход')
	bupass_form_comp = models.ForeignKey('Survey', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Форма обхода')