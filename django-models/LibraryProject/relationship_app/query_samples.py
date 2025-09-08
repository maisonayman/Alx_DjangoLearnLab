import django
import os
import sys

sys.path.append(r"D:/ALX_tasks/Alx_DjangoLearnLab/django-models/LibraryProject")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print("Books by George Orwell:")
for book in books_by_author:
    print("-", book.title)

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
print(f"\nBooks in {library.name}:")
for book in library.books.all():
    print("-", book.title)

# 3. Retrieve the librarian for a library
librarian = library.librarian
print(f"\nLibrarian for {library.name}: {librarian.name}")
