from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
import pymongo
from bson import ObjectId

my_client = pymongo.MongoClient('mongodb://localhost:27017')
db = my_client['ZomatoChronicles']
menuData = db['menu']
totalOrders = db['orders']


def dummy(request):
    menu_cursor = menuData.find({})
    menu_data = list(
        map(lambda item: {
            "id": str(item["_id"]),
            "name": item["name"],
            "price": item["price"],
            "availability": item["availability"],
            "image": item["image"]}, menu_cursor))
    return JsonResponse({"data": menu_data}, safe=False)


def home(request):
    return render(request, "index.html")


def menu(request):
    try:
        menu_curser = menuData.find({})
        zomatoMenu = list(map(lambda item: {
            "id": str(item["_id"]),
            "name": item["name"],
            "price": item["price"],
            "availability": item["availability"],
            "image": item["image"]}, menu_curser))
        context = {"menu": zomatoMenu}
        return render(request, "menu.html", context=context)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def add_dish(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        image = request.POST.get("image")
        availability = request.POST.get("availability") == "on"
        dish = {"name": name, "price": price,
                "availability": availability, "image": image}
        menuData.insert_one(dish)
        return redirect("menu")
    return render(request, "add_dish.html")


def delete_dish(request, dish_id):
    dish_id = ObjectId(dish_id)
    try:
        menuData.find_one_and_delete({"_id": dish_id})
        return redirect("menu")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def update_dish(request, dish_id):
    dish_id = ObjectId(dish_id)
    item = menuData.find_one({"_id": dish_id})
    item["_id"] = str(item["_id"])
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        image = request.POST.get("image")
        availability = request.POST.get(
            "availability") == "on"  # to get the checkbox value
        updatedDish = {
            "$set": {
                "name": name,
                "price": price,
                "availability": availability,
                "image": image}
        }
        menuData.find_one_and_update({"_id": dish_id}, updatedDish)
        return redirect("menu")
    return render(request, "update_dish.html", {"dish": item})


def orders_list(request):
    try:
        orders = totalOrders.find({})
        orders = list(map(lambda item: {
            "id": str(item["_id"]),
            "customer_name": item["customer_name"],
            "dishes": item["dishes"],
            "status": item["status"],
            "total_amount": item["total_amount"]}, orders)
        )
        return render(request, "orders.html", {"orders": orders})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def process_order(request):
    menuItems = menuData.find({"availability": True})
    menuItems = list(map(lambda item: {
        "id": str(item["_id"]),
        "name": item["name"],
        "price": item["price"],
        "availability": item["availability"],
        "image": item["image"]}, menuItems)
    )
    if request.method == "POST":
        customer_name = request.POST.get("name")
        dish_ids = request.POST.getlist("selected_ids")
        total_amount = 0
        order_dishes = []
        # Check dish availability and calculate total amount
        for dish_id in dish_ids:
            dish = next(
                (item for item in menuItems if item["id"] == dish_id), None)
            if dish and dish["availability"]:
                total_amount += float(dish["price"])
                order_dishes.append(dish)
            else:
                return HttpResponse("Some items are not available please check.")

        order = {
            "customer_name": customer_name,
            "dishes": order_dishes,
            "status": "received",
            "total_amount": total_amount
        }
        totalOrders.insert_one(order)
        return redirect("orders_list")
    return render(request, "process_order.html", {"menu": menuItems})


def update_status(request, order_id):
    try:
        order_id = ObjectId(order_id)
        order = totalOrders.find_one({"_id": order_id})
        statuses = ["received", "ready for pickup", "preparing", "delivered"]
        statuses = list(filter(lambda status: status !=
                        order["status"], statuses))
        if request.method == "POST":
            if order != None:
                newStatus = request.POST.get("updated_status")
                totalOrders.find_one_and_update(
                    {"_id": order_id}, {"$set": {"status": newStatus}})
                return redirect("orders_list")
            return JsonResponse({"message": "Order not found."}, status=404)
        return render(request, "updatestatus.html", {"order": order, "statuses": statuses})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

