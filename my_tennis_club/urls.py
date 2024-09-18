from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path('', lambda request: redirect('courts/', permanent=False)),
    path("members/", include("members.urls")),
    path("courts/", include("courts.urls")),
    path("admin/", admin.site.urls),
]
