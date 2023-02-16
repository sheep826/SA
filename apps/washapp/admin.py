from django.contrib import admin
from washapp import models

# Register your models here.
admin.site.register(models.order)
admin.site.register(models.order_detail)
admin.site.register(models.price)
admin.site.register(models.store)