# StyleOdds

StyleOdds is a modern Django-based web application for fashion e-commerce, featuring user authentication, product browsing, shopping cart, checkout, and profile management. The project is designed to be easily extensible and a great starting point for learning or building your own online store.

## 🌟 Features

- User registration, login, and profile management
- Product catalog and detailed product views
- Shopping cart and checkout flow
- Stripe integration for payments
- Admin dashboard
- Responsive design with Tailwind CSS
- Clean, modular Django app structure

## 🗂️ Folder Structure

```
styleodds/
│
├── accounts/              # User authentication, profiles, and related templates
│   ├── templates/
│   │   └── accounts/      # login, signup, profile views, etc.
│   │   └── admin/         # admin dashboard template
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── styleodds/             # Main Django project settings and URLs
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── theme/                 # Tailwind CSS integration and theme templates
│   ├── static/
│   ├── static_src/
│   ├── templates/
│   └── ...
│
├── static/                # Static assets (CSS, images, product images)
│   ├── images/
│   ├── vintage_collection/
│   └── style.css
│
├── media/                 # Uploaded media (profile pictures, etc.)
│
├── templates/             # Global templates (home, shop, cart, etc.)
│
├── manage.py
├── requirements.txt
└── README.md
```

---

Let me know if you want to customize any section or add more details!

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** Django Templates, Tailwind CSS
- **Database:** SQLite (default, can be swapped for MySQL/PostgreSQL)
- **Authentication:** Django built-in auth
- **Payments:** Stripe
- **Other:** Pillow, python-dotenv, WhiteNoise, django-tailwind, django-crispy-forms, django-browser-reload

## 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/styleodds.git
   cd styleodds
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables (see `.env.example` for reference).

4. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. For Tailwind CSS, see the `theme/` app for setup instructions.

## 🤝 Contributing

Feel free to **fork** this repository and enhance your skills!  
Pull requests are welcome. If you have ideas for new features or improvements, open an issue or submit a PR.

---

**Happy coding and stay stylish!**
