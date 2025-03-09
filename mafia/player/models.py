from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Player(models.Model):
    # id = models.AutoField(primary_key=True)  # Поле id будет автоматически увеличиваться
    first_name = models.CharField(max_length=50)  # Имя игрока
    last_name = models.CharField(max_length=50)  # Фамилия игрока
    email = models.EmailField(unique=True)  # Электронная почта (уникальная)
    phone = models.CharField(max_length=15)  # Телефон (можно использовать CharField для хранения цифр)
    nickname = models.CharField(max_length=50, blank=True)  # Никнейм (необязательное поле)
    rating = models.FloatField(default=0.0)  # Рейтинг (по умолчанию 0.0)
    role = models.IntegerField(default=0)  # Роль (целое число)
    club = models.IntegerField(default=0)  # Клуб (целое число)
    slug = models.SlugField(max_length=255, blank=True, db_index=True, default='', null=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.id}, {self.first_name}, {self.last_name}, {self.email}, {self.phone}, {self.nickname}, {self.rating}, {self.role}, {self.club}"

    def get_absolute_url(self):
        return reverse('player_slug', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:  # Генерируем slug, только если он еще не задан
            self.slug = slugify(f"{self.first_name}-{self.last_name}")
        super().save(*args, **kwargs)