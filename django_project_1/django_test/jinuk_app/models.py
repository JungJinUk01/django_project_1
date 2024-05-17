from django.db import models

# models:
# 애플리케이션의 데이터와 정보를 표현한다. 여기 정의된 내용을 통해 데이터베이스에 데이터가 저장되는데 장고에서는 모델에 정의된 1개의 클래스가 데이터베이스의 1개의 테이블이 된다.
# 여기는 데이터를 정의하고 데이터베이스에 저장될 테이블의 형태를 나타낼 뿐 view나 controller의 정보를 알고 있으면 안된다.
# view는 데이터 등을 입력하거나 보여주는 역할, controller는 이 과정을 수행해주는 역할
# model은 단지 데이터만을 가지고 있어야하며 데이터를 보여주거나 입력하는 view, controller의 기능이 이곳에 명시되어서는 안된다.

# Create your models here.
from django.db import models

class Vehicle(models.Model):
    vehicle_num0 = models.CharField(max_length=10)
    vehicle_num = models.CharField(max_length=10)
    driver = models.CharField(max_length=50, blank=True, null=True)
    maker = models.CharField(max_length=50, blank=True, null=True)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    passenger_num = models.PositiveIntegerField(blank=True, null=True)
    use = models.CharField(max_length=10, default='사용')  # 기본값을 '사용'으로 설정
    type = models.CharField(max_length=50, blank=True, null=True)
    model_year = models.PositiveIntegerField(blank=True, null=True)
    vehicle_id = models.CharField(max_length=50, unique=True)
    release_date = models.DateField(blank=True, null=True)
    check_date = models.DateField(blank=True, null=True)
    motor_type = models.CharField(max_length=50, blank=True, null=True)  
    rated_output = models.CharField(max_length=50, blank=True, null=True) 
    vehicle_registration = models.FileField(upload_to='vehicles/', blank=True, null=True )

    def __str__(self):
        return f"{self.vehicle_num0}-{self.vehicle_num}"

    # models.py는 django에서 데이터베이스 스키마를 정의하는 역할을 한다. 여기서 정의한 클래스는 데이터베이스 테이블과
    # 직접적으로 연결되며, 클래스의 속성은 테이블의 컬럼에 해당한다. 이러한 ORM모델(?)을 사용하여 데이터베이스에 데이터를 
    # 저장하고, 조회, 수정, 삭제 등의 작업을 객체 지향적인 방법으로 수행할 수 있다.

    # 클래스 = 테이블: 각 모델 클래스는 데이터베이스의 하나의 테이블에 해당한다.
    # 속성 = 컬럼: 클래스 내부에 정의된 속성들은 데이터베이스 테이블의 컬럼들에 해당한다.
    # 객체 = 행: 데이터베이스에 데이터를 추가할 때, 해당 모델의 인스턴스를 생성하고, 이 인스턴스를 저장함으로써 데이터베이스
    #           테이블에 새로운 행이 추가된다.

    # 웹에서 데이터를 추가하면 데이터베이스 테이블에 새로운 행으로 저장되고 개발한 애플리케이션의 인터페이스에서 이 데이터 조회가 가능하다.
