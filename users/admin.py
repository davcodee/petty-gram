"""User admin clases"""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile
# Register your models here.
#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('pk','user', 'phone_number','website','picture')
    list_display_links = ('pk','user')
    list_editable = ('phone_number', 'website','picture')
    
    """Campos del dashboard para buscar"""
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    """Lista de elementos que vamos a filtrar"""
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )


    """
    Tupla en django que nos permite customizar nuestro dashboard
    de administración.
    """
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra Information', {
            'fields' : (
                ('website', 'phone_number'),
                ('biography')
            ),

        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    """Customización de nuestro dashboard """
    readonly_fields = ('created', 'modified',)


class ProfileInLine(admin.StackedInline ):
    """Profile admin inline admin  for users"""
    model = Profile
    can_delete  = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin  user admin to base user admin"""
    inlines = (ProfileInLine,) 
    listDisplays = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active ',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin )