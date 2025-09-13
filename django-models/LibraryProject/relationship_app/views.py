from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, permission_required
from .models import Book, Library

# عرض كل الكتب (مفتوح للجميع)
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# إضافة كتاب (محتاج permission can_add_book)
@permission_required('relationship_app.can_add_book')
def add_book(request):
    # هنا أي كود لإضافة كتاب (manual أو form) 
    return render(request, "relationship_app/add_book.html")


# تعديل كتاب (محتاج permission can_change_book)
@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    # كود تعديل كتاب
    return render(request, "relationship_app/edit_book.html")


# حذف كتاب (محتاج permission can_delete_book)
@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    # كود حذف كتاب
    return render(request, "relationship_app/delete_book.html")


# -------------------- Library View --------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# -------------------- User Registration --------------------
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


# -------------------- Roles Dashboards --------------------
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
