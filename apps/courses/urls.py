from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^add$', views.add),
  url(r'^confirm_delete/(?P<id>\d+)$', views.confirm_delete),
  url(r'^delete/(?P<id>\d+)$', views.delete)

]
