from django.urls import path

from blog.admin import admin_site

urlpatterns = [
    path("myadmin/", admin_site.urls),
]
