from django.core.exceptions import ObjectDoesNotExist
from .models import CartItem,Cart
from .views import get_session_id

def item_count(req):
    items_count=0
    if 'admin' in req.path:
        return {}
    else:
        try:
            cart=Cart.objects.get(cart_id=get_session_id(req))
            cart_product=CartItem.objects.filter(cart_id=cart)
            for i in cart_product:
                items_count+=1
        except ObjectDoesNotExist:
            items_count=0
    return dict(item_count=items_count)