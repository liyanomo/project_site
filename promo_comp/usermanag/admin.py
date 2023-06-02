from django.contrib import admin
from .models import ExtendedUser, Home, Company, Bupass, Survey, CompanyData

# Register your models here.

admin.site.register(ExtendedUser)
admin.site.register(Home)
admin.site.register(Company)
admin.site.register(Bupass)
admin.site.register(Survey)
admin.site.register(CompanyData)