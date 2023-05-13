from django.contrib import admin
from .models import *
from nimble.common.models import Base

# Register your models here.

class BaseAdmin(admin.ModelAdmin):
    list_display = ['order', 'created', 'updated', 'is_active', 'is_deleted']
    list_filter  = ['is_active', 'is_deleted']
    search_fields = ['name', 'description']
    ordering = ['order','created']

class NFTOwnerAdmin(BaseAdmin):
    list_display = ['user','channel', 'quantity'] + BaseAdmin.list_display
    list_display_links = ['user','channel', 'quantity']
    search_fields = ['user','channel', 'quantity']


admin.site.register(NFTOwner, NFTOwnerAdmin)   
