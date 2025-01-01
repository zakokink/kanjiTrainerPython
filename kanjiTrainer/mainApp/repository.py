from .models import Kanji

def getAllKanjisForUserAndLanguage(userId, languageId):
    print('getAllKanjisForUserAndLanguage....')
    kanjis = Kanji.objects.filter(user = userId, language = languageId)
    print(len(kanjis))

    if(kanjis == None):
        print('Keine Kanjis gefunden!')
        return None

    #trainingWithMaxForUebung = Training.objects.filter(date = str(maxDate), uebung = uebungId, user = userId)
    return kanjis
