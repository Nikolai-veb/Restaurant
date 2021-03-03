from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from PIL import Image


class Categories(models.Model):
    name = models.CharField('Category', max_length=250)
    slug = models.SlugField('URL', max_length=300, unique=True, db_index=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse('by_category', kwargs={"cat_slug": self.slug})

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField('Status', max_length=250)
    slug = models.SlugField('URL', max_length=300, unique=True, db_index=True)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def get_absolute_url(self):
        return reverse('by_status', kwargs={"stat_slug": self.slug})

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField("Product", max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField("Image", upload_to="products/%Y/%m/%d/", blank=True, null=True)
    description = models.TextField("Description", )
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, null=True, related_name="product")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True, related_name="product")
    slug = models.SlugField('URL', max_length=300, unique=True, db_index=True)
    moderation = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["create"]

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"prod_slug": self.slug})

    def __str__(self):
        return self.name

    def get_image(self):
        """The function of displaying pictures in the admin panel"""
        if self.image:
            return mark_safe(f'<img src={self.image.url} width="50" height="60">')
        else:
            return '(No found image)'

    get_image.short_description = "Image"
    get_image.allow_tags = True
