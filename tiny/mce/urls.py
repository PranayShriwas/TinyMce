# your_app_name/urls.py
from django.urls import path
from .views import your_model_detail

urlpatterns = [
    path('/<int:pk>/', your_model_detail, name='your_model_detail'),
]
