from django.urls import path
from . import views


urlpatterns = [
    path("", views.courts, name="courts"),
    path("reserve/<int:id>", views.reserve, name="reserve"),
    path("unreserve/<int:id>/", views.unreserve, name="unreserve"),
]
