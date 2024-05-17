# views.py - 웹 페이지에서 보여질 내용을 담당하는 파일
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse # json 형식으로 데이터를 보내기 위해 사용
from django.views.decorators.csrf import csrf_exempt # csrf 보호 기능을 끄기 위해 사용
from .models import Vehicle # 모델 데이터 가져오기 위해 사용
from .forms import VehicleForm # VehicleForm 가져오기 위해 사용 - forms.py

# 차량 목록 페이지를 보여주는 함수
def vehicle_list(request):
    vehicles = Vehicle.objects.all() # 모든 차량 데이터를 가져옴
    return render(request, 'jinuk_add.html', {'vehicles': vehicles})
    # jinuk_add.html 파일에 가져온 데이터를 전달해 페이지를 보여줌


@csrf_exempt
# 새로운 차량 데이터 등록 함수
def create_vehicle(request):
    if request.method == 'POST': # 만약 요청이 post방식이라면 (등록 버튼을 눌렀다면)
        form = VehicleForm(request.POST, request.FILES) # 전달된 데이터로 폼을 만듦
        if form.is_valid(): # 폼 데이터가 올바른지 확인
            form.save() # 폼 데이터를 데이터베이스에 저장(crate)
            return JsonResponse({'message': 'Vehicle created successfully'}) # 성공 메시지 반환
        else:
            return JsonResponse({'errors': form.errors}, status=400)

@csrf_exempt
# 차량 데이터 삭제 함수
def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)  # 차량 ID에 해당하는 차량을 찾음 (못 찾으면 404 에러)
    vehicle.delete()
    return JsonResponse({'message': 'Vehicle deleted successfully'})

