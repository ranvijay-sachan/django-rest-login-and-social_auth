from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^facebook/$', views.fb_view, name='facebook'),

]