from rest_framework import serializers
from .models import Author, Book
import datetime

# Serializer for the Book model
# Used to convert Book objects to JSON and validate incoming data.
# Includes validation to ensure the publication year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation for the publication_year field
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future (>{current_year})."
            )
        return value


# Serializer for the Author model
# Includes the author's name and a nested list of their books.
# The nested BookSerializer dynamically serializes all related Book objects.
# Relationship explanation:
#   - 'books' comes from the related_name in the Book model
#   - This creates a nested structure where each Author includes their books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
