from django.contrib import admin
from .models import SignUp
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display=('id','name','email','contact_number', 'timestamp',)


admin.site.register(SignUp, SignUpAdmin)