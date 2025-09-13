
# Delete a Book

**Command:**
```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()

print(Book.objects.all())



(1, {'bookshelf.Book': 1})
<QuerySet []>
