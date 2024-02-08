from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello, World!')

def listings(request):
    return HttpResponse("<ol><li>Maksym</><li>Monica</><li>Shipa</></ol>")

def search_item(request, item_id):
    items = ["laptop", "Android Phone", "Keyboard", "Mouse"]
    item = items[item_id]
    return HttpResponse(f'You requested item {item}.')

def search_item_by_key(request, item_name):
    items = {
        "Phones": "We have some android phones in stock",
        "Laptops": "We also sell high-end laptops",
        "Monitors": "Yop of the line monitors available",
    }
    item = items[item_name]
    return HttpResponse(item)