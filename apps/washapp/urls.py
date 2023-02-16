from unicodedata import name
from django.urls import path, include, re_path
from washapp import views


urlpatterns = [
    # path("", views.index),
    path("dinosaur/", views.dinosaur, name='dinosaur'),
    path("wash1/", views.wash1, name='wash1'),
    path("wash2/", views.wash2, name='wash2'),
    path("order/", views.orderlist, name='order'),
    path('order_detail)', views.order_detail, name='orderdetail'),
    path("QA/", views.QA, name='QA'),
    path("contact/", views.contact, name='contact'),
    path("order_detail/", views.orderdetail, name='order_detail'),
    path("QRcode/", views.QRcode, name='QRcode'),
    path("transmode1/", views.transmode1, name='transmode1'),
    path("transmode1/transmode2/", views.transmode2, name='transmode2'),
    path('checkorder/', views.checkorder, name='checkorder'),
    path('finishorder/', views.finishorder),
    path('finish/', views.finish, name='finish'),
    path("finish/finishorder/", views.orderlist, name='finishorder'),
]