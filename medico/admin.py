from django.contrib import admin
from .models import Medico
# Register your models here.

class MedicoAdmin(admin.ModelAdmin):
    ...

admin.site.register(Medico, MedicoAdmin)