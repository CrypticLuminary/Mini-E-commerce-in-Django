from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    

class Products(models.Model):
    category = models.ForeignKey(Category, verbose_name=("category"), on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True,max_length=250)
    description = models.TextField(blank=True)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated = models.DateTimeField( auto_now=True)
    image = models.ImageField(upload_to='products', height_field=None, width_field=None,blank=True,null=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"pk": self.pk,"slug":self.slug})
    