import django
import os
import sys

sys.path.append(r"D:\ALX_tasks\Alx_DjangoLearnLab\django-models\LibraryProject")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author_name = "George Orwell"
library_name = "Central Library"

author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print("-", book.title)

library = Library.objects.get(name=library_name)
print(f"\nBooks in {library.name}:")
for book in library.books.all():
    print("-", book.title)

librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library.name}: {librarian.name}")
