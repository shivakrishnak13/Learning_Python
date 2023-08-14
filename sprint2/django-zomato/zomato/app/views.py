from django.shortcuts import render,redirect
import json
import os
from . import forms
from django.contrib import messages


# Create your views here.
inventory = './inventory.json'

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Set the working directory to the script's directory
os.chdir(script_directory)

def load_file():
    with open(inventory,'r') as file :
        data= json.load(file)
        return data

dishes = load_file()["dishes"]
orders = load_file()['orders']

def save_iventory(dishes,orders) :
    data = {"dishes" : dishes,"orders":orders}
    # Write JSON object into a file
    with open(inventory,'w')as file:
        json.dump(data,file,indent=4)


def add_dish(request) :
    form = forms.DishForm()
    if request.method == 'POST' :
        form = forms.DishForm(request.POST)
        if form.is_valid() :
            newDish = {
                "id" : dishes[-1]['id']+1,
                "name" : form.cleaned_data['name'],
                "price" : float(form.cleaned_data["price"]),
                "availability" : form.cleaned_data["availability"]
            }
        
            dishes.append(newDish)
            save_iventory(dishes,orders)
            messages.success(request, 'Product added successfully!')

            return redirect('add_dish')

    all_messages = messages.get_messages(request)
    return render(request, 'add_dish.html', {'form': form, 'messages': all_messages})


def home(request) :
    return render(request,'index.html',{'dishes':dishes,"Orders":orders})


def update(request,id) :
    dish=None
    for i in dishes :
        if i['id'] == id :
            dish=i

    form = forms.DishForm()
    if request.method == "POST" :
        form = forms.DishForm(request.POST)
        if form.is_valid() :
            for item in dishes :
                if item['id'] == id :
                    item['name'] = form.cleaned_data["name"]
                    item['price'] = float(form.cleaned_data["price"])
                    item['availability'] = form.cleaned_data['availability']
            save_iventory(dishes,orders)
            return redirect("home")
    
    return render(request,'update.html',{'dish':dish})


def delete(request,id) :
    newDishes = [dish for dish in dishes if dish['id'] != id]
    save_iventory(newDishes,orders)
    return redirect("home")


def place_order(request,id) :
    dish=None
    for i in dishes :
        if i['id'] == id :
            dish=i
    form = forms.OrderForm()
    order_id= None
    if orders:
        order_id = orders[-1]['order_id'] + 1
    else:
        order_id = 1
    if request.method == 'POST' :
        form = forms.OrderForm(request.POST) 
        if form.is_valid() :
            newOrder = {
                "order_id": order_id,
                "name": form.cleaned_data['customerName'],
                "quantity" : form.cleaned_data["quantity"],
                "totalPrice" : (float)(dish['price']) * int((form.cleaned_data["quantity"])),
                'item_name' : dish['name'],
                'item_price' : dish['price'],
                'status' :"Pending"
            }
            orders.append(newOrder)
            save_iventory(dishes,orders)
    return render(request,'order.html',{'dish':dish})


def update_status(request,id) :
    initst = None
    for i in orders :
        if i['order_id'] == id :
            initst = i['status']
    form = forms.UpdateStatus()
    if request.method == "POST" :
        form = forms.UpdateStatus(request.POST)
        if form.is_valid(): 
            status = form.cleaned_data['status']
            for item in orders :
                if item['order_id'] == id :
                    item['status']=status
            save_iventory(dishes,orders)
            return redirect('home')
    return render(request,'updatestatus.html',{'status':initst})
