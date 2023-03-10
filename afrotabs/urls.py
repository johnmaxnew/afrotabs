from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("home.urls")),
    path("afro23/", admin.site.urls),
    path("tabs/", include("tabs.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('user/', include('accounts.urls')),
]

handler404 = 'tabs.views.error_404'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
