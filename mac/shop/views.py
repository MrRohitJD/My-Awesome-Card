from django.shortcuts import render
from .models import Product,Contact,Orders, OrderUpdate
from math import ceil
from django.contrib import messages
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('Category', 'id')
    cats = {item['Category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(Category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method =="POST":
        name = request.POST.get('Iname', '')
        email = request.POST.get('Iemail','')
        phone = request.POST.get('Iphone','')
        desc = request.POST.get('Idesc' , '')
        contact = Contact(Mname=name,Memail=email,Mphone=phone,Mdesc=desc)
        contact.save()
        messages.info(request, 'successfully send your query  --we contact you as soon as possible...')
    return render(request, 'shop/contact.html')

def search(request):
    return HttpResponse("We are at search")

def productView(request, myid):
    product = Product.objects.filter(id =myid)
    print(product)
    return render(request, 'shop/productView.html',{'prod':product[0]})

orders =None
def checkout(request):
    if request.method =="POST":
        items_json =request.POST.get('IitemsJson', '')
        name = request.POST.get('Iname', '')
        email = request.POST.get('Iemail','')
        address = request.POST.get('IAddress','') + " " + request.POST.get('address2', '')
        city = request.POST.get('Icity','')
        state = request.POST.get('Istate','')
        zip_code = request.POST.get('Izip','')
        phone = request.POST.get('Iphone','')
                        # modelName = viewsName
        orders = Orders(Mitems_json=items_json, Mname=name,Memail=email, Maddress= address , Mcity=city, Mstate=state,Mzip_code=zip_code,Mphone=phone)
        orders.save()
        update =OrderUpdate(order_id =orders.Morder_id, update_desc="the order has been placed" )
        update.save()
        thank =True;
        id= orders.Morder_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')

def tracker(request):
    if request.method=="POST":
        orderID =request.POST.get('IorderId','')
        email =request.POST.get('Iemail','')
        
        try:
            orders = Orders.objects.filter(Morder_id= orderID, Memail=email)
            if len(orders)>0:
                update = OrderUpdate.objects.filter(order_id =orderID)
                updates=[]
                for item in update:
                    updates.append({'text': item.update_desc, 'time':item.timestamp})
                    response = json.dumps(updates)
                    return HttpResponse(response)
                
            else:
                return HttpResponse('{}')
        except Exception as e:
                return HttpResponse('{}')
            
    return render(request, 'shop/tracker.html')




def thank_you(request):
    # id= orders.Morder_id
    return render(request, 'shop/thank_you.html',{'id':id})