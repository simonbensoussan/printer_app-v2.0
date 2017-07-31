
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from landing.views import CreateView
from landing import views
from landing import views_generic


urlpatterns = [
    url(r'^stocks-test/$', views_generic.CreateView.as_view(), name="get_post_stock"), #create
    url(r'^stocks-test/(?P<pk>[0-9]+)$', views_generic.StocksDetail.as_view(), name="get_delete_update_stock"),
    # url(
    #     r'^stocks/(?P<pk>[0-9]+)$',
    #     views.get_delete_update_stock,
    #     name='get_delete_update_stock'
    #     #name='detail'
    # ),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),  # ADD THIS URL
    # url(
    #     r'^stocks/$',
    #     views.get_post_stock,
    #     name='get_post_stock'
    #     #name='create'
    # )
]

urlpatterns = format_suffix_patterns(urlpatterns)
