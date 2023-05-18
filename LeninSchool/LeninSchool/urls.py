from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import static

from LeninSchool import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls'))
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

