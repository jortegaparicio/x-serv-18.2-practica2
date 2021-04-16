from django.urls import path

from . import views

urlpatterns = [
    path('<str:surl>', views.get_content)
]
