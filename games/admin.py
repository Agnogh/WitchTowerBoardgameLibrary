from django.contrib import admin

# Register your models here.

from .models import Game
from .models import Category
from .models import Review
from .models import ContactMessage
from .models import Event

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(ContactMessage)
admin.site.register(Event)
