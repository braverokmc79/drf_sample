from django.urls import path
from . import views

app_name = "sales"  # 네임스페이스 지정
  
  
urlpatterns = [
    path("monthly/", views.monthly_sales_summary),
    path("category/", views.category_sales_summary),
]


