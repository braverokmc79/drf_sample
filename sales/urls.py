from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

#app_name = "sales"  # 네임스페이스 지정
  
  
urlpatterns = [
    path('', views.api_root, name='api-root'),
    path("sales/monthly/", views.monthly_sales_summary),
    path("sales/category/", views.category_sales_summary),
    
    path('orders/daily/', views.daily_order_count),
    path('orders/product/', views.product_revenue_summary),
]

urlpatterns = format_suffix_patterns(urlpatterns)
