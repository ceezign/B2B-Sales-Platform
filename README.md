# ◆ JiggyTheGreat B2B Sales Platform

A professional Django B2B sales channel for product browsing and quote requests. No customer login required.

---

## Quick Start

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations and create admin user
python manage.py migrate
python manage.py createsuperuser

# 4. Start the server
python manage.py runserver
```

| URL | Description |
|---|---|
| http://127.0.0.1:8000/ | Public product catalogue |
| http://127.0.0.1:8000/product/`<slug>`/ | Product detail + quote form |
| http://127.0.0.1:8000/admin/ | Admin CRM panel |

---

## Email Configuration

Go to `b2b_platform/settings.py` and update this block:

```python
EMAIL_HOST_USER     = os.environ.get('EMAIL_HOST_USER', 'johnrussell0085@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'your-16-char-app-password')
DEFAULT_FROM_EMAIL  = os.environ.get('DEFAULT_FROM_EMAIL', 'B2B Sales <johnrussell0085@gmail.com>')
COMPANY_ADMIN_EMAIL = os.environ.get('COMPANY_ADMIN_EMAIL', 'atundetoheeb1@gmail.com')
COMPANY_NAME        = os.environ.get('COMPANY_NAME', 'JiggyTheGreat Ltd.')
```

**Gmail requires an App Password — your regular password will not work.**

1. Go to https://myaccount.google.com/security → enable **2-Step Verification**
2. Go to https://myaccount.google.com/apppasswords → create one named `Django B2B`
3. Paste the 16-character password (no spaces) into `EMAIL_HOST_PASSWORD`

> To test emails without sending, set `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` — emails print to the terminal instead.

---

## How It Works

```
Admin adds product → Customer browses catalogue → Submits quote form
    → Request saved to DB
    → Email sent to company admin        (notification)
    → Email sent to customer             (confirmation + reference ID)
    → Admin updates status in /admin/
    → Email sent to customer             (status update — automatic via signal)
```

---

## Admin Panel

**Products** — Add, edit, activate/deactivate products. Slug auto-generates from the name.

**Product Requests** — Your internal CRM. Filter by status, search by company or email. Change a request's status and the customer is emailed automatically.

Status options: `Pending` → `Processing` → `Completed` / `Rejected`

---

## Common Errors

**`Username and Password not accepted`**
You're using your Gmail password. Generate an App Password instead — see Email Configuration above.

**`os.environ.get()` not working**
The first argument must be a variable *name*, not the value:
```python
# WRONG
EMAIL_HOST_USER = os.environ.get('johnrussell0085@gmail.com', 'johnrussell0085@gmail.com')

# CORRECT
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'johnrussell0085@gmail.com')
```

**Images not displaying** — Run `pip install Pillow`

**No such table** — Run `python manage.py migrate`

---

## Project Structure

```
b2b_platform/
├── b2b_platform/        # Settings, root URLs
├── sales/               # Models, views, forms, admin, emails, signals
├── templates/
│   ├── base.html
│   ├── sales/           # product_list.html, product_detail.html
│   └── emails/          # 3 email types × HTML + TXT
├── static/css/main.css  # Corporate navy/gold theme
├── media/products/      # Uploaded product images
├── requirements.txt
└── manage.py
```

---

## Production Checklist

- [ ] `DEBUG = False`
- [ ] New strong `SECRET_KEY`
- [ ] `ALLOWED_HOSTS = ['yourdomain.com']`
- [ ] Real environment variables (no hardcoded credentials)
- [ ] Switch to PostgreSQL
- [ ] Run `collectstatic`
- [ ] Gunicorn + Nginx + SSL certificate
