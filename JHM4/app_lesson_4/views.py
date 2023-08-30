from django.shortcuts import render
from django.http import HttpResponse
def index(requests):
    return render(requests, 'index.html')
def top_sellers(requests):
    return render(requests, 'top-sellers.html')

def advertis(requests):
    return render(requests, 'advertisement.html')
def advertisement_post(requests):
    return render(requests, 'advertisement-post.html')
def login(requests):
    return render(requests, 'login.html')
def profile(requests):
    return render(requests, 'profile.html')
def register(requests):
    return render(requests, 'register.html')