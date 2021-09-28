from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(req):
    return render(req,'index.html')
def get_all_product_cat(req,catslug=None):
    cat_page=None
    products_list=None
    if catslug!=None:
        cat_page=get_object_or_404(Category,slug=catslug)
        products_list=Product.objects.all().filter(category=cat_page,available=True)
    else:
        products_list=Product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(req.GET.get('page'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    print(paginator.num_pages)
    return render(req,'category.html',{'category':cat_page,'products':products})

def get_product(req,cat_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=cat_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(req,'product.html',{'product':product})
