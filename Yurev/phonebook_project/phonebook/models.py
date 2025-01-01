from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")

    def __str__(self):
        return f"{self.name} ({self.phone_number})"
