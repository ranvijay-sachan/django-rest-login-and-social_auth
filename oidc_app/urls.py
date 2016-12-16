from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.oidc_view, name='openind_connect'),
]