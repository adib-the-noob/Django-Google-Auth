from django.contrib import admin
from .models import User

# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['email', 'is_active', 'is_admin']
#     list_filter = ['is_admin']
#     fieldsets = [
#         (None, {'fields': ['email', 'password1','password2']}),
#         ('Personal info', {'fields': ['username']}),
#         ('Permissions', {'fields': ['is_admin']}),
#     ]
#     add_fieldsets = [
#         (None, {
#             'classes': ['wide'],
#             'fields': ['email', 'password1', 'password2'],
#         }),
#     ]
#     search_fields = ['email']
#     ordering = ['email']
    # filter_horizontal = []

admin.site.register(User)