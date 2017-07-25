
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from landing.views import CreateView
from . import views


urlpatterns = [
    url(r'^stocks-test/$', CreateView.as_view(), name="create"),
    url(
        r'^stocks/(?P<pk>[0-9]+)$',
        views.get_delete_update_stock,
        name='get_delete_update_stock'
    ),
    url(
        r'^stocks/$',
        views.get_post_stock,
        name='get_post_stock'
    )
]

#urlpatterns = format_suffix_patterns(urlpatterns)
