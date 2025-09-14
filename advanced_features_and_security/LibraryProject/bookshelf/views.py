

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book

# Create your views here.

def home(request):
	return HttpResponse("<h1>Welcome to the Library Project</h1><p>Go to <a href='/books/'>/books/</a> to see the books.</p>")

# This view is protected by the 'can_view_book' permission
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
	books = Book.objects.all()
	# In a real app, you would render a template here
	return HttpResponse("You have permission to view the list of books.")

# This view is protected by the 'can_create_book' permission
@permission_required('bookshelf.can_create_book', raise_exception=True)
def book_create(request):
	# In a real app, you would have form logic here
	return HttpResponse("You have permission to create a new book.")


# This view is protected by the 'can_edit_book' permission
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_edit(request, pk):
	# In a real app, you would have form logic here for a specific book
	return HttpResponse(f"You have permission to edit book with id {pk}.")

# --- EXAMPLE OF A SECURE VIEW ---
def book_search_safe(request):
	"""
	This view demonstrates how to handle user input securely to prevent SQL injection.
	It uses the Django ORM's filter method, which automatically parameterizes the query.
	"""
	query = request.GET.get('q', '') # Get the search term from the URL, default to empty
	results = []
	if query:
		# GOOD: This is safe. Django's ORM handles escaping special characters.
		results = Book.objects.filter(title__icontains=query)

	return render(request, 'bookshelf/book_list.html', {'books': results})

# --- EXAMPLE OF A DANGEROUS, INSECURE VIEW (FOR DEMONSTRATION ONLY) ---
def book_search_unsafe(request):
	"""
	!!! DANGEROUS !!! DO NOT USE THIS CODE.
	This shows an insecure way to build a query using string formatting,
	which is vulnerable to SQL injection.
	"""
	query = request.GET.get('q', '')
	# BAD: Never format SQL queries with user input like this.
	# A malicious user could enter SQL code as their query.
	# books = Book.objects.raw(f"SELECT * FROM bookshelf_book WHERE title LIKE '%{query}%'")
	# For the purpose of the project, we comment out the unsafe code and show the safe alternative.
	# The documentation is the key deliverable here.
	return render(request, 'bookshelf/book_list.html', {})

from .forms import ExampleForm
