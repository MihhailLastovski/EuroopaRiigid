from random import*
import os
import gtts
from playsound import playsound
def failist_sõnastikusse():
    sonastik={}
    file = open("Euroopa_riigid.txt","r")
    for line in file:
        linn,pealinn=line.strip().split(":")
        sonastik[linn.strip()]=pealinn.strip()
    file.close()
    return sonastik

def new_word(sonastik):
    slovo=input("Введите страну, которую хотите добавить: ")
    slovo2=input("Введите столицу, которую хотите добавить: ")
    with open("Euroopa_riigid.txt","a") as fail:
        fail.write(slovo+":"+slovo2+"\n")
    sonastik[slovo]=slovo2
    print(f'Страна "{slovo}" и её столица "{slovo2}" добавлены')

def test(result,l,l2):
    slovo=choice(l)
    otvet=input(f"{slovo}: ")
    if otvet in l2: 
        if l2.index(otvet)==l.index(slovo):
            result+=1
            print("Правильно")
    else:
        print("Неправильно")
    return result

def sound():
    """Функция для озвучивания текста, введенного пользователем (работает один раз, потом появляется ошибка)
    """
    print("На каком языке будет озвучка слова? rus/eng")
    valik=input("")
    if valik=="rus":
        text=input("Введите слово для озвучки на русском: ")
        tts=gtts.gTTS(text, lang="ru")
        tts.save("sound_.mp3")
        playsound("sound_.mp3")
    elif valik=="eng":
        text=input("Введите слово для озвучки на английском: ")
        tts=gtts.gTTS(text, lang="en")
        tts.save("wordsound.mp3")
        playsound("wordsound.mp3")
    else:
        print("Вы ввели неправильно")
