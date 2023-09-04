from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('health_check.urls')),
    path('admin/', admin.site.urls),
    path('health/', include('health_check.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
settings.DEBUG = False