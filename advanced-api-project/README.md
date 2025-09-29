# Book API Endpoints

## List all books
**Endpoint:** `GET /books/`  
**Access:** Public  

## Retrieve a single book
**Endpoint:** `GET /books/<id>/`  
**Access:** Public  

## Create a new book
**Endpoint:** `POST /books/create/`  
**Access:** Authenticated users only  

## Update a book
**Endpoint:** `PUT /books/update/<id>/`  
**Access:** Authenticated users only  

## Delete a book
**Endpoint:** `DELETE /books/delete/<id>/`  
**Access:** Authenticated users only  

---

### Permissions
- `AllowAny`: Used for listing and retrieving books.
- `IsAuthenticated`: Required for creating, updating, and deleting books.
