from django.db import models

# Create your models here.

class Player(models.Model):
    # id = models.AutoField(primary_key=True)  # Поле id будет автоматически увеличиваться
    first_name = models.CharField(max_length=50)  # Имя игрока
    last_name = models.CharField(max_length=50)  # Фамилия игрока
    email = models.EmailField(unique=True)  # Электронная почта (уникальная)
    phone = models.CharField(max_length=15)  # Телефон (можно использовать CharField для хранения цифр)
    nickname = models.CharField(max_length=50, blank=True)  # Никнейм (необязательное поле)
    rating = models.FloatField(default=0.0)  # Рейтинг (по умолчанию 0.0)
    role = models.IntegerField()  # Роль (целое число)
    club = models.IntegerField()  # Клуб (целое число)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.nickname})"