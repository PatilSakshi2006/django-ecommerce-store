# ShopEase – E-commerce Website

A full-stack e-commerce web application developed using Django, Python, HTML, CSS, and JavaScript. ShopEase allows users to browse products, manage their shopping cart, place orders, and view their order history.

## Live Demo

**Website:** https://django-ecommerce-store-fnqw.onrender.com/

## Features

- Product listing and product details
- Product search functionality
- Session-based shopping cart
- Add, update, and remove cart items
- User registration, login, and logout
- Checkout and order placement
- Order history for registered users
- Django admin panel for managing products and orders
- Responsive user interface
- Database integration

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML5 | Website structure |
| CSS3 | Styling and layout |
| JavaScript | Frontend interactions |
| SQLite | Local development database |
| PostgreSQL | Production database |
| Git & GitHub | Version control and source code management |
| Render | Website deployment |

## Project Structure

```text
simple_ecommerce_store/
├── manage.py
├── requirements.txt
├── README.md
├── store_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── shop/
    ├── migrations/
    ├── management/
    │   └── commands/
    │       └── seed_products.py
    ├── templates/shop/
    ├── static/shop/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── admin.py
```

## Installation and Setup

### Requirements

- Python 3.10 or newer
- Git
- Internet connection

### Run Locally on Windows

1. Clone the repository:

```bash
git clone https://github.com/PatilSakshi2006/django-ecommerce-store.git
```

2. Open the project folder:

```bash
cd django-ecommerce-store
```

3. Create a virtual environment:

```powershell
py -m venv venv
```

4. Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

5. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

6. Apply database migrations:

```bash
python manage.py migrate
```

7. Add sample products:

```bash
python manage.py seed_products
```

8. Create an admin account (optional):

```bash
python manage.py createsuperuser
```

9. Start the development server:

```bash
python manage.py runserver
```

10. Open the website:

http://127.0.0.1:8000/

**Admin Panel:** http://127.0.0.1:8000/admin/

## Deployment

The application is deployed using Render.

- Web service: Render
- Production database: PostgreSQL
- Static files: WhiteNoise
- Application server: Gunicorn

## Important Notes

- This is an educational project developed for learning and practical experience.
- Checkout creates an order record but does not process real payments.
- Product images are loaded using external image URLs.
- Never upload secret keys, database credentials, or environment variables to a public repository.
