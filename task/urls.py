from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية (index)
    path('', include('marketplace.urls')),  # ← هذا السطر يربط index.html

    # روابط التطبيقات الأخرى
    path('accounts/', include('accounts.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('payments/', include('payments.urls')),
]

# إعدادات رفع الصور (media)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
