from django.http import JsonResponse
from .models import SalesRecord
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .utils import load_orders



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        "monthly_sales": "/api/sales/monthly/",
        "category_sales": "/api/sales/category/",
    })


@api_view(['GET'])
def monthly_sales_summary(request):
    # 월별 총 매출 집계
    result = (SalesRecord.objects
                .annotate(month=TruncMonth("order_date"))
                .annotate(sales=F("price") * F("quantity"))
                .values("month")
                .annotate(total_sales=Sum("sales"))
                .order_by("month"))
    return Response(result)


@api_view(['GET'])
def category_sales_summary(request):
    # 카테고리별 총 매출 집계
    result = (SalesRecord.objects
                .annotate(sales=F("price") * F("quantity"))
                .values("category")
                .annotate(total_sales=Sum("sales")))
    return Response(result)




def daily_order_count(request):
    """
    일별 주문 수 집계
    결과 형태: [{"date": "2025-06-15", "count": 2}, {"date": "2025-06-16", "count": 1}, …]
    """
    data = load_orders()
    counts = {}   # {"2025-06-15": 2, ...}
    for item in data:
        date = item["order_date"]
        if date in counts:
            counts[date] += 1
        else:
             counts[date] = 1
    response = []
    for date, cnt in sorted(counts.items()):
        response.append({"date": date, "count": cnt})
    return JsonResponse(response, safe=False)




def product_revenue_summary(request):
    """
    상품별 매출 합계 집계
    결과 형태: [{"product": "아메리카노", "revenue": 12000}, …]
    """
    data = load_orders()
    revenue = {}
    for item in data:
        prod = item["product"]
        rev  = item["price"] * item["quantity"]
        if prod in revenue:
            revenue[prod] += rev
        else:
            revenue[prod] = rev
    response = []
    for prod, total in sorted(revenue.items()):
        response.append({"product": prod, "revenue": total})
    return JsonResponse(response, safe=False)
