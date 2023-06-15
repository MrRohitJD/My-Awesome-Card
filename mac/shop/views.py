from django.shortcuts import render
from .models import Product,Contact,Orders, OrderUpdate
from math import ceil
from django.contrib import messages
from django.http import HttpResponse
import json

import paytmchecksum
from django.views.decorators.csrf import csrf_exempt
import requests
import datetime

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


MERCHANT_KEY = 'bKMfNxPPf_QdZppa'
mid="DIY12386817555501617"
def checkout(request):
    global id
    if request.method =="POST":
        items_json =request.POST.get('IitemsJson', '')
        name = request.POST.get('Iname', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('Iemail','')
        address = request.POST.get('IAddress','') + " " + request.POST.get('address2', '')
        city = request.POST.get('Icity','')
        state = request.POST.get('Istate','')
        zip_code = request.POST.get('Izip','')
        phone = request.POST.get('Iphone','')
                        # modelName = viewsName
        orders = Orders(Mitems_json=items_json, Mamount=amount, Mname=name,Memail=email, Maddress= address , Mcity=city, Mstate=state,Mzip_code=zip_code,Mphone=phone)
        orders.save()
        update =OrderUpdate(order_id =orders.Morder_id, update_desc="the order has been placed" )
        update.save()
        thank =True;
        id = orders.Morder_id
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
        # Request paytm to transfer the amount to your account after payment by user
        paytmParams = dict()

        paytmParams["body"] = {
            "requestType": "Payment",
            "mid": mid,
            "websiteName": "My-Awesome-Caed",
            "orderId": str(orders.Morder_id),
            "callbackUrl": 'http://127.0.0.1:8000/shop/handelrequest/',
            "txnAmount": {
                "value": str(amount),
                "currency": "INR",
            },
            "userInfo": {
                "custId": email,
            },
        }

        # Generate checksum by parameters we have in body
        # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        checksum = paytmchecksum.generateSignature(json.dumps(paytmParams["body"]), MERCHANT_KEY)

        paytmParams["head"] = {
            "signature": checksum
        }
        post_data = json.dumps(paytmParams)

        # for Staging
        url = "https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid=DIY12386817555501617&orderId=ORDERID_98765"

        # for Production
        # url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=YOUR_MID_HERE&orderId=ORDERID_98765"
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()
        print(response)

        return render(request, 'shop/paytm.html', {'param_dict': response })

    return render(request, 'shop/checkout.html')

@csrf_exempt
def handelrequest(request):
    # import checksum generation utility
    # You can get this utility from https://developer.paytm.com/docs/checksum/

    # initialize a dictionary
    paytmParams = dict()

    # body parameters
    paytmParams["body"] = {

        # Find your MID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        "mid": mid,

        # Enter your order id which needs to be check status for
        "orderId": str(id),
    }

    # Generate checksum by parameters we have in body
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
    checksum = paytmchecksum.generateSignature(json.dumps(paytmParams["body"]), "YOUR_MERCHANT_KEY")

    # head parameters
    paytmParams["head"] = {

        # put generated checksum value here
        "signature": checksum
    }

    # prepare JSON string for request
    post_data = json.dumps(paytmParams)

    # for Staging
    url = "https://securegw-stage.paytm.in/v3/order/status"

    # for Production
    # url = "https://securegw.paytm.in/v3/order/status"

    response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

    return render(request, 'shop/paymentstatus.html', {'response': response})



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
    return render(request, 'shop/thank_you.html',{'id':id})

