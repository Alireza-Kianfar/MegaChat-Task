Message API (Django + DRF)


Quick start :

1. Create and activate a virtualenv

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install requirements

```bash
pip install -r requirements.txt
```

3. Prepare the database and run the app

```bash
python manage.py migrate
python manage.py runserver
```

Run tests

```bash
python manage.py test
```

How it works

- API base: `/api/messages/` — standard CRUD routes (list, retrieve, create, update, delete).
- `GET /api/messages/` returns a plain list .
- Each message has a `status` (Draft / Sent / Archived) and `created_at` timestamp.
- Admin site is available at `/admin/`.

Environment

Set these environment variables for production:

- `DJANGO_SECRET_KEY` — keep this secret.
- `DJANGO_DEBUG` — ``True`` for development, ``False`` for production.
- `DJANGO_ALLOWED_HOSTS` — comma-separated hosts for production.

