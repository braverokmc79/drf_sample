from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sample/', include('sample.urls')),     # 루트 경로는 sample 앱 전용
    path('api/sales/', include('sales.urls')),  # /sales/ 로 접속하는 경로
]