from shop.models import Category, Product
from django.contrib import admin

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','available','created','updated']
    prepopulated_fields={'slug':('name',)}
    list_editable=['price','stock','available']
    list_per_page=20
admin.site.register(Product,ProductAdmin)