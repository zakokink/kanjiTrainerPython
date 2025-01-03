from django.shortcuts import render, HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Kanji
from .serializers import KanjiSerializer
from .repository import getAllKanjisForUserAndLanguage, getAllKanjisForUserAndLanguageOrderByLastStuddied, \
    getAllKanjisForUserAndLanguageOrderByLastNegative, getAllKanjisForUserAndLanguageOrderByFailedCount

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
        limit = kwargs.get('limit')

        queryset = getAllKanjisForUserAndLanguage(userId, languageId, limit)

        if(queryset == None):
            print("Keine Daten gefunden")
            return Response(data={"status": 404, "data": None})

        serializer_class = KanjiSerializer(queryset, many=True)
        return Response(data={"data": serializer_class.data})

class AllKanjisForUserAndLanguageOrderByLastStuddied(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        languageId = kwargs.get('languageId')
        limit = kwargs.get('limit')

        queryset = getAllKanjisForUserAndLanguageOrderByLastStuddied(userId, languageId, limit)

        if(queryset == None):
            print("Keine Daten gefunden")
            return Response(data={"status": 404, "data": None})

        serializer_class = KanjiSerializer(queryset, many=True)
        return Response(data={"data": serializer_class.data})

class AllKanjisForUserAndLanguageOrderByLastNegative(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        languageId = kwargs.get('languageId')
        limit = kwargs.get('limit')

        queryset = getAllKanjisForUserAndLanguageOrderByLastNegative(userId, languageId, limit)

        if(queryset == None):
            print("Keine Daten gefunden")
            return Response(data={"status": 404, "data": None})

        serializer_class = KanjiSerializer(queryset, many=True)
        return Response(data={"data": serializer_class.data})

class AllKanjisForUserAndLanguageOrderByFailedCount(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        languageId = kwargs.get('languageId')
        limit = kwargs.get('limit')

        queryset = getAllKanjisForUserAndLanguageOrderByFailedCount(userId, languageId, limit)

        if(queryset == None):
            print("Keine Daten gefunden")
            return Response(data={"status": 404, "data": None})

        serializer_class = KanjiSerializer(queryset, many=True)
        return Response(data={"data": serializer_class.data})

class KanjiRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kanji.objects.all()
    serializer_class = KanjiSerializer
    lookup_field = "pk"


