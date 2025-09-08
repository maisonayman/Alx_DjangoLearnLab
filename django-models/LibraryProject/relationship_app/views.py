from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView


# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})


# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
