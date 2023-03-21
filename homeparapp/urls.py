from django.urls import path
from . import views
#Все сслыки на обработчики и их названия на Jil
urlpatterns = [
  path('home',views.index,name="home"),
  path("about",views.about,name="about"),
  path("price",views.price,name="price"),
  path("result",views.result,name="result"),
  path("support",views.support,name="support"),
  path('',views.singin,name="singin"),
  path('thx',views.thx,name="thx"),
]
