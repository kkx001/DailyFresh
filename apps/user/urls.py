
from django.urls import re_path
from apps.user.views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserOrderView, AddressView

app_name = 'user'

urlpatterns = [
    re_path('^register/$', RegisterView.as_view(), name='register'),
    re_path('^active/(?P<token>.*)/$', ActiveView.as_view(), name='active'),
    re_path('^login/$', LoginView.as_view(), name='login'),
    re_path('^logout/$', LogoutView.as_view(), name='logout'),

    re_path('^$', UserInfoView.as_view(), name='user'),#用户中心
    re_path('^order/(?P<page>\d+)/$', UserOrderView.as_view(), name='order'), #订单页面
    re_path('^address/$', AddressView.as_view(), name='address'), #地址页面
]
