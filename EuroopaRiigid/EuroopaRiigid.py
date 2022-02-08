from module1 import*
from random import*
from tkinter import*
from tkinter.messagebox import*
sonastik=failist_sõnastikusse()
linnad=[i for i in sonastik.keys()]
pealinnad=[i for i in sonastik.values()]
def opt1():
    for key, value in sonastik.items():
            print(key+"-"+value)
def opt2():
    slovo=input("Введите страну или столицу: ")
    if slovo in linnad:
        print(slovo+"-"+sonastik[slovo])
    elif slovo in pealinnad:
        print(slovo+"-"+linnad[pealinnad.index(slovo)])
    else:
        print(f"Страны или столицы нет в словаре")


#3
#new_word(sonastik)
#4
#slovo = input("Введите страну, с ошибкой в написании: ")
#    if slovo in sonastik:
#        print(f"Страна и ее столица были удалены")
#        del sonastik[slovo]
#        new_word(sonastik)
#    else:
#        print("Такой страны в списке нет")
#5
#    result=0
#    for i in range(10):
#        numbe =randint(1,2)
#        if number==1:
#            result=test(result,linnad,pealinnad)                
#        else:
#            result=test(result,pealinnad,linnad)
#    hind=result*100/10
#    print(f"У тебя {result}/10 баллов")
#    if hind>=90:
#        print("Вы получили 5")
#    elif hind>= 75 and hind <=90:
#        print("Вы получили 4")
#    elif hind>= 50 and hind <=75:
#        print("Вы получили 3")
#    else:
#        print("Вы получили 2")
#6
#    sound()

aken=Tk()
aken.geometry("1000x600")
aken.title("Euroopa riigid")
aken.configure(bg="white")
Button(aken,text="Все страны и столицы",heigh=3,width=20,font="Arial 15",fg="black",bg="#adc1ff",relief="ridge",command=opt1).pack()
Button(aken,text="Поиск стран и столиц",heigh=3,width=20,font="Arial 15",fg="black",bg="#adc1ff",relief="ridge",command=opt2).pack()
Button(aken,text="Новая страна и столица",heigh=3,width=20,font="Arial 15",fg="black",bg="#adc1ff",relief="ridge").pack()
Button(aken,text="Исправление ошибок",heigh=3,width=20,font="Arial 15",fg="black",bg="#adc1ff",relief="ridge").pack()
Button(aken,text="Тест",heigh=3,width=20,font="Arial 15",fg="black",bg="#adc1ff",relief="ridge").pack()
Button(aken,text="Озвучивание",heigh=3,width=20,font="Arial 15",fg="black",bg="#adc1ff",relief="ridge").pack()
alam_aken=Toplevel()
alam_aken.geometry("400x400")
alam_aken.mainloop()
aken.mainloop()




