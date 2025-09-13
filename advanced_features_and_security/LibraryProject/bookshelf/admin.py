from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
# Custom admin configuration for Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  
    list_filter = ("publication_year", "author")            
    search_fields = ("title", "author")                     

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  
    list_filter = ("publication_year", "author")            
    search_fields = ("title", "author")                     

# Register the model with custom admin class
admin.site.register(Book, BookAdmin)



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "date_of_birth", "is_staff", "is_active"]
    search_fields = ["username", "email"]
    ordering = ["username"]

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "date_of_birth", "profile_photo", "password1", "password2", "is_staff", "is_active")}
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
