from django.contrib import admin
from .models import Staff, Carrers, Postulation
# Register your models here.



class StaffAdmin(admin.ModelAdmin):
    list_display=('id','name','departement', 'title',)


class CarrersAdmin(admin.ModelAdmin):
    list_display=('id','name','description', 'timestamp',)


class PostulationAdmin(admin.ModelAdmin):
    list_display=('id','full_name','email', 'timestamp',)


admin.site.register(Staff, StaffAdmin)

admin.site.register(Carrers, CarrersAdmin)
admin.site.register(Postulation, PostulationAdmin)