from django.contrib import admin
from .models import Medico
# Register your models here.

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'idade')
    search_fields = ('nome', 'crm')
    list_filter = ('idade',)

admin.site.register(Medico, MedicoAdmin)