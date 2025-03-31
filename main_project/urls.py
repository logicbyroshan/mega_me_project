from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('personal/', include('personal.urls')),
    path('blogs/', include('blogs.urls')),
    path('hobby/', include('hobby.urls')),
    path('help/', include('help.urls')),
    path('manage/', include('memanage.urls')),
    path('work/', include('work.urls')),
    path('venture/', include('venture.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)