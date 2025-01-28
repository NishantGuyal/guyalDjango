from django.shortcuts import render
from django.http import HttpResponse


def home(response):
    return render(response, "home.html")


def about(response):
    return HttpResponse("Welcome to About page")


def contact(response):
    return HttpResponse("Welcome to Contact page")
