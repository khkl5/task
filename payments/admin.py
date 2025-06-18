from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('order', 'total_amount', 'provider_share', 'platform_fee', 'created_at')
    search_fields = ('order__id',)
    list_filter = ('created_at',)
