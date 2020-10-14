
from django.contrib import admin
from django.urls import path, re_path
from apps.cart.views import CartAddView, CartInfoView, CartUpdateView, CartDeleteView

app_name = 'cart'

urlpatterns = [
    re_path('^add/$', CartAddView.as_view(), name='add'), # 购物车记录添加
    path('', CartInfoView.as_view(), name='show'), # 购物车页面显示
    re_path('^update/$', CartUpdateView.as_view(), name='update'),# 购物车记录更新
    re_path('^delete/$', CartDeleteView.as_view(), name='delete'),# 购物车记录删除
]
