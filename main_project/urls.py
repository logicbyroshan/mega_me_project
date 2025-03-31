from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_main.urls')),
    path('portfolio/', include('app_portfolio.urls')),
    path('personal/', include('app_personal.urls')),
    path('blogs/', include('app_blogs.urls')),
    path('hobby/', include('app_hobby.urls')),
    path('help/', include('app_help.urls')),
    path('manage/', include('app_memanage.urls')),
    path('work/', include('app_work.urls')),
    path('venture/', include('app_venture.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)