import django
import os
import sys

# خلي Python يعرف مكان المشروع
sys.path.append(r"D:\ALX_tasks\Alx_DjangoLearnLab\django-models\LibraryProject")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Variables for queries
author_name = "George Orwell"
library_name = "Central Library"

# 1. Query all books by a specific author
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print("-", book.title)

# 2. List all books in a library
library = Library.objects.get(name=library_name)  # ✅ ده اللي الرسالة طالبه
print(f"\nBooks in {library.name}:")
for book in library.books.all():
    print("-", book.title)

# 3. Retrieve the librarian for a library
librarian = library.librarian
print(f"\nLibrarian for {library.name}: {librarian.name}")
