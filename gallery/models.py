from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class Categories(models.Model):
    name = models.CharField("Category", max_length=250)
    slug = models.SlugField("URL", max_length=250, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolut_url(self):
        return reverse("by_category", kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name


class Images(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField("Image", upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, related_name='gallery')
    moderation = models.BooleanField("Moderation", default=False)
    slug = models.SlugField("URL", max_length=250, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def get_absolut_url(self):
        return reverse("image_detail", kwargs={'ima_slug': self.slug})

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