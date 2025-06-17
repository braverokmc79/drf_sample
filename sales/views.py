# sales/views.py
from django.http import JsonResponse
from .models import SalesRecord
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth

def monthly_sales_summary(request):
    # ① 월별 총 매출 집계
    result = (SalesRecord.objects
                .annotate(month=TruncMonth("order_date")) # 날짜 필드는?
                .annotate(sales=F("price") * F("quantity"))  # 매출은 price * quantity
                .values("month")
                .annotate(total_sales=Sum("sales")) # 매출 합계?
                .order_by("month"))
    return JsonResponse(list(result), safe=False)



def category_sales_summary(request):
    # ② 카테고리별 총 매출 집계
    result = (SalesRecord.objects
                .annotate(sales=F("price") * F("quantity")) # 매출 계산?
                .values("category")
                .annotate(total_sales=Sum("sales"))) # 매출 합산?
    return JsonResponse(list(result), safe=False)

