from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.

@api_view(['GET'])

def list_books(request):
    books = Book.objects.all()
    
    if not books:
        return HttpResponse("No books found.")
    
    response_text = "Books in the database:\n\n"
    for book in books:
        response_text += f"- {book.title} (Author: {book.author.name})\n"
    
    return HttpResponse(response_text, content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"   
    context_object_name = "library" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context


