from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .models import User, UserAction


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'account_type', 'is_active', 'date_joined')
        list_filter = ('type', 'is_active', 'is_superuser')


class UserAdminWithExtraFields(ImportExportModelAdmin, UserAdmin):

    def __init__(self, *args, **kwargs):
        super(UserAdminWithExtraFields, self).__init__(*args, **kwargs)

        abstract_fields = [field.name for field in AbstractUser._meta.fields]
        user_fields = [field.name for field in self.model._meta.fields]

        self.add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('email', 'username', 'password1', 'password2')}),
        )

        self.fieldsets += (
            (_('Extra fields'), {
                'fields': [
                    f for f in user_fields if (
                        f not in abstract_fields and
                        f != self.model._meta.pk.name
                    )
                ],
            }),
        )

class UserActionAdmin(admin.ModelAdmin):
    list_display = ['user','action_type','updated']
    list_filter = ['updated']
    search_fields = ['user','action_type','updated']

admin.site.register(UserAction, UserActionAdmin)
UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'account_type', 'is_active', 'date_joined')
UserAdmin.list_filter = ('account_type', 'is_active', 'is_superuser')
UserAdmin.resource_class = UserResource
admin.site.register(User, UserAdminWithExtraFields)