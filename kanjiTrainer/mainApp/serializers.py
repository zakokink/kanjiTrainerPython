from rest_framework import serializers

from .models import Kanji, User, Language


class KanjiSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=False)
    language = serializers.SerializerMethodField(read_only=False)

    def get_user(self, kanji):
        return UserSerializer(kanji.user, many=False, read_only=False).data

    def get_language(self, kanji):
        return LanguageSerializer(kanji.language, many=False, read_only=False).data

    class Meta:
        model = Kanji
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"