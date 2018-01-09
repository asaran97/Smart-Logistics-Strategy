from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<lat>[0.0-9.9]+)/(?P<long>[0.0-9.9]+)/$', views.show_hub, name="hub_details"),
]