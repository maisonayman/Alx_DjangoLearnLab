from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .models import Book, Library


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return render(request, "relationship_app/add_book.html")


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    return render(request, "relationship_app/edit_book.html")


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    return render(request, "relationship_app/delete_book.html")


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin, login_url='/no-access/')
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian, login_url='/no-access/')
def librarian_dashboard(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member, login_url='/no-access/')
def member_dashboard(request):
    return render(request, 'relationship_app/member_view.html')
