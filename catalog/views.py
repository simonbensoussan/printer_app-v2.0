from django.shortcuts import render
from .models import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    
    """
    View function for home page of site.
    Test with def for display info
    without use generic old method
    """
    num_product = Product.objects.all().count()
    num_provider = Provider.objects.all().count()
    num_market = MarketPlace.objects.all().count()
    context = {'nbre_produit': num_product,
               'nbre_fournisseur': num_provider,
               'nbre_market' : num_market
                }
    return render(request,'catalog/test.html', context)

class ProductListView(generic.ListView):
    '''
        Class display all objects of the model to the template, simply and more powerfull
    '''
    # specific the model to display in the template
    model = Product
    # your own name for the list as a template variable
    context_object_name = 'my_product_list'
    #specific query example Get 5 books containing the title war
    # queryset  = Product.objects.filter(title__icontains = 's')[:5]
    template_name = 'catalog/productList.html' # my_templte_for_ProductList
   
    '''
        Queryset method override another way to make the things
        
        def get_queryset(self):
        return Product.objects.filter(title__icontains ='S')[:5]
    '''

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'catalog/productDetail.html'
    context_object_name = 'product' 
    
# creer une autre view pour le provider
class ProviderListView(generic.ListView):
    '''
       Display genric list of all provider
    '''
    model = Provider
    template_name = 'catalog/providerList.html'
    context_object_name  = 'provider_list'
    
    #queryset function

class ProductCreate(CreateView):
    '''
    Create a new product from the modal in js
    it's also a way to create a ModelForm, thank to the url yoou don't need to create a file form 
    with new class of type form.formModel everything is incorporate into the generic class
    '''
    model = Product
    fields = ['name','marque','image','price_HT','marketplace','provider','remise']
    #redirect to success template after registration
    success_url = reverse_lazy('success_create')
class ProductUpdate(UpdateView):
    '''
    Update a product
    '''
    model = Product
    fields = ['price_HT','provider']

class ProductDelete(DeleteView):
    '''
    Delete a product
    '''
    model = Product
  # template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('product')