"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from apps.orders.views import OrderPlaceView, OrderCommitView, OrderPayView, CheckPayView, CommentView

app_name = 'orders'

urlpatterns = [
    re_path('^place/$', OrderPlaceView.as_view(), name='place'),
    re_path('^commit$', OrderCommitView.as_view(), name='commit'),
    re_path('^pay/$', OrderPayView.as_view(), name='pay'),
    re_path('^check/$', CheckPayView.as_view(), name="check"),
    re_path('^comment/(?P<order_id>.+)/$', CommentView.as_view(), name='comment'),
]
