from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.deliver, name="deliver"),
    url(r'^(?P<id>[0-9]+)/$', views.add_delivery, name="add_delivery"),
]