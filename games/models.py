from django.db import models
from django.conf import settings
# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator

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
    # bug fix to prevent values going below 1 and over 5
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
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


# contact model
class ContactMessage(models.Model):
    # drop down options liszt
    TOPIC_CHOICES = [
        ("lending", "Lending"),
        ("event", "Events"),
        ("general", "General"),
        ("other", "Other"),
    ]

    # connect messag to loogged in account
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contact_messages",
    )
    # this is for type of messahe / query it will be
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    # actual text in message
    message = models.TextField()
    # creation time
    created_at = models.DateTimeField(auto_now_add=True)
    # if it was actiond by admin or not (like checklist)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        # last messages shows first
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.get_topic_display()}"


# EVENT MODEL
class Event(models.Model):
    # Event name (200 is excesive, but I want to be sure about any UI issues)
    title = models.CharField(max_length=200)
    # game that will be played (100 char is more than enough)
    # PLAIN TEXT for now -> link to actual game later
    game_name = models.CharField(max_length=100, blank=True)
    # calendar date
    event_date = models.DateField()
    # time
    event_time = models.TimeField()
    # description (no limites)
    description = models.TextField(blank=True)
    # Can be left blank but to have 'rewards' filed
    reward = models.CharField(max_length=255, blank=True)
    # wehn was event created saved in admin (MAYBE REMOVE LATER)
    created_at = models.DateTimeField(auto_now_add=True)
    # simple activity confirmation so that event can be made in advance
    # but set as 'active' when ready
    is_active = models.BooleanField(default=True)

    # in case of 2 events,m order is by date
    class Meta:
        ordering = ["event_date", "event_time"]

    # appearance in Django
    def __str__(self):
        return f"{self.title} - {self.event_date}"
