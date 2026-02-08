from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = "Cria superuser automaticamente usando variáveis de ambiente"

    def handle(self, *args, **kwargs):
        username = os.getenv("ADMIN_USERNAME")
        email = os.getenv("ADMIN_EMAIL")
        password = os.getenv("ADMIN_PASSWORD")

        if not username or not password:
            self.stdout.write(self.style.WARNING("ADMIN_USERNAME ou ADMIN_PASSWORD não definido"))
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser {username} criado com sucesso"))
        else:
            self.stdout.write(self.style.NOTICE(f"Superuser {username} já existe"))
