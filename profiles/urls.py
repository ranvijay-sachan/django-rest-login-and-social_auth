from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^(?P<backend>[^/]+)/$',
        view=views.LoginView.as_view(),
        name="authentication"
    ),
]
