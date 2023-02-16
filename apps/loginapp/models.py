from pyexpat import model
from django.db import models

# Create your models here.
import uuid
def UUIDrand():
    return str(uuid.uuid4())

class login(models.Model):
    FKcheck=models.CharField(max_length=36,default=UUIDrand)
    Rstate=models.CharField(max_length=42)
    #Raccesscode=models.CharField(max_length=43)

class udata(models.Model):
    UID=models.CharField('使用者編號', max_length=50)
    UAccess=models.CharField('資料請求', max_length=50)
    wpoint = models.IntegerField('智慧喜點數', null=True)
    uphone = models.IntegerField('聯絡電話', null=True)
    uaddress = models.CharField('寄取地址', max_length=100, null=True)
