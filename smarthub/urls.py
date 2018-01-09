from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('hubdata.urls')),
    url(r'^agent/', include('agent.urls')),
]
