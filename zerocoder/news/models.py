from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class News_post(models.Model):
    title = models.CharField("Название страницы", max_length=50)
    short_description = models.CharField("Краткое описание новости", max_length=200)
    text = models.TextField("Новость")
    pub_data = models.DateTimeField("Дата публикации")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
