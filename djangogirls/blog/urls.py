from django.urls import path

from myapp.admin import admin_site

urlpatterns = [
    path("myadmin/", admin_site.urls),
]
