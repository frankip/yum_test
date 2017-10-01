from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_details, name='details'),
    url(r'^add$', views.add_details, name='add-new'),
]