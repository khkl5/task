from django.db import models
from marketplace.models import Order

class Transaction(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    provider_share = models.DecimalField(max_digits=8, decimal_places=2)
    platform_fee = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"معاملة لطلب {self.order.id}"

    class Meta:
        verbose_name = 'معاملة'
        verbose_name_plural = 'المعاملات'
