from django.urls import path

from . import views

urlpatterns = [
    path("deauth/", views.DeAuthUser.as_view(), name="deauth")
]