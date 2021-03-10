from django.contrib.auth.models import User
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


class Tags(models.Model):
    name = models.CharField("Tag", max_length=250)
    slug = models.SlugField("URL", max_length=250, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def get_absolut_url(self):
        return reverse("by_tag", kwargs={'tag_slug': self.slug})

    def __str__(self):
        return self.name


class Recipes(models.Model):
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.SET_NULL, null=True)
    title = models.CharField('Title', max_length=250)
    image = models.ImageField('Image', upload_to='recipes_images/%Y/%m/%d', blank=True, null=True)
    text = models.TextField()
    category = models.ForeignKey(Categories, verbose_name='Category', on_delete=models.PROTECT, related_name='recipe')
    tags = models.ManyToManyField(Tags, verbose_name='Tags', related_name='tags')
    slug = models.SlugField('URL', max_length=250, unique=True, db_index=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def get_absolut_url(self):
        return reverse("recipe_single", kwargs={'rec_slug': self.slug})

    def __str__(self):
        return self.title

    def get_image(self):
        """The function of displaying pictures in the admin panel"""
        if self.image:
            return mark_safe(f'<img src={self.image.url} width="50" height="60">')
        else:
            return '(No found image)'

    get_image.short_description = "Image"
    get_image.allow_tags = True