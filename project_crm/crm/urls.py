from django.conf.urls import url,include
from django.contrib import admin
from  crm.views import home,depart,user
urlpatterns = [
    url(r'^index/$', home.index),
    url(r'^depart/list/$', depart.depart_list),
    url(r'^depart/add/$', depart.depart_add),
    url(r'^depart/edit/(\d+)/', depart.depart_edit),
    url(r'^depart/del/(\d+)/$', depart.depart_del),

    url(r'^user/list/$', user.user_list),
    url(r'^user/add/$', user.user_add),
    url(r'^user/edit/(\d+)/', user.user_edit),
    url(r'^user/del/(\d+)/', user.user_del),
]