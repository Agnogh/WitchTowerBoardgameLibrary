from django.db import models
from django.conf import settings
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

    min_players = models.PositiveSmallIntegerField(null=True, blank=True)
    max_players = models.PositiveSmallIntegerField(null=True, blank=True)

    # dureation in minutes for play time
    min_play_time = models.PositiveSmallIntegerField(null=True, blank=True)
    max_play_time = models.PositiveSmallIntegerField(null=True, blank=True)

    age = models.PositiveSmallIntegerField(null=True, blank=True)

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


# review database model
class Review(models.Model):
    game = models.ForeignKey(
        # connected to 'Game' model
        "Game",
        # delete reviews if game deletes
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    user = models.ForeignKey(
        # user model is used
        settings.AUTH_USER_MODEL,
        # if account is deleted, delete comment
        on_delete=models.CASCADE,
        # all reviews from this specif user
        related_name="reviews",
    )
    # for storing rating/score
    rating = models.PositiveSmallIntegerField()
    # stores comment in text
    comment = models.TextField()
    # time & date 1st tidme
    created_at = models.DateTimeField(auto_now_add=True)
    # time & date when something is changed / updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # so only 1 review per customer is allowed
        unique_together = ("game", "user")
        # order so last review added show up first FIFO
        ordering = ["-created_at"]

    def __str__(self):
        # use variable so I get Zombicide - Agnogh - 5/5
        return f"{self.game.title} - {self.user.username} ({self.rating}/5)"
