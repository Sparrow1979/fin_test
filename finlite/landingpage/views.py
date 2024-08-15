from django.shortcuts import render
from django.contrib import admin

test_data = [
    {
        'company': 'bf',
        'revenue':100000,
        'cogs':80000,
        'profit': 20000
        },
    {
        'company': 'fl',
        'revenue':200000,
        'cogs':150000,
        'profit': 50000
        }
        ]

def landing_page(request):
    context = {
        'company': test_data
    }
    return render(request, 'landingpage/index.html', context)

def  about(request):
    return render(request, 'landingpage/about.html', {'title': 'ABOUT'})
