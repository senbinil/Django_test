from search_module.views import search_base
from django.urls import path
from django.urls.conf import include
from .views import get_all_product_cat, get_product, home
app_name='shopin'
urlpatterns=[
    path('',get_all_product_cat,name='allcat'),
    path('<slug:catslug>/',get_all_product_cat,name='product_by_cat'),
    path('<slug:cat_slug>/<slug:product_slug>/',get_product,name='product_detail'),
]