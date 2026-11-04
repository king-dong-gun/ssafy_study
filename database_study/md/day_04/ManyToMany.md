### 1. 다대다 관계 (Many to many relationships)

> 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우이다.
>
- 양쪽 테이블 모두 여러 개의 레코드와 연결될 수 있다.
- N:M 관계라고 표현한다.
- Django에서는 `ManyToManyField`를 사용한다.

#### N:1의 문제점

> N:1 관계에서는 외래 키(Foreign Key)를 가진 레코드가 하나의 레코드만 참조할 수 있기 때문에 다대다 관계를 표현하는 데 한계가 있다.
>

예시: 환자와 의사의 관계

- 한 명의 환자는 여러 의사에게 진료받을 수 있다.
- 한 명의 의사는 여러 환자를 진료할 수 있다.
- 따라서 환자와 의사는 N:M 관계이다.

**N:1 관계에서 환자 생성**

```python
patient1 = Patient.objects.create(name="김동건", doctor=doctor1)
patient2 = Patient.objects.create(name="최예나", doctor=doctor2)
```

- `patient1`은 `doctor1`과 연결된다.
- `patient2`는 `doctor2`와 연결된다.
- `create()`는 새로운 레코드를 생성하여 데이터베이스에 저장한다.

**같은 이름으로 환자를 추가 생성하는 경우**

```python
patient3 = Patient.objects.create(name="김동건", doctor=doctor2)
```

기존 `patient1`을 수정하는 것이 아니라 새로운 환자 레코드가 생성된다.

![](https://velog.velcdn.com/images/king-dong-gun/post/80240595-7de9-46e4-b57c-cc69a8c3da8f/image.png)


- `patient1`과 `patient3`은 이름이 같지만 PK가 다르므로 서로 다른 레코드이다.
- 실제로 같은 환자라면 환자 정보가 중복 저장되는 문제가 발생한다.

#### 위 N:1 관계의 한계

- 새로운 레코드를 생성하면 동일한 환자 정보가 중복 저장될 수 있다.
- 기존 외래 키를 변경하면 이전 의사와의 관계가 사라진다.
- 하나의 외래 키 필드로는 여러 의사를 동시에 참조할 수 없다.

해결 방법

- 두 테이블 사이에 **중개 테이블(Intermediate Table)**을 생성한다.
- 중개 테이블에 환자 ID와 의사 ID를 저장해 다대다 관계를 표현한다.
- Django의 `ManyToManyField`를 사용하면 중개 테이블이 자동으로 생성된다.

---

### 2. 중개 모델

> 다대다(N:M) 관계에서 두 모델을 연결하고, 두 모델 사이의 관계 정보를 저장하는 모델이다.
>
- 두 모델의 **기본 키(PK)를 외래 키(FK)**로 참조한다.
- 두 모델 사이의 다대다 관계를 관리한다.
- Django에서는 `ManyToManyField`를 사용하면 중개 테이블이 자동으로 생성된다.
- 추가 정보가 필요한 경우 중개 모델을 직접 정의할 수 있다.

#### 중개 모델 구현

#### 1. 중개 모델 직접 정의

```python
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.doctor_id}: {self.patient_id}"
```

- `Doctor`: 의사 정보를 저장하는 모델
- `Patient`: 환자 정보를 저장하는 모델
- `Reservation`: 의사와 환자를 연결하는 중개 모델
- `ForeignKey`: 각 모델의 기본 키(PK)를 외래 키(FK)로 참조한다.

#### 2. ManyToManyField를 통한 중개 테이블 자동 생성

```python
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

- `doctors` : 환자와 연결된 여러 의사를 관리하는 필드
- `ManyToManyField` : N:M 관계를 설정하는 Django 필드
- `Doctor` : 관계를 맺을 대상 모델

| 구분 | 기존 방식 | 변경된 방식 |
| --- | --- | --- |
| 중개 모델 | `Reservation` 직접 정의 | 직접 정의하지 않음 |
| 중개 테이블 | `Reservation` 모델을 기반으로 생성 | Django가 자동 생성 |
| 관계 설정 | `ForeignKey` 2개 | `ManyToManyField` |
| 관계 추가 | `Reservation.objects.create()` | `patient.doctors.add()` |
| 관계 조회 | `Reservation` 조회 | `patient.doctors.all()` |

단순히 의사와 환자를 연결하는 경우에는 `ManyToManyField`를 사용하여 중개 테이블을 자동으로 생성할 수 있다.

하지만 증상, 진료 날짜, 예약 시간 등의 추가 정보를 저장하려면 중개 모델을 직접 정의하고 `through` 옵션으로 연결할 수 있다.

---

### 3. through 속성

> `through`는 다대다 관계에서 직접 정의한 중개 모델을 지정하는 옵션으로, 두 모델 간의 관계뿐만 아니라 추가 데이터도 함께 관리할 수 있다.
>

**중개 모델 정의**

```python
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```

- `through='Reservation'`: 자동 생성되는 중개 테이블 대신 직접 정의한 `Reservation` 모델을 사용한다.
- `doctor`: 연결된 의사를 참조하는 외래 키
- `patient`: 연결된 환자를 참조하는 외래 키
- `symptom`: 환자의 증상을 저장하는 필드
- `reserved_at`: 예약 레코드가 처음 생성될 때의 날짜와 시간을 자동 저장하는 필드

#### 의사와 환자 생성

```python
doctor1 = Doctor.objects.create(name="장원영")
patient1 = Patient.objects.create(name="김동건")
patient2 = Patient.objects.create(name="최예나")
```

- `Doctor.objects.create()`: 의사 레코드 생성
- `Patient.objects.create()`: 환자 레코드 생성
- 아직 의사와 환자 사이의 예약 관계는 생성되지 않는다.

**중개 모델을 통한 예약 생성**

```python
reservation1 = Reservation(
    doctor=doctor1,
    patient=patient1,
    symptom="headache"
)
reservation1.save()
```

- `Reservation()`: 예약 객체 생성
- `doctor=doctor1`: 연결할 의사 지정
- `patient=patient1`: 연결할 환자 지정
- `symptom="headache"`: 환자의 증상 저장
- `save()`: 예약 정보를 데이터베이스에 저장

**ManyToManyField를 통한 예약 생성**

```python
patient2.doctors.add(
    doctor1,
    through_defaults={"symptom": "flu"}
)
```

- `add()`: 환자와 의사의 관계 추가
- `through_defaults`: 중개 모델에 저장할 추가 데이터 전달
- `symptom="flu"`: 환자의 증상을 저장

#### 중개 테이블 저장 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/24c059b3-1901-4806-bcd2-c03083077c8c/image.png)


---

### 4. ManyToManyField 특징

> `ManyToManyField(to, **options)`는 Django에서 N:M(다대다) 관계를 설정할 때 사용하는 모델 필드이다.
>
- `to`: 관계를 맺을 대상 모델을 지정한다.
- `*options`: `through`, `related_name`, `symmetrical` 등의 추가 설정을 의미한다.
- 어느 모델에서든 관련된 객체에 접근할 수 있는 **양방향 관계**를 제공한다.
- `ManyToManyField.add()`는 이미 존재하는 관계를 다시 추가하지 않는다. 다만 직접 정의한 중개 모델에서는 별도의 제약 조건이 없다면 동일한 두 객체 사이의 관계 레코드를 여러 개 저장할 수 있다.
- 중개 테이블을 통해 두 모델 사이의 관계를 관리한다.

#### ManyToManyField의 대표 인자 3가지

**1. through**

> 직접 생성한 중개 모델을 지정하는 인자이다.
>
- 자동 생성되는 중개 테이블 대신 직접 정의한 중개 모델을 사용한다.
- 증상, 예약 시간 등의 추가 데이터를 저장할 때 활용한다.

```python
doctors = models.ManyToManyField(Doctor, through='Reservation')
```

**2. related_name**

> 역참조 시 사용할 이름을 변경하는 인자이다.
>
- 기본 역참조 이름 대신 개발자가 지정한 이름을 사용한다.
- 관련 객체를 조회할 때 코드의 가독성을 높일 수 있다.

```python
doctors = models.ManyToManyField(Doctor, related_name='patients')
```

```python
# 기본 역참조
doctor1.patient_set.all()

# related_name 설정 후
doctor1.patients.all()
```

**3. symmetrical**

> `symmetrical`은 자기 자신을 참조하는 다대다 관계에서 대칭 여부를 설정하며, 자기 참조 관계에서는 기본값이 `True`이다.
>
- `True`: A가 B와 관계를 맺으면 B도 A와 관계를 맺는다.
- `False`: A가 B와 관계를 맺어도 B가 A와 관계를 맺는 것은 아니다.
- 자기 자신을 참조하는 다대다 관계에서 사용한다.

```python
class Person(models.Model):
    friends = models.ManyToManyField('self', symmetrical=True)
```