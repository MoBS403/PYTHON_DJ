from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# ==============================
# FUNÇÃO PARA DATA FORMATADA
# ==============================
def current_time():
    return datetime.now().strftime("%d/%m/%Y")


# ==============================
# MODELS
# ==============================
class Post(models.Model):
    postname = models.CharField(max_length=600)
    category = models.CharField(max_length=600)

    image = models.ImageField(
        upload_to="images/posts/",
        blank=True,
        null=True
    )

    content = models.CharField(max_length=100000)

    time = models.CharField(
        max_length=100,
        default=current_time,
        blank=True
    )

    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.postname


class Comment(models.Model):
    content = models.CharField(max_length=200)

    time = models.CharField(
        max_length=100,
        default=current_time,
        blank=True
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.content[:20]}..."


class Contact(models.Model):
    name = models.CharField(max_length=600)
    email = models.EmailField(max_length=600)
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=10000, blank=True)