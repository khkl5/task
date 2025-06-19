from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        max_length=50,
        required=True,
        label='اسم المستخدم',
        widget=forms.TextInput(attrs={'placeholder': 'اسم المستخدم'})
    )

    phone_number = forms.CharField(
        max_length=10,
        required=True,
        label='رقم الجوال',
        validators=[
            RegexValidator(
                regex=r'^05\d{8}$',
                message='رقم الجوال يجب أن يبدأ بـ 05 ويتكون من 10 أرقام'
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': '05xxxxxxxx'})
    )

    email = forms.EmailField(
        required=True,
        label='البريد الإلكتروني',
        widget=forms.EmailInput(attrs={'placeholder': 'example@email.com'})
    )

    password = forms.CharField(
        label='كلمة المرور',
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••••••'}),
        help_text='يجب أن تحتوي كلمة المرور على 8 أحرف على الأقل.'
    )

    confirm_password = forms.CharField(
        label='تأكيد كلمة المرور',
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••••••'}),
        required=True
    )

    full_name = forms.CharField(
        max_length=100,
        required=True,
        label='الاسم الكامل',
        widget=forms.TextInput(attrs={'placeholder': 'الاسم الكامل'})
    )

    role = forms.ChoiceField(
        choices=UserProfile.ROLES,
        required=True,
        label='الدور'
    )

    class Meta:
        model = UserProfile
        fields = ['username', 'phone_number', 'email', 'password', 'confirm_password', 'full_name', 'role']

    def clean_username(self):
        username = self.cleaned_data['username']
        if UserProfile.objects.filter(username=username).exists():
            raise forms.ValidationError('اسم المستخدم مستخدم من قبل.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserProfile.objects.filter(email=email).exists():
            raise forms.ValidationError('البريد الإلكتروني مستخدم من قبل.')
        return email

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if UserProfile.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError('رقم الجوال مستخدم من قبل.')
        return phone

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('كلمة المرور يجب أن تكون 8 أحرف على الأقل.')
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'كلمة المرور وتأكيدها غير متطابقين.')

    def save(self, commit=True):
        # إنشاء مستخدم User
        user = User.objects.create(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=make_password(self.cleaned_data['password'])  # تشفير كلمة المرور
        )

        # إنشاء UserProfile
        profile = super().save(commit=False)
        profile.user = user
        if commit:
            profile.save()

        return profile
