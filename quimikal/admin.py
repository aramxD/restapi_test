from django.contrib import admin
from .models import Quimikal
# Register your models here.

class QuimikalAdmin(admin.ModelAdmin):
    list_display=('id','name','email','contact_number', 'timestamp',)


admin.site.register(Quimikal, QuimikalAdmin)