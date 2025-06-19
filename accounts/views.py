from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages  # ✅ مهم للرسائل
from .models import UserProfile
from .forms import UserRegistrationForm

# ✅ الصفحة الرئيسية
def home(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def user_list(request):
    users = UserProfile.objects.all()
    context = {
        'users': users
    }
    return render(request, 'accounts/user_list.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # بعد التسجيل يذهب للـ login
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # ✅ نضيف رسالة ترحيب
            messages.success(request, f'مرحبًا، {user.userprofile.full_name}!')
            return redirect('home')  # يرجع إلى الصفحة الرئيسية
        else:
            error_message = 'اسم المستخدم أو كلمة المرور غير صحيحة'
            return render(request, 'accounts/login.html', {'error_message': error_message})

    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

# ✅ دوال التحقق الفوري
def validate_username(request):
    username = request.GET.get('username', None)
    exists = UserProfile.objects.filter(username=username).exists()
    return JsonResponse({'is_taken': exists})

def validate_email(request):
    email = request.GET.get('email', None)
    exists = UserProfile.objects.filter(email=email).exists()
    return JsonResponse({'is_taken': exists})

def validate_phone(request):
    phone = request.GET.get('phone_number', None)
    exists = UserProfile.objects.filter(phone_number=phone).exists()
    return JsonResponse({'is_taken': exists})
