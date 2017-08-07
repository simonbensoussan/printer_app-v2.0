from django.conf.urls import *
from . import views
from django.views.generic import TemplateView

#easy for the mapping
# app_name ='catalog'

urlpatterns = [
        url(r'^$', views.index, name ='index'),
        url(r'^product/$', views.ProductListView.as_view(), name ='product'), # generic url
        url(r'^product/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name = 'product-detail'), # name the same in the function in the model get_absolute
        url(r'^provider/$', views.ProviderListView.as_view(), name ='provider'),
        url(r'^product/add/$', views.ProductCreate.as_view(), name ='product-add'),
        #success template after creation
        url(r'^congratulations/', TemplateView.as_view(template_name="catalog/success_creation.html"), name='success_create'),
        url(r'^product/(?P<pk>[0-9]+)$', views.ProductUpdate.as_view(), name = 'product-update'),
        url(r'^product/(?P<pk>[0-9]+)/delete$', views.ProductDelete.as_view(), name = 'product-delete')
        
    ]