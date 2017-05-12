from django.conf.urls import url
from . import views # import views from blog application

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # only an empty string will match
]

