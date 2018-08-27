from django.conf.urls import url
from . import views


app_name = 'own_blog'

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home_page'),
    url(r'^(?P<post_id>[0-9]+)/detail/$', views.detail, name='post_detail'),
    url(r'^archives/$', views.archives, name='archives')
]
