from django.shortcuts import render
from products.models import add_product

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def gallery(request):
    products=add_product.objects.all()
    print(products)
    print("******************************\n")
    print(products[0].image)
    return render(request,"gallery.html",{"products" : products})
    return render(request,"gallery.html")

def contact(request):
    return render(request,"contact.html")
def services(request):
    return render(request,"services.html")
