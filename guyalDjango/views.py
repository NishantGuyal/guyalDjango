from django.http import HttpResponse


def home(response):
    return HttpResponse("Hello, world!")


def about(response):
    return HttpResponse("Welcome to About page")


def contact(response):
    return HttpResponse("Welcome to Contact page")
