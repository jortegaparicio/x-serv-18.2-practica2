from django.urls import path

from . import views

urlpatterns = {
    path('', views.form_act),
    path('<str:surl>', views.get_content)
}
