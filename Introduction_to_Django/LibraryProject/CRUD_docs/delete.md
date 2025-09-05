
---

### 📄 `delete.md`
```markdown
# Delete a Book

**Command:**
```python
book_to_delete = Book.objects.get(id=1)
book_to_delete.delete()

print(Book.objects.all())



(1, {'bookshelf.Book': 1})
<QuerySet []>
