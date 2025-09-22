Django Starter Kit
==================

A modular, secure, and production-ready Django starter kit designed for rapid backend development. Includes support for MySQL or SQLite, environment-based settings, and essential packages for forms, filtering, email, OAuth, and more.

------------------------------------------------------------
🚀 Getting Started
------------------------------------------------------------

1. Clone the Repository
```bash
    git clone https://github.com/bondo2-hub/django-starter-kit.git
    cd django-starter-kit
```

2. Create a Virtual Environment (Optional)
```bash
    pipenv install
    pipenv shell
```

3. Install Dependencies
```bash
    pipenv install -r requirements.txt
```

- 💡 If you're using WSL and encounter issues with mysqlclient, run:
    sudo apt install default-libmysqlclient-dev build-essential

------------------------------------------------------------
🔐 Setup
------------------------------------------------------------

No manual steps. Just run:

1. Run the script:
```bash
    python bootstrap.py
```
**Your dev kit will auto-configure everything—env file, migrations, and more**

Once it's ready, clean the slate and start fresh:
```bash
    rm -rf .git
    git init
```

# You can now start working!
------------------------------------------------------------
🧱 Switching Between Environments
------------------------------------------------------------

To run your project in different environments (development vs production),
set the DJANGO_SETTINGS_MODULE variable in both wsgi.py and asgi.py:

```bash
    # Example for production
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.production')

    # Example for development
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.development')
```

- ⚠️ **Cloud platforms** (Heroku, Railway, Render, etc.) often set this via environment variables.
Avoid hardcoding assumptions—document clearly and let users configure it per platform.

------------------------------------------------------------
🧪 Included Packages
------------------------------------------------------------
```bash
Django==5.1.3
mysqlclient
django-anymail==12.0
django-cors-headers==4.6.0
django-crispy-forms==2.3
django-debug-toolbar==5.1.0
django-environ==0.12.0
django-filter==24.3
django-formtools==2.5.1
django-oauth-toolkit==3.0.1
django-phonenumber-field==8.0.0
django-storages==1.14.4
```
------------------------------------------------------------
📦 Deployment Notes
------------------------------------------------------------

- Use production.py for hardened settings (HTTPS, logging, secure cookies).
- Configure static and media file serving via Nginx or your cloud provider.
- Always set DEBUG=False in production and define ALLOWED_HOSTS.

------------------------------------------------------------
🧠 Philosophy
------------------------------------------------------------

This starter kit reflects a backend philosophy focused on:

- 🔒 Security-first architecture
- 🧼 Clean, reproducible environments
- 🧩 Modular design for real-world scalability
- 🧠 Developer clarity and onboarding speed

------------------------------------------------------------
🤝 Contributing
------------------------------------------------------------

Feel free to fork, extend, or submit pull requests. This kit is built for backend engineers
who value clarity.

------------------------------------------------------------
📄 License
------------------------------------------------------------

[MIT](https://choosealicense.com/licenses/mit/)