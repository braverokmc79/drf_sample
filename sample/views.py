import os
import json
from django.http import JsonResponse
from django.conf import settings

def get_sample_data(request):
    file_path = os.path.join(settings.BASE_DIR, 'sample_data.json')
    try:
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse(data, safe=False)  # 리스트 형태 응답 가능하도록 safe=False
    except FileNotFoundError:
        return JsonResponse({'error': '파일을 찾을 수 없습니다.'}, status=404)
