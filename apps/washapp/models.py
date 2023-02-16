from django.db import models
from django.utils import timezone

# Create your models here.
class order(models.Model):
    orderId = models.CharField('訂單編號', max_length=20, null=False)
    oUserid = models.CharField('使用者編號', max_length=10, null=False)
    oOrdertime = models.DateTimeField('成立時間', default=timezone.now)
    oFinish = models.DateTimeField('完成時間', null=True)
    def _str_(self):
        return self.orderId

class order_detail(models.Model):
    orderId = models.CharField('訂單編號', max_length=20, null=True)
    washmode=models.CharField('洗衣模式', max_length=20, null=True)
    spinmode=models.CharField('脫水模式', max_length=20, null=True)
    drymode=models.CharField('烘衣模式', max_length=20, null=True)
    foldmode=models.CharField('摺衣模式', max_length=20, null=True) 
    card=models.IntegerField('信用卡',null=False,default=0)
    oTotal = models.IntegerField('總金額', null=True)
    oPoint = models.IntegerField('總點數', null=True)
    C_amount = models.IntegerField('花費碳排總量', null=True)
    C_tax = models.IntegerField('碳稅', null=True)
    oTransport= models.CharField('運送方式', max_length=10, null=True)
    oSendcode = models.CharField('寄件條碼', max_length=30, null=True)
    oReceivecode = models.CharField('取件條碼', max_length=30, null=True)
    sId = models.CharField('店鋪標號', max_length=10, null=True)
    mState = models.CharField('洗衣狀態', max_length=10, null= True)
    oDelivery = models.CharField('外送員編號', max_length=10, blank=True)
    finaltime = models.CharField('預定完成時間', max_length=50, blank=True, null=True)
    wpoint = models.IntegerField('智慧喜點數', null=True)
    wash_num = models.IntegerField('送洗桶數', null=True)
    def _str_(self):
        return self.orderId

class price(models.Model):
    modename = models.CharField('模式名稱',max_length=20, null=False, blank=False)
    ttime = models.IntegerField('所需時間', null=False, blank=False)
    tprice = models.IntegerField('所需價格',null=False, blank=False)
    point = models.IntegerField('獲得點數',null=False, blank=False)
    carbon = models.IntegerField('碳排量', null=False, blank=False)
    def __str__(self):
        return self.modename


class store(models.Model):
    storeID = models.CharField('店鋪編號', max_length=10, null=False, blank=False)
    storeName = models.CharField('店鋪名稱', max_length=20, null=False, blank=False)
    storeAddress = models.CharField('店鋪地址', max_length=50, null=False, blank=False)
    def _str_(self):
        return self.storeID


