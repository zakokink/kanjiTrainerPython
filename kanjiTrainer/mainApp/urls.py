from django.urls import path
from . import views

urlpatterns = [
    path("test", views.test, name="test"),
    #path('kanjiById/<int:pk>', views.KanjiListUpdateDestroy.as_view(), name="kanji-user-view"),

    path('kanjis', views.KanjiListCreate.as_view(), name="user-view-create"),
    path('kanjisForUserForLanguage/<int:userId>/<int:languageId>/<int:limit>', views.AllKanjisForUserAndLanguage.as_view(),
         name="kanjis-user-language-view-create"),

    path('kanjisForUserForLanguageOrderByLastStuddied/<int:userId>/<int:languageId>',
         views.AllKanjisForUserAndLanguageOrderByLastStuddied.as_view(),
         name="kanjis-last-studdied-view-create"),

    path('kanjisForUserAndLanguageOrderByLastStuddiedFromId/<int:userId>/<int:languageId>/<int:startingId>',
         views.AllKanjisForUserAndLanguageOrderByLastStuddiedFromId.as_view(),
         name="kanjis-last-studdied-view-startingId"),

    path('kanjisForUserForLanguageOrderByLastNegative/<int:userId>/<int:languageId>',
         views.AllKanjisForUserAndLanguageOrderByLastNegative.as_view(),
         name="kanjis-last-negative-view-create"),

    path('kanjisForUserForLanguageOrderByFailedCount/<int:userId>/<int:languageId>',
         views.AllKanjisForUserAndLanguageOrderByFailedCount.as_view(),
         name="kanjis-failed-count-view-create"),

    path('kanjis/<int:pk>', views.KanjiRetrieveUpdateDestroy.as_view(), name="kanji-update"),

    path('kanjisForUserForLanguageOldFirst/<int:userId>/<int:languageId>',
         views.AllKanjisForUserAndLanguageOldFirst.as_view(),
         name="kanjis-old-first-view-create"),

]

