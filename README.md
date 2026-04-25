# Mini Shop (Django E-commerce)

Mini Shop is a Django-based e-commerce project with product browsing, category filtering, search, session-based cart management, and user authentication.

## Features

- Product catalog with category support
- Product search by name, description, and category
- Product detail pages with stock status and optional images
- Session-based shopping cart (add, update quantity, remove)
- Cart item count in global navigation
- User signup, login, logout, and account page
- Django admin for managing categories and products
- Seeded categories and sample products via migrations

## Tech Stack

- Python
- Django 6.0.2
- SQLite (default database)
- Pillow (for image handling)
- HTML templates + custom CSS

## Project Structure

```text
ecommerce/
|-- accounts/      # authentication views/forms/urls
|-- cart/          # session cart logic and context processor
|-- core/          # home page
|-- products/      # catalog models/views/urls/admin
|-- config/        # Django settings and root URLs
|-- templates/     # shared and page templates
|-- static/        # CSS assets
|-- media/         # uploaded product images (runtime)
|-- manage.py
|-- requirements.txt
```

## Quick Start

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run migrations

```bash
python manage.py migrate
```

This applies migrations and seeds initial categories/products from `products/migrations/0002_seed_categories_and_products.py`.

### 4. (Optional) Create an admin user

```bash
python manage.py createsuperuser
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Demo Data

The project automatically seeds demo categories and products during migration.

No manual setup is required to see products.



## Main Routes

- `/` home page
- `/products/` product listing
- `/products/<slug>/` product detail
- `/cart/` cart page
- `/accounts/signup/` signup
- `/accounts/login/` login
- `/accounts/logout/` logout
- `/accounts/account/` account page
- `/admin/` Django admin

## Useful Commands

```bash
python manage.py test
python manage.py makemigrations
python manage.py migrate
```

## Notes

- `DEBUG=True` and a development `SECRET_KEY` are currently set in `config/settings.py`.
- Static files are served from `static/` during development.
- Media uploads are stored in `media/` and served in debug mode.

