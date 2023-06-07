from django.db import models
from django.urls import reverse



class Ring(models.Model):
    titleRing = models.CharField('Название', max_length=50)
    metalRing = models.TextField('Материал')
    priceRing = models.IntegerField('Цена')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.titleRing

    def get_absolute_url(self):
        return reverse('post_ring', kwargs={'ring_id': self.pk})

    class Meta:
        verbose_name = 'Кольца'
        ordering = ['titleRing']


class Medallion(models.Model):
    titleMedallion = models.CharField('Название', max_length=50)
    metalMedallion = models.TextField('Материал')
    priceMedallion = models.IntegerField('Цена')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.titleMedallion

    def get_absolute_url(self):
        return reverse('post_medallion', kwargs={'medallion_id': self.pk})

    class Meta:
        verbose_name = 'Медальоны'
        ordering = ['titleMedallion']


class Earrings(models.Model):
    titleEarrings = models.CharField('Название', max_length=50)
    metalEarrings = models.TextField('Материал')
    priceEarrings = models.IntegerField('Цена')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.titleEarrings

    def get_absolute_url(self):
        return reverse('post_earring', kwargs={'earrings_id': self.pk})

    class Meta:
        verbose_name = 'Серьги'
        ordering = ['titleEarrings']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

