from django.contrib import admin
from .models import *
from nimble.common.models import Base

# Register your models here.

class BaseAdmin(admin.ModelAdmin):
    list_display = ['order', 'created', 'updated', 'is_active', 'is_deleted']
    list_filter  = ['is_active', 'is_deleted']
    search_fields = ['name', 'description']
    ordering = ['order','created']

class CommunityAdmin(BaseAdmin):
    list_display = ['name', 'channel'] + BaseAdmin.list_display
    list_display_links = ['name', 'channel']
    search_fields = ['name', 'channel']

class TagAdmin(BaseAdmin):
    list_display = ['name'] + BaseAdmin.list_display
    list_display_links = ['name']
    search_fields = ['name']

class VideoAdmin(BaseAdmin):
    list_display = ['title', 'description', 'views', 'category', 'is_private','playlist', 'channel', 'get_tags'] + BaseAdmin.list_display
    list_display_links = ['title', 'description', 'views', 'category', 'is_private','playlist', 'channel']
    search_fields = ['title', 'description', 'views', 'category', 'is_private','playlist__name', 'channel__name']

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

class PlaylistAdmin(BaseAdmin):
    list_display = ['name', 'description', 'channel'] + BaseAdmin.list_display
    list_display_links = ['name', 'description', 'channel']
    search_fields = ['name', 'description', 'channel']


class ChannelAdmin(BaseAdmin):
    list_display = ['name', 'description'] + BaseAdmin.list_display
    list_display_links = ['name', 'description']
    search_fields = ['name', 'description']


admin.site.register(Community, CommunityAdmin)   
admin.site.register(Tag, TagAdmin)    
admin.site.register(Video, VideoAdmin)    
admin.site.register(Playlist, PlaylistAdmin)    
admin.site.register(Channel, ChannelAdmin)