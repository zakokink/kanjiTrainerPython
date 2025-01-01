from django.urls import path
from . import views

urlpatterns = [
    path("test", views.test, name="test"),
    path('kanjiById/<int:pk>', views.KanjiListUpdateDestroy.as_view(),
         name="kanji-user-view"),

    path('kanjis', views.KanjiListCreate.as_view(), name="user-view-create"),
    path('kanjisForUserForLanguage/<int:userId>/<int:languageId>', views.AllKanjisForUserAndLanguage.as_view(),
         name="kanjis-user-language-view-create"),

]

