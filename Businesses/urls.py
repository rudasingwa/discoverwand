from django.conf.urls import include, url
from django.contrib import admin

from .views import (
	homepage,
	search_result,
	detail,
	Create,
	)

urlpatterns = [
    url(r'^$', homepage),
    url(r'^search$', search_result),
    url(r'^(?P<id>\d+)$', detail, name='detail'),
    url(r'^create$', Create),

]
