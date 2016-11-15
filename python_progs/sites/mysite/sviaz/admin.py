from django.contrib import admin
from .models import Kpd, Fpsu, Reserve, OS, Other, Phones, Platform, Servers, Switches, Routers

# Register your models here.

class KpdAdmin(admin.ModelAdmin):
    list_display = ('platform', 'service', 'throughput', 'tarif', 'last_mile', 'provider', 'contract_number_legal', 'b_z')
    list_filter = ('provider', 'contract_number_legal', 'last_mile', 'throughput', 'service', 'platform')
    ordering = ('platform',)
    search_fields = ('platform',)
admin.site.register(Kpd, KpdAdmin)