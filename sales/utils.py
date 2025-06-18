# sales/utils.py
import os
import json
from django.conf import settings

def load_sales_data():
    """프로젝트 루트의 sales_data.json 파일을 읽어와 Python 객체로 반환"""
    path = os.path.join(settings.BASE_DIR, 'sales_data.json')
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    return data


def load_orders():
    path = os.path.join(settings.BASE_DIR, 'orders_data.json')
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    return data