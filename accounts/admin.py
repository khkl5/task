from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('display_full_name', 'display_role', 'display_user')
    search_fields = ('full_name', 'role', 'user__username')
    list_filter = ('role',)

    def display_full_name(self, obj):
        return obj.full_name
    display_full_name.short_description = 'الاسم الكامل'

    def display_role(self, obj):
        return dict(obj.ROLES).get(obj.role, obj.role)
    display_role.short_description = 'الدور'

    def display_user(self, obj):
        return obj.user.username
    display_user.short_description = 'المستخدم'
