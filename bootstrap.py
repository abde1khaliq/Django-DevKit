import subprocess
import secrets
import os

PROJECT_NAME = 'django_devkit'
ENV_FILE = '.env'

def run(cmd, shell=True):
    print(f"▶️ Running: {''.join(cmd) if isinstance(cmd, list) else cmd}")
    subprocess.run(cmd, shell=shell, check=True)

def generate_env():
    if not os.path.exists(ENV_FILE):
        django_secret_key = secrets.token_urlsafe(50)
        with open(ENV_FILE, 'w') as file:
            file.write(f"# Database engine: 'mysql' or 'sqlite'\n")
            file.write(f'DB_ENGINE=sqlite\n')
            file.write(f'# MySQL credentials (only needed if DB_ENGINE=mysql)\n')
            file.write(f'DB_NAME=your_db_name\n')
            file.write(f'DB_USER=your_db_user\n')
            file.write(f'DB_PASSWORD=your_db_password\n')
            file.write(f'DB_HOST=localhost\n')
            file.write(f'DB_PORT=3306\n')
            file.write(f'# Django settings\n')
            file.write(f'SECRET_KEY={django_secret_key}\n')
            file.write(f'DEBUG=True\n')
            file.write(f'ALLOWED_HOSTS=127.0.0.1,localhost\n')
        print(f'✅ Generated {ENV_FILE}')

def run_migrations():
    run(['manage.py', 'makemigrations'])
    run(['manage.py', 'migrate'])

def main():
    print(f"🚀 Bootstrapping {PROJECT_NAME}...")
    generate_env()
    run_migrations()
    print("✅ Setup complete. You can now run the server using: python manage.py runserver")

if __name__ == "__main__":
    main()