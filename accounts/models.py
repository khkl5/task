from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

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

    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='اسم المستخدم'
    )

    phone_number = models.CharField(
        max_length=10,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^05\d{8}$',
                message='رقم الجوال يجب أن يبدأ بـ 05 ويتكون من 10 أرقام'
            )
        ],
        verbose_name='رقم الجوال'
    )

    email = models.EmailField(
        unique=True,
        verbose_name='البريد الإلكتروني'
    )

    full_name = models.CharField(
        max_length=100,
        verbose_name='الاسم الكامل'
    )

    role = models.CharField(
        max_length=10,
        choices=ROLES,
        verbose_name='الدور'
    )

    def __str__(self):
        return f"{self.full_name} - {self.role}"

    class Meta:
        verbose_name = 'ملف المستخدم'
        verbose_name_plural = 'ملفات المستخدمين'
