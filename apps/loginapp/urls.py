from unicodedata import name
from django.urls import path, include
from loginapp import views

urlpatterns = [
    path("",views.index, name='index'),
    path("login_line",views.login_view),
    path("logout/", views.logout, name="logout"),
    path("api_check/", views.api_check),
    path("login_session/", views.login_session),
    path("register/", views.register),
    path("phone/", views.phone, name='phone'),
    path("SMS/", views.SMS, name='SMS'),
    path('SMScode/', views.SMScode),
]