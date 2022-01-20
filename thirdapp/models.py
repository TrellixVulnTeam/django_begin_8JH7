from django.db import models

# Create your models here.


class Shop(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    shop_name = models.CharField(max_length=100, null=True)
    shop_desc = models.CharField(max_length=100, null=True)
    rest_date = models.CharField(max_length=100, null=True)
    parking_info = models.CharField(max_length=100, null=True)
    img_path = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'shop'
        app_label = 'thirdapp'
        managed = False


class JejuOlle(models.Model):
    id = models.IntegerField(primary_key=True)
    acourse = models.CharField(max_length=100, null=True, db_column='course')
    # course = models.CharField(max_length=100, null=True)
    course_name = models.CharField(max_length=100, null=True)
    distance = models.FloatField(default='0')
    time_info = models.CharField(max_length=100, null=True)
    start_end_info = models.CharField(max_length=255, null=True)
    cre_date = models.DateField(
        auto_now=False, auto_now_add=False)

    class Meta:
        db_table = 'jeju_olle'
        app_label = 'thirdapp'
        managed = False


class Owner(models.Model):
    name = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'owner'
        managed = False


class Animal(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'animal'
        managed = False


class Playground(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=20, null=True)
    animals = models.ManyToManyField(Animal, null=True)

    class Meta:
        db_table = 'playground'
        managed = False


class Warranty(models.Model):
    model_nm = models.CharField(max_length=50, null=True)
    period = models.IntegerField(null=True)

    class Meta:
        db_table = 'warranty'
        managed = False


class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField(null=True)
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True)
    warranty = models.OneToOneField(
        Warranty, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'product'
        managed = False


class Dept(models.Model):
    deptno = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=14, null=True)
    loc = models.CharField(max_length=13, null=True)

    class Meta:
        db_table = 'dept'
        managed = False


class Emp(models.Model):
    empno = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=10, null=True)
    job = models.CharField(max_length=9, null=True)
    mgr = models.IntegerField(null=True)
    hiredate = models.DateTimeField(null=True)
    sal = models.IntegerField(null=True)
    comm = models.IntegerField(null=True)
    # 정리하기 디비컬럼명은 장고에서 디폴트로 dept_id로 생성해놓았지만 실제 컬럼명은 deptno이기 때문에 지정해줌.
    dept = models.ForeignKey(
        Dept, on_delete=models.SET_NULL, null=True, db_column='deptno')

    class Meta:
        db_table = 'emp'
        managed = False
