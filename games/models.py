from django.db import models

# Create your models here.

# CharField - Short text (title, tagline...)
# SlugField - url text
# TextField - Long text (decsriptons)
# Decinal filed - money digits
# PositiveIntegerField - Stcoks
# blank=True - filed is optional


class Game(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    tagline = models.CharField(max_length=255, blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    publisher = models.CharField(max_length=150, blank=True)
    designer = models.CharField(max_length=150, blank=True)

    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,  # to unset category
        null=True,  # allow to store "nothing" so category is not mandatory
        blank=True,  # filed can be empty
        related_name="games",  # access games using category
    )
    sku = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # first time ading
    updated_at = models.DateTimeField(auto_now=True)  # changes and renewal

    def __str__(self):
        return self.title


class Category(models.Model):
    # shouldn't exceeed 80 characters
    name = models.CharField(max_length=80)
    # no repetition
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
