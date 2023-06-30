from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="ShopHome"),
    path("about", views.about, name="About"),
    path("contact",views.contact,name="Contact"),
    path("tracker", views.tracker,name="TrackingStatus"),
    path("search",views.search,name= "Search"),
    # path("productView",views.productView,name= "ProductView"),
    path("productViews/<int:myid>", views.productView, name="ProductView"),
    path("checkout",views.checkout,name= "checkout"),
    path("thank_you",views.thank_you,name="thank_you")

]