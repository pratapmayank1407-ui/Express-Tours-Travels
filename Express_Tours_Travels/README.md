# Express Tours & Travels

A Django-based tours and travels website for Express Tours & Travels, Lucknow.

## Included
- Responsive travel website
- Home, tours, package detail, about, gallery and contact pages
- Custom trip / booking enquiry form
- Django admin for packages, destinations, enquiries, reviews, gallery and messages
- WhatsApp and phone CTAs
- Google Maps embed using the supplied location coordinates
- Optional email notifications via SMTP
- Render deployment configuration

## Important
Sample destinations and packages are provided as starter content. Replace them with the business's real packages, prices, images and policies through `/admin/`.

## Run locally (Windows)
Use Python 3.11 for this project.

```powershell
cd Express_Tours_Travels
py -3.11 -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Add sample starter content
Run:

```powershell
python manage.py seed_demo
```

This creates starter destinations, packages and a few reviews. All can be edited or deleted in the admin panel.

## Email
By default, Django uses the console email backend locally. Set the SMTP variables in `.env` / Render environment variables to send actual email notifications.

For Gmail, use an App Password rather than your regular account password.

## Production
Set `DEBUG=False`, a strong `SECRET_KEY`, correct `ALLOWED_HOSTS`, and a PostgreSQL `DATABASE_URL`. Run `collectstatic` during deployment.
