from django.contrib import admin
from .models import jjcuser

#class NewAppAdmin(admin.ModelAdmin):
 #   list_display = ('name','email','subject','messg')
  #  list_display_links = ('name')
   # search_fields=('name','email')
    #list_per_page = 20

admin.site.register(jjcuser)
# Register your models here.
