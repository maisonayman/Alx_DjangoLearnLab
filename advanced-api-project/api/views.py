from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated ,AllowAny
from django.db.models import Q
from django_filters import rest_framework

class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.OrderingFilter]   # <-- أضف OrderingFilter
    ordering_fields = ['title', 'publication_year']  # <-- الحقول اللي تسمح بالترتيب
    ordering = ['title']  # <-- default ordering (مثلاً بالعنوان)

    def get_queryset(self):
        queryset = Book.objects.all()

        # Manual filters
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        year = self.request.query_params.get('publication_year')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if year:
            queryset = queryset.filter(publication_year=year)

        # Search functionality (title OR author)
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(author__icontains=search)
            )

        return queryset




class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
