from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^user/$', views.UserView.as_view(), name='homepage'),
]
