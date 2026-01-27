from django.urls import path
from .views import upload_resume
from screener import views

urlpatterns = [
    path('', views.upload_resume, name='upload_resume'),
]
