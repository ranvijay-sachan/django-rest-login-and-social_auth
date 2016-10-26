from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^facebook/$', views.fb_view, name='facebook'),
    url(r'^employees/$', views.SnippetList.as_view()),
    url(r'^employees/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)