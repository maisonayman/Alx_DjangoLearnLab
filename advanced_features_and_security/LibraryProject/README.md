# Advanced Features and Security

## Task 1: Permissions and Groups Setup

This project utilizes Django's groups and permissions system to manage access control for the `bookshelf` application.

### Groups Configuration

The following groups are intended to be set up in the Django Admin panel:

-   **Viewers**: Assigned the `can_view_book` permission. Can only see the list of books.
-   **Editors**: Assigned `can_view_book`, `can_create_book`, and `can_edit_book` permissions. Can manage book entries but cannot delete them.
-   **Admins**: Assigned all custom book permissions, giving them full control.

### Custom Permissions

The `bookshelf.Book` model defines the following custom permissions in its `Meta` class:

-   `can_view_book`
-   `can_create_book`
-   `can_edit_book`
-   `can_delete_book`

### View Enforcement


## Task 3: Security Review and HTTPS Enforcement

This section details the measures implemented to secure the application for production, focusing on secure communication.

### HTTPS and HSTS Enforcement
The application is configured to enforce HTTPS across the entire site. In `settings.py`, `SECURE_SSL_REDIRECT` is set to `True` for production, ensuring any HTTP requests are redirected to HTTPS.

Furthermore, HTTP Strict Transport Security (HSTS) is enabled with `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, and `SECURE_HSTS_PRELOAD`. This instructs browsers to communicate with our site exclusively over HTTPS for a specified duration, mitigating man-in-the-middle (MITM) attacks.

### Secure Cookies
Both `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` are set to `True`. This guarantees that these sensitive cookies are only ever transmitted over an encrypted HTTPS connection, preventing session hijacking over insecure networks like public Wi-Fi.

### Additional Security Headers
To further harden the application against common attacks, the following headers are implemented:
-   **`X_FRAME_OPTIONS = 'DENY'`**: Protects against clickjacking by preventing the site from being loaded in an `<iframe>`.
-   **`SECURE_CONTENT_TYPE_NOSNIFF`**: Prevents the browser from trying to guess the content type of a file, which can mitigate certain XSS attack vectors.
-   **`SECURE_BROWSER_XSS_FILTER`**: Enables the browser's built-in cross-site scripting filter.

### Areas for Improvement
While these settings provide a strong security baseline, future improvements could include:
-   Storing all secret keys and sensitive information in environment variables instead of the `settings.py` file.
-   Implementing a more restrictive Content Security Policy (CSP).
-   Regularly updating all dependencies to patch known vulnerabilities.