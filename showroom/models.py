import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)


def brand_path(instance, filename):
    return os.path.join('brand_pics', filename)


def staff_path(instance, filename):
    return os.path.join('staff_profiles', filename)


def car_path(instance, filename):
    return os.path.join('car_pics', filename)

# Create your models here.
# Show Room
# Staff
# Brand
# Model
# Engine
# Feature


class Engine(models.Model):
    engine_number = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.engine_number


class Feature(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Showroom(models.Model):
    name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        print("Showroom created")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=256)
    brand_pic = models.ImageField(upload_to=brand_path)
    showroom = models.ForeignKey(
        Showroom, on_delete=models.CASCADE, related_name='brands')

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=256)
    car_pic = models.ImageField(upload_to=car_path)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='brand')

    feature = models.ManyToManyField(Feature, related_name='feature')

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.ForeignKey(
        CarModel, on_delete=models.CASCADE, related_name='model')
    chasis_number = models.CharField(max_length=100, unique=True)
    engine = models.OneToOneField(
        Engine, on_delete=models.CASCADE, related_name='engine')

    def __str__(self):
        return self.model.name


class Staff(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to=staff_path)
    position = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, unique=True)
    showroom = models.ForeignKey(
        Showroom, on_delete=models.CASCADE, related_name='staff')

    def __str__(self):
        return self.name
