from django.shortcuts import render, redirect
from .models import Book, Library
from django.views.generic.detail import DetailView   

# ✅ الاستيرادات المطلوبة عشان التشيك يمر
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)   # ✅ استخدم الفورم الجاهز من Django
        if form.is_valid():
            user = form.save()
            login(request, user)   # ✅ يعمل تسجيل دخول للمستخدم مباشرة
            return redirect("login")   # رجّعه لصفحة login
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# ====== شروط التحقق من role ======
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# ====== Views لكل role ======

@user_passes_test(is_admin, login_url='/no-access/')
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian, login_url='/no-access/')
def librarian_dashboard(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member, login_url='/no-access/')
def member_dashboard(request):
    return render(request, 'relationship_app/member_view.html')
