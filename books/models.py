from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    title = models.CharField(max_length=254)
    friendly_title = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_friendly_title(self):
        return self.friendly_title


class Book(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
