from django.contrib import admin
from django.utils.html import format_html
from .models import Service, Order, Review

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', 'price', 'service_image')  # ← أضفنا الصورة
    search_fields = ('title', 'provider__username')
    list_filter = ('provider',)

    def service_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="80" style="object-fit: cover; border-radius: 8px;" />',
                obj.image.url
            )
        return "لا يوجد صورة"
    service_image.short_description = 'صورة الخدمة'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('service', 'client', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('client__username', 'service__title')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('order', 'rating')
    search_fields = ('order__service__title',)
