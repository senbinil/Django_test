from cart_module.views import add_cart, cart_minus, cartview, delete_item, get_session_id
from django.urls import path

app_name='cart'

urlpatterns=[ 
    path('',cartview,name='cart'),
    path('addcart/<int:product_id>/',add_cart,name='addcart'),
    path('cart_update/<int:product_id>/',cart_minus,name='cartminus'),
    path('remove/<int:product_id>',delete_item,name='remove_item'),
]