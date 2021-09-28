from django.db import models
from shop.models import Product,Category
# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=240,blank=True)
    date_added=models.DateField(auto_now=True)

    class Meta:
        ordering=['cart_id',]
    def __str__(self) -> str:
        return str(self.cart_id)

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart_id=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price* self.quantity

    