from django.contrib import admin
from .models import Book
# Register your models here.
# Custom admin configuration for Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  
    list_filter = ("publication_year", "author")            
    search_fields = ("title", "author")                     

# Register the model with custom admin class
admin.site.register(Book, BookAdmin)
