from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(verbose_name="Название", max_length=50)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    image = models.CharField(verbose_name="Изображение", max_length=100)
    release_date = models.DateField(verbose_name="Релиз")
    lte_exists = models.BooleanField(verbose_name="LTE")
    slug = models.SlugField(verbose_name="URL", max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)
