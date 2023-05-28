from django.contrib import admin
from .models import Company, House

# Register your models here.

admin.site.register (Company)
admin.site.register (House)
admin.site.register(ExtendedUser)
admin.site.register(Poll)
admin.site.register(PoolForm)
admin.site.register(CampaignData)
