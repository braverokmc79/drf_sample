from django.urls import path
from . import views

app_name = "sample"  # 네임스페이스 지정
  
  
urlpatterns = [
    path('', views.get_sample_data),    
]


