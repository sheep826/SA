from django.db import models
from django.utils import timezone

# Create your models here.
class order(models.Model):
    orderId = models.CharField('訂單編號', max_length=20, null=False)
    oUserid = models.CharField('使用者編號', max_length=10, null=False)
    oOrdertime = models.DateTimeField('成立時間', default=timezone.now)
    oFinish = models.DateTimeField('完成時間', auto_now=True)
    def _str_(self):
        return self.orderId

# class mode

class order_detail(models.Model):
    orderId = models.CharField('訂單編號', max_length=20, null=False)
    mName = models.CharField('模式名稱', max_length=10, null=False)
    oTotal = models.IntegerField('總金額', null=False)
    oPoint = models.IntegerField('總點數', null=False)
    C_amount = models.IntegerField('花費碳排總量', null=False)
    oTransport= models.CharField('運送方式', max_length=10, null=False)
    oSendcode = models.CharField('寄件條碼', max_length=30, null=False)
    oReceivecode = models.CharField('取件條碼', max_length=30, null=False)
    sId = models.CharField('店鋪標號', max_length=10, null=False)
    mState = models.CharField('洗衣狀態', max_length=10, null= False)
    oDelivery = models.CharField('外送員編號', max_length=10, blank=True)
    def _str_(self):
        return self.orderId

class price(models.Model):
    modename = models.CharField('模式名稱',max_length=20, null=False, blank=False)
    ttime = models.TimeField('所需時間', null=False, blank=False)
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