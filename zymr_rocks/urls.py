from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.authtoken import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/login/', include('profiles.urls')),
    url(r'^api/v1/sample/', include('sample.urls')),
]

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]