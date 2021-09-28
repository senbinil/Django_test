from django.http.response import HttpResponse
from django.shortcuts import render
from shop.models import Product,Category
from django.db.models import Q
# Create your views here.

def search_base(req):
    if req.GET['search_key']!='':
        print(req.GET['search_key'])
        key=req.GET.get('search_key')
        print(key)
        key=key.capitalize()
        matched_data=Product.objects.all().filter(Q(name__contains=key.capitalize()) | Q(title__contains=key.capitalize()) | Q(name__contains=key) | Q(title__contains=key))
        print(matched_data)
        return render(req,'search.html',{'key':key,'result':matched_data})
    return render(req,'search.html')