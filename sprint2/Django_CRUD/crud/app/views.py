from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

data={}

def create(request) :
    name = input('Enter your Name: ') 
    age = input('Enter your age: ') 
    city = input('Enter your city: ') 
    data["name"] = name
    data["age"]=age
    data["city"]=city

    return JsonResponse({"message":"data successfully added","data":data})


def read(request) :
    return JsonResponse({"data":data})

def update(request) :
    name=input("enter new value for name: ")
    age=input("enter new value for age: ")
    city=input("enter new value for city: ")
    if len(name)==0 or not isinstance (name,str):
        raise ValueError ("Invalid Value")
    else:
        data['name']=name
        data['age']=age
        data['city']=city
        return  JsonResponse({'message':'Data updated','data':data})

def delete(request) :

    del data["name"]
    del data["age"]
    del data["city"]
    return JsonResponse({"data":data})
