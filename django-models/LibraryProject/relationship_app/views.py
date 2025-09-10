from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView   
from .forms import RegisterForm

# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')   # بعد التسجيل روح للصفحة login
    else:
        form = RegisterForm()
    return render(request, 'relationship_app/register.html', {"form": form})
