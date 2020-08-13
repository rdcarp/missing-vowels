from django.urls import path

from . import views


urlpatterns = [
    path('', views.CategoryIndexView.as_view(), name='index'),
]
