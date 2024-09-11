from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_active', 'is_verifeid')
    list_filter = ('email', 'is_superuser', 'is_active', 'is_verifeid')
    search_fields = ('email', )
    ordering = ('email', )
    fieldsets = (
        ("authentication", {
            "fields": (
                'email',
                'password',

            ),
            }),
            ("permissions", {
            "fields": (
                'is_staff',
                'is_active',
                'is_superuser',
                'is_verifeid',

            ),
            }),
            ("group permissions", {
            "fields": (
                'groups',
                'user_permissions',
            ),
            }),
            ("important dates", {
            "fields": (
                'last_login',
            ),
            }),
    )
    add_fieldsets = (
        (None,{
                "classes": ["wide"],
                "fields": ["email",
                           "password1", 
                           "password2", 
                           "is_staff", 
                           "is_active", 
                           "is_superuser",
                           "is_verifeid"],
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)

