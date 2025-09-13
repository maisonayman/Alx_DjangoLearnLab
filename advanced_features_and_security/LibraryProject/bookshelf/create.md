# Create a Book

**Command:**
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print(book.id, book.title, book.author, book.publication_year)


1 1984 George Orwell 1949
