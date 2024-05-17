"""
URL configuration for django_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django_test 프로젝트 폴더 내의 urls.py에서 /vehicle/ URL엔드포인트를 jinuk_app
# 애플리케이션의 manage_vehicle 뷰 함수에 매핑하는 url 패턴
from django.urls import path # url경로를 정의하기 위해 사용 
from jinuk_app import views # views.py 파일에서 함수들을 가져옴
from django.conf import settings # setting information 불러오기
from django.conf.urls.static import static # static file 다루기 위해 사용

# Add this to your urlpatterns
urlpatterns = [
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    # vehicles/ 경로로 접속하면 vehicle_list function 실행(show vehicle list)
    path('vehicles/create/', views.create_vehicle, name='create_vehicle'),
    # vehicles/create 경로로 접속하면 create_vehicle function 실행(registed menwvehicle)
    path('vehicles/delete/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),
    # /vehicles/delete/ID/ 경로로 접속하면 delete_vehicl functino 실행(delete exsist vehicle data)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static file, media file 설정
