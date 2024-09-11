from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    category_name = models.TextField(null=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    # sdfsfsdf
    title = models.CharField(max_length=25)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(to=SubCategory, on_delete=models.CASCADE)
    category_name = models.TextField(null=True)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.title


class Contacts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.title
