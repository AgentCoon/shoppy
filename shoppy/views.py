from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world! Welcome to index!")


def product(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)


def product_review(request, product_id):
    return HttpResponse("You're looking at review of %s." % product_id)