from django.urls import path
from .api import views

urlpatterns = [
    path('get', views.ImageListView.as_view(),name=None),
    path('create',views.ImageCreateView.as_view(),name=None),
]