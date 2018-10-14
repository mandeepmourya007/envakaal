

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    #path("index/",views.index,name="index"),
    path("contact/",views.contact,name="contact"),
    path("services/",views.services,name="services"),

    path("gallery/",views.gallery,name="gallery"),
    #path("gallery/", include('products.urls')),
    #path("services/", include('services.urls')),


]
