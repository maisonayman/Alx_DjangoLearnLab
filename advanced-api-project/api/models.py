from django.db import models

# The Author model represents a book author.
# Each author can be linked to multiple books (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name


# The Book model represents a single book.
# Each book has a title, a publication year, and belongs to one author.
# The ForeignKey creates a one-to-many relationship:
#   - One author can have many books
#   - Each book is linked to exactly one author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Allows reverse lookup: author.books.all()

    def __str__(self):
        return f"{self.title} by {self.author}"
