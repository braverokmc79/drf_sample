import json
import os
import django

# Django 환경 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from sales.models import SalesRecord  # 앱 이름에 맞게 수정

# JSON 파일 열기
with open('sales_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 데이터 삽입
for record in data:
    SalesRecord.objects.create(
        order_id=record['order_id'],
        category=record['category'],
        price=record['price'],
        quantity=record['quantity'],
        order_date=record['order_date'],
    )

print("데이터 삽입 완료!")
