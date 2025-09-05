
---

### 📄 `retrieve.md`
```markdown
# Retrieve a Book

**Command:**
```python
retrieved_book = Book.objects.get(id=1)
print(retrieved_book.id, retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)



1 1984 George Orwell 1949
