
---

### 📄 `update.md`
```markdown
# Update a Book

**Command:**
```python
book_to_update = Book.objects.get(id=1)
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(book_to_update.id, book_to_update.title, book_to_update.author, book_to_update.publication_year)


1 Nineteen Eighty-Four George Orwell 1949
