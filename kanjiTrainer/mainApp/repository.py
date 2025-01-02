from .models import Kanji, Limit

def getAllKanjisForUserAndLanguage(userId, languageId, limit):
    print('getAllKanjisForUserAndLanguage....')
    kanjis = Kanji.objects.filter(user = userId, language = languageId).order_by('-id')[:limit]
    print(len(kanjis))

    if(kanjis == None):
        print('Keine Kanjis gefunden!')
        return None

    return kanjis

def getAllKanjisForUserAndLanguageOrderByLastStuddied(userId, languageId, limit):

    limitFromDb : Limit = Limit.objects.filter(user = userId, language = languageId)

    if(len(limitFromDb) > 0):
        maxItems = limitFromDb[0].maxItems
    else:
        maxItems = limit

    kanjis = Kanji.objects.filter(user = userId, language = languageId).order_by('-lastStuddied').order_by('id')[:maxItems]

    if(kanjis == None):
        return None

    return kanjis

def getAllKanjisForUserAndLanguageOrderByLastNegative(userId, languageId, limit):
    limitFromDb : Limit = Limit.objects.filter(user = userId, language = languageId)

    if(len(limitFromDb) > 0):
        maxItems = limitFromDb[0].maxItems
    else:
        maxItems = limit

    kanjis = Kanji.objects.filter(user = userId, language = languageId).order_by('-lastNegative').order_by('id')[:maxItems]

    if(kanjis == None):
        print('Keine Kanjis gefunden!')
        return None

    return kanjis

def getAllKanjisForUserAndLanguageOrderByFailedCount(userId, languageId, limit):
    limitFromDb : Limit = Limit.objects.filter(user = userId, language = languageId)

    if(len(limitFromDb) > 0):
        maxItems = limitFromDb[0].maxItems
    else:
        maxItems = limit

    kanjis = Kanji.objects.filter(user = userId, language = languageId).order_by('-failedCount').order_by('id')[:maxItems]

    if(kanjis == None):
        print('Keine Kanjis gefunden!')
        return None

    return kanjis