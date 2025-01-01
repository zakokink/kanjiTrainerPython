from django.contrib import admin

from .models import User, Kanji, Language

admin.site.register(User)
admin.site.register(Kanji)
admin.site.register(Language)

