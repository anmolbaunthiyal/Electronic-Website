from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.email


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.CharField(max_length=10)
    img_url = models.CharField(max_length=2083, default='')
    description = models.TextField(default='')
    category = models.CharField(max_length=10, default='')
    date = models.DateField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    amount = models.IntegerField()
    desc = models.TextField(default="")
    date = models.DateField()

    def __str__(self):
        return self.email


class New(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    img_url = models.CharField(max_length=2083, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name



