from django.shortcuts import render
from .models import JejuOlle, Shop

# Create your views here.


def shop(request):
    shop_list = Shop.objects.all()

    return render(request,
                  'thirdapp/shop.html',
                  {'shop_list': shop_list})


def olle(request):
    olle_list = JejuOlle.objects.all()

    return render(request,
                  'thirdapp/olle.html',
                  {'olle_list': olle_list})
