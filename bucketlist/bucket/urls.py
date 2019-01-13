from django.urls import path
from . import views

app_name = "buckets"

urlpatterns = [
    #ex: /bucket/
    path('', views.index, name='index'),
    #ex: /bucket/3/
    path('<int:bucket_id>/', views.detail, name='detail'),
]
