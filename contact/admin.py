from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','project','full_name','email', 'timestamp',)


admin.site.register(Contact, ContactAdmin)