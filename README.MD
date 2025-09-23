Django Starter Kit
==================

Django Dev Kit is a modular, secure, and production-ready backend starter built for developers who value clarity, speed, and scalability. Perfect for hackathons, prototyping and production pivots. This kit gets you running in seconds—with no frontend dependencies.

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
```bash
sudo apt install default-libmysqlclient-dev build-essential
```
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

# ----- You can now start working! -----

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
🤝 Contributing
------------------------------------------------------------

Feel free to fork, extend this kit, or submit pull requests. This kit is built for backend engineers
who value clarity.
