from django.db import models
from django.conf import settings

class Service(models.Model):
    provider = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        verbose_name='مزود الخدمة'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='عنوان الخدمة'
    )
    description = models.TextField(
        verbose_name='وصف الخدمة'
    )
    price = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
        verbose_name='السعر'
    )
    image = models.ImageField(
        upload_to='service_images/',
        verbose_name='صورة الخدمة',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'خدمة'
        verbose_name_plural = 'الخدمات'


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'قيد التنفيذ'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغي'),
    )

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='orders',
        verbose_name='العميل'
    )
    service = models.ForeignKey(
        Service, 
        on_delete=models.CASCADE,
        verbose_name='الخدمة المطلوبة'
    )
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='pending',
        verbose_name='الحالة'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ الإنشاء'
    )

    def __str__(self):
        return f"طلب {self.service} من {self.client}"

    class Meta:
        verbose_name = 'طلب'
        verbose_name_plural = 'الطلبات'


class Review(models.Model):
    order = models.OneToOneField(
        Order, 
        on_delete=models.CASCADE,
        verbose_name='الطلب'
    )
    rating = models.PositiveIntegerField(
        verbose_name='التقييم'
    )
    comment = models.TextField(
        verbose_name='التعليق'
    )

    def __str__(self):
        return f"تقييم لـ {self.order.service}"

    class Meta:
        verbose_name = 'تقييم'
        verbose_name_plural = 'التقييمات'
