from django.contrib import admin
from myapp.models import Register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']
    list_filter = ['email',]
    search_fields = ['first_name',]

admin.site.register(Register,RegisterAdmin)
