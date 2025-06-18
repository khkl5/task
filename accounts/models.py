from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLES = (
        ('client', 'عميل'),
        ('provider', 'مزود خدمة'),
        ('owner', 'مالك'),
    )

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        verbose_name='المستخدم'
    )
    role = models.CharField(
        max_length=10, 
        choices=ROLES, 
        verbose_name='الدور'
    )
    full_name = models.CharField(
        max_length=100, 
        verbose_name='الاسم الكامل'
    )

    def __str__(self):
        return f"{self.full_name} - {self.role}"

    class Meta:
        verbose_name = 'ملف المستخدم'
        verbose_name_plural = 'ملفات المستخدمين'
