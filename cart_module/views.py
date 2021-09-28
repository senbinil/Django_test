from django.core.exceptions import ObjectDoesNotExist
from shop.models import Product
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart,CartItem

# Create your views here.
def cartview(req):
    try:
        cart=Cart.objects.get(cart_id=get_session_id(req))
        cart_items=CartItem.objects.filter(cart_id=cart,active=True)  
        item_total={}
        total=0
        counter=0
        for cart_item in cart_items:
            total+=(cart_item.product.price*cart_item.quantity)
            counter+=cart_item.quantity
    except ObjectDoesNotExist:
        return render(req,'cart.html')
    return render(req,'cart.html',{'items':cart_items,'total':total,'counter':counter})

def get_session_id(req):
    cart_id=req.session.session_key
    if not cart_id:
        cart_id=req.session.create()
    print(cart_id)
    return cart_id
def add_cart(req,product_id):
    get_product=Product.objects.get(id=product_id)
    #check if cart exist
    #if exist get cart details else create a new cart with session id 
    #as cart ID
    try:
        cart_details=Cart.objects.get(cart_id=get_session_id(req))
    except Cart.DoesNotExist:
        cart_details=Cart.objects.create(
           cart_id=get_session_id(req),
        )
        cart_details.save()
    # with cart details in hand  
    # 1st case , check if product already exit if yes increase it quantity
    #else create a record with product details and cart ID
    try:
        cart_product=CartItem.objects.get(product=get_product,cart_id=cart_details)
        if cart_product.quantity< cart_product.product.stock:
            cart_product.quantity+=1
        cart_product.save()
    except CartItem.DoesNotExist:
        cart_product=CartItem.objects.create(
            product=get_product,
            cart_id=cart_details,
            quantity=1,
        )
    return redirect('cart:cart')


def cart_minus(req,product_id):
    # get cart
    cart=Cart.objects.get(cart_id=get_session_id(req))
    product=get_object_or_404(Product,id=product_id)
    # cart item
    cart_item=CartItem.objects.get(cart_id=cart,product=product)
    # updating cart item quantity 
    if cart_item.quantity > 1:
        cart_item.quantity-=1
        cart_item.save()
    # if quantity  is 1 then remove given item
    else:
        cart_item.delete()
    return redirect('cart:cart')

def delete_item(req,product_id):
     # get cart
    cart=Cart.objects.get(cart_id=get_session_id(req))
    product=get_object_or_404(Product,id=product_id)
    # cart item
    cart_item=CartItem.objects.get(cart_id=cart,product=product)
    cart_item.delete()
    return redirect('cart:cart')