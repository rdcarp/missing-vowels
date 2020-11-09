from django.urls import path

from . import views


app_name = "missingvowels"


urlpatterns = [
    path('', views.CategoryIndexView.as_view(), name='index'),
    path('<int:pk>', views.CategoryDetailView.as_view(), name='category'),
    path('<int:pk>', views.CategoryDetailView.as_view(), name='answer'),
]
