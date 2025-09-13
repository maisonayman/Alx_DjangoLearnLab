from django.urls import path
from .views import LibraryDetailView
from .views import list_books, register, add_book, edit_book, delete_book
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .admin_view import admin_dashboard
from .librarian_view import librarian_dashboard
from .member_view import member_dashboard

urlpatterns = [
    path("add_book/", add_book, name="add_book"),
    path("edit_book/<int:book_id>/",edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/", delete_book, name="delete_book"),
    path("books/", list_books, name="list_books"),  # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
    path("register/", register, name="register"),  # function-based view
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),

]
