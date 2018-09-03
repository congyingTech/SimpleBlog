from django.conf.urls import url
from . import views
from views import RSSFeed


app_name = 'own_blog'

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home_page'),
    url(r'^(?P<post_id>[0-9]+)/detail/$', views.detail, name='post_detail'),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^about_me/$', views.about_me, name='about_me'),
    url(r'feed/$', RSSFeed(), name="RSS"),
]
