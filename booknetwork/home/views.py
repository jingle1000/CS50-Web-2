from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

books = [
    {
        'isbn': 'xxxxxxxxxxxxxx',
        'title': 'A Book Title',
        'author': 'Bob Smith',
        'year_published': '2018'
    },
    {
        'isbn': 'xxxxxxxxxxxxxx',
        'title': 'A Book Title',
        'author': 'Bob Smith',
        'year_published': '2018'
    },
    {
        'isbn': 'xxxxxxxxxxxxxx',
        'title': 'A Book Title',
        'author': 'Bob Smith',
        'year_published': '2018'
    }
]

def home(request):
    content = {
        'books': books
    }
    return render(request, 'home/layout.html', content)
