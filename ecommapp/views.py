from django.shortcuts import render, redirect
from ecommapp.models import Product, Contact, Order
from django.contrib.auth.models import User, auth
from accounts.models import Address
from django.contrib import messages
from datetime import datetime
from math import ceil
from django.contrib.auth import logout
# Create your views here.
def index(request):
    data = Product.objects.all() #get all products under Product
    all_products = []
    category_products = Product.objects.values('category','id') #get the different categories
    categories = {item['category'] for item in category_products} #list of categories using list comprehension
    for category in categories: 
        prod = Product.objects.filter(category = category) #get products by the respective category in a list called prod
        n = len(prod) #number of products under one category
        nSlides = n//4 + ceil(n/4-n//4) #logic for displaying slides
        all_products.append([prod,range(1,nSlides),nSlides])  #Ask about this line
    params = {'all_products': all_products} #bcz render accepts only a dictionary, params is just all_products but as a dict
    return render(request,'index.html', params)
    

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        #Create a Contact object 
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today()) 
        contact.save()
        messages.success(request, 'Success! Your message has been sent.')
    return render(request, 'contact.html')

def productview(request, myid):
    product = Product.objects.filter(id = myid) #Here product is a list of lists
                                                #where product[i] is a list of all the attributes associated with a 
    return render(request, 'productview.html', {'product':product[0]}) #Since ids are unique, there will be only one item with each id

def checkout(request):
    if request.method == 'POST':
        
        items_json = request.POST.get("items_json") #Inside "" is the same as defined in the model
                                                   #and same as the name attribute in the particular field of the form  
        name = request.user.first_name + " " + request.user.last_name #Important to use 'request.'user
        addressline = request.user.address.addressline
        city = request.user.address.city
        state = request.user.address.state
        zip_code = request.user.address.zip_code
        phone = request.user.address.phone

        # Create an Order object named order
        order = Order(items_json = items_json, name=name, addressline=addressline,
        city = city, state=state, zip_code=zip_code, phone=phone) #<Inside_model_name> = <variable_inside_funciton>
        # order = Order(name = name, items_json = items_json)
        order.save()
        ordered = True #To complete the process of checkout
        return render(request, 'checkout.html', {'ordered':ordered})
    else:
        if request.user.is_authenticated:    
            return render(request, 'checkout.html')
        else:
            return redirect('login')
