
from django.contrib import admin
from django.urls import path, include

# for image upload
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # accessing base app urls
    path('',include('base.urls')),
    # accessing api urls
    path('api/',include('base.api.urls'))
]

# for image upload
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

