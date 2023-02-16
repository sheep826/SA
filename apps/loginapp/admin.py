from django.contrib import admin

# Register your models here.
from loginapp import models
admin.site.register(models.login)