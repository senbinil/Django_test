from .views import search_base
from django.urls import path

app_name='search_module'

urlpatterns=[ 
    path('',search_base,name='search'),
]