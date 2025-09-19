Django Starter Kit
==================

A modular, secure, and production-ready Django starter kit designed for rapid backend development. Includes support for MySQL or SQLite, environment-based settings, and essential packages for forms, filtering, email, OAuth, and more.

------------------------------------------------------------
🚀 Getting Started
------------------------------------------------------------

1. Clone the Repository

    git clone https://github.com/bondo2-hub/django-starter-kit.git
    cd django-starter-kit

2. Create a Virtual Environment (Optional)

    pipenv install
    pipenv shell

3. Install Dependencies

    pip install -r requirements.txt

    💡 If you're using WSL and encounter issues with mysqlclient, run:
    sudo apt install default-libmysqlclient-dev build-essential

------------------------------------------------------------
🔐 Secret Key Setup
------------------------------------------------------------

Every Django project requires a unique SECRET_KEY for cryptographic operations like session signing and CSRF protection.

Steps to Generate Your Secret Key:

1. Run the key generator script:

    cd base/management
    python generate_secret_key.py

    cd base/management
    python3 generate_secret_key.py

2. Copy the output into your .env file:

    SECRET_KEY=your-generated-key-here

⚠️ Important: Never commit your .env file or share your secret key publicly.

------------------------------------------------------------
🧰 Environment Configuration
------------------------------------------------------------

Use the .env file to configure your project:

    # Core settings
    SECRET_KEY=your-generated-key
    DEBUG=False
    ALLOWED_HOSTS=127.0.0.1,localhost

    # Database engine: 'mysql' or 'sqlite'
    DB_ENGINE=mysql

    # MySQL credentials (only needed if DB_ENGINE=mysql)
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=3306

------------------------------------------------------------
🧱 Switching Between Environments
------------------------------------------------------------

To run your project in different environments (development vs production),
set the DJANGO_SETTINGS_MODULE variable in both wsgi.py and asgi.py:

    # Example for production
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.production')

    # Example for development
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.development')

⚠️ Cloud platforms (Heroku, Railway, Render, etc.) often set this via environment variables.
Avoid hardcoding assumptions—document clearly and let users configure it per platform.

------------------------------------------------------------
🧪 Included Packages
------------------------------------------------------------

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

MIT License. See LICENSE file for details.