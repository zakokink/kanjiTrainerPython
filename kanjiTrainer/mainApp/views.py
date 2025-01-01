from django.shortcuts import render, HttpResponse
from rest_framework import generics
from rest_framework.response import Response

from .models import Kanji
from .serializers import KanjiSerializer
from .repository import getAllKanjisForUserAndLanguage

def test(request):
    return HttpResponse("Es funktioniert!")


class KanjiListUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kanji.objects.all()
    serializer_class = KanjiSerializer
    lookup_field = "pk"


class KanjiListCreate(generics.ListCreateAPIView):
    queryset = Kanji.objects.all()
    serializer_class = KanjiSerializer


class AllKanjisForUserAndLanguage(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        languageId = kwargs.get('languageId')

        queryset = getAllKanjisForUserAndLanguage(userId, languageId)

        if(queryset == None):
            print("Keine Daten gefunden")
            return Response(data={"status": 404, "data": None})

        serializer_class = KanjiSerializer(queryset, many=True)
        return Response(data={"data": serializer_class.data})


