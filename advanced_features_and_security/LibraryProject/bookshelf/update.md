
# Update a Book

**Command:**
```python
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(book.id, book.title, book.author, book.publication_year)


1 Nineteen Eighty-Four George Orwell 1949
