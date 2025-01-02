from django.contrib import admin
from .models import User, Kanji, Language, Limit

admin.site.register(User)
admin.site.register(Kanji)
admin.site.register(Language)
admin.site.register(Limit)
