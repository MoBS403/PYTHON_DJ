import os
import django
from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from django.contrib.auth.models import User

# Lê as credenciais do .env
USERNAME = config("ADMIN_USERNAME", default="admin")
EMAIL = config("ADMIN_EMAIL", default="admin@meudominio.com")
PASSWORD = config("ADMIN_PASSWORD", default="SenhaForte123")

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print(f"Superusuário '{USERNAME}' criado com sucesso!")
else:
    print(f"Superusuário '{USERNAME}' já existe.")
