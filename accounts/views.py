from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile

def user_list(request):
    users = UserProfile.objects.all()
    context = {
        'users': users
    }
    return render(request, 'accounts/user_list.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        full_name = request.POST.get('full_name')
        role = request.POST.get('role')

        # إنشاء المستخدم الأساسي
        user = User.objects.create_user(username=username, password=password)

        # إنشاء ملف المستخدم
        profile = UserProfile.objects.create(
            user=user,
            full_name=full_name,
            role=role
        )

        return redirect('user_list')  # رجوع لقائمة المستخدمين أو أي صفحة أخرى

    return render(request, 'accounts/register.html')
