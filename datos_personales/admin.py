from django.contrib import admin
from .models import Datos_personales


class Datos_personalesAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'apellido' , 'estado')



admin.site.register(Datos_personales, Datos_personalesAdmin)
