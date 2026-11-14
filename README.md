# Simple E-commerce Store (Django)

A beginner-friendly e-commerce project built with Django, HTML, CSS and JavaScript.

## Features
- Product listing and product details
- Search products
- Session-based shopping cart (add, update quantity, remove)
- User registration, login and logout
- Checkout and order creation
- Order history for logged-in users
- Django admin for managing products and orders
- SQLite database (created automatically by migrations)

## Requirements
- Python 3.10 or newer
- Internet connection for the first-time Django installation

## Run on Windows (PowerShell)

1. Extract the ZIP file.
2. Open PowerShell in the extracted `simple_ecommerce_store` folder (the folder containing `manage.py`).
3. Create and activate a virtual environment:

   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

4. Install Django:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Create the database tables:

   ```powershell
   python manage.py migrate
   ```

6. Add sample products:

   ```powershell
   python manage.py seed_products
   ```

7. (Optional) Create an admin account:

   ```powershell
   python manage.py createsuperuser
   ```

8. Start the website:

   ```powershell
   python manage.py runserver
   ```

9. Open http://127.0.0.1:8000/ in your browser.
   Admin panel: http://127.0.0.1:8000/admin/

## Project structure

```text
simple_ecommerce_store/
├── manage.py
├── requirements.txt
├── README.md
├── store_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── shop/
    ├── migrations/
    ├── management/commands/seed_products.py
    ├── templates/shop/
    ├── static/shop/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── admin.py
```

## Notes
- This is an educational/demo project. Checkout creates an order record but does not collect real payments.
- Product images use remote placeholder URLs. Replace them with your own images if desired.
- Change `SECRET_KEY` and set `DEBUG = False` before deploying publicly.
