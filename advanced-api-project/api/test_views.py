from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()

        # Authenticated client
        self.client.login(username="testuser", password="password123")

        # Create some book objects
        self.book1 = Book.objects.create(title="Django for Beginners", author="William", publication_year=2020)
        self.book2 = Book.objects.create(title="Python Tricks", author="Dan", publication_year=2019)

    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse("book-detail", kwargs={"pk": self.book1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django for Beginners")

    def test_create_book_authenticated(self):
        url = reverse("book-create")
        data = {"title": "New Book", "author": "Author Test", "publication_year": 2021}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        client = APIClient()
        url = reverse("book-create")
        data = {"title": "Fail Book", "author": "Nobody", "publication_year": 2022}
        response = client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book(self):
        url = reverse("book-update", kwargs={"pk": self.book1.id})
        data = {"title": "Updated Django", "author": "William", "publication_year": 2020}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django")

    def test_delete_book(self):
        url = reverse("book-delete", kwargs={"pk": self.book2.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_filter_books_by_author(self):
        url = reverse("book-list") + "?author=Dan"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Dan")

    def test_search_books(self):
        url = reverse("book-list") + "?search=Django"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Django for Beginners")

    def test_order_books_by_year(self):
        url = reverse("book-list") + "?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))

