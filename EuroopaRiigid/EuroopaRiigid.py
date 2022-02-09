from module1 import*
from random import*
from tkinter import*
from tkinter.messagebox import*
sonastik=failist_sõnastikusse()
linnad=[i for i in sonastik.keys()]
pealinnad=[i for i in sonastik.values()]
global slovo,slovo2,slovo3
def create_window(): 
       global window
       window = Toplevel()
       window.geometry("400x250")
def opt1(): #Показывает в консоли
    for key, value in sonastik.items():
            print(key+"-"+value)
def opt2():
    global txt,lbl2,b1
    create_window()
    lbl=Label(window,text="Введите страну или столицу",heigh=1,width=30,font="Arial 14",fg="black",relief="ridge")
    lbl.place(x=2, y=2, relx=0.075, rely=0.04)
    txt=Entry(window,width=25,font="Arial 14",fg="black",bg="lightblue")
    txt.place(x=2, y=2, relx=0.05, rely=0.39)
    b1=Button(window,text="ПОИСК",width=6,font="Arial 14",fg="black",bg="peach puff",relief="ridge",command=lambda:foropt2())
    b1.place(x=2, y=2, relx=0.78, rely=0.36)
    lbl2=Label(window,text="Введите страну или столицу",heigh=2,width=30,font="Arial 15",fg="black",relief="ridge")
    lbl2.place(x=2, y=2, relx=0.075, rely=0.75)
def foropt2():
    slovo=str(txt.get())
    if slovo in linnad:
        lbl2.configure(text=slovo+"-"+sonastik[slovo])
    elif slovo in pealinnad:
        lbl2.configure(text=slovo+"-"+linnad[pealinnad.index(slovo)])
    else:
        lbl2.configure(text="Страны или столицы нет в словаре")
def opt3():
    global lbl4,b2,txt2,txt3
    create_window()
    lbl3=Label(window,text="Новая страна и столица",heigh=1,width=30,font="Arial 14",fg="black",relief="ridge")
    lbl3.place(x=2, y=2, relx=0.075, rely=0.04)
    lblstran=Label(window,text="страна",heigh=1,width=6,font="Arial 10",fg="black",relief="ridge")
    lblstran.place(x=2, y=2, relx=0.05, rely=0.39)
    txt2=Entry(window,width=10,font="Arial 10",fg="black",bg="lightblue")
    txt2.place(x=2, y=2, relx=0.21, rely=0.39)
    lblstol=Label(window,text="столица",heigh=1,width=6,font="Arial 10",fg="black",relief="ridge")
    lblstol.place(x=2, y=2, relx=0.42, rely=0.39)
    txt3=Entry(window,width=10,font="Arial 10",fg="black",bg="lightblue")
    txt3.place(x=2, y=2, relx=0.58, rely=0.39)
    b2=Button(window,text="ДОБАВИТЬ",width=9,font="Arial 10",fg="black",bg="peach puff",relief="ridge",command=lambda:foropt3())
    b2.place(x=2, y=2, relx=0.78, rely=0.37)
    lbl4=Label(window,text="Введите страну и столицу",heigh=2,width=42,font="Arial 11",fg="black",relief="ridge")
    lbl4.place(x=2, y=2, relx=0.015, rely=0.75)
def foropt3():
    slovo2=str(txt2.get())
    slovo3=str(txt3.get())
    with open("Euroopa_riigid.txt","a") as fail:
        fail.write(slovo2+":"+slovo3+"\n")
    sonastik[slovo2]=slovo3
    lbl4.configure(text=f'Страна "{slovo2}" и столица "{slovo3}" добавлены')
# opt4 не доделано. Пока что только удаляет страну и столицу, но не изменяет
def opt4():
    create_window()
    lbl5=Label(window,text="Введите страну с ошибкой",heigh=1,width=30,font="Arial 14",fg="black",relief="ridge")
    lbl5.place(x=2, y=2, relx=0.075, rely=0.04)
    txt4=Entry(window,width=35,font="Arial 12",fg="black",bg="lightblue")
    txt4.place(x=2, y=2, relx=0.01, rely=0.39)
    b2=Button(window,text="ИЗМЕНИТЬ",width=9,font="Arial 10",fg="black",bg="peach puff",relief="ridge",command=lambda:foropt4())
    b2.place(x=2, y=2, relx=0.78, rely=0.37)
    lbl6=Label(window,text="...",heigh=2,width=42,font="Arial 11",fg="black",relief="ridge")
    lbl6.place(x=2, y=2, relx=0.015, rely=0.75)
    def foropt4():
        slovo=str(txt4.get())
        if slovo in sonastik:
            lbl6.configure(text=f"Страна и столица были удалены")
            del sonastik[slovo]
        else:
            lbl6.configure(text="Такой страны в списке нет")  
# opt5 возникли трудности с переносом в интерфейс, поэтому пока что только в консоли работает
def opt5():
    result=0
    for i in range(10):
        number=randint(1,2)
        if number==1:
            result=test(result,linnad,pealinnad)                
        else:
            result=test(result,pealinnad,linnad)
    hind=result*100/10
    print(f"У тебя {result}/10 баллов")
    if hind>=90:
        print("Вы получили 5")
    elif hind>= 75 and hind <=90:
        print("Вы получили 4")
    elif hind>= 50 and hind <=75:
        print("Вы получили 3")
    else:
        print("Вы получили 2")
# opt6 возникли трудности с переносом в интерфейс(только в консоли работает) и сама функция работает плохо, один раз срабатывает, а потом надо удалять файл. И еще ошибки начали появляться
def opt6():    
    sound()

aken=Tk()
aken.geometry("1000x600")
aken.title("Euroopa riigid")
aken.configure(bg="white")
Button(aken,text="Все страны и столицы",heigh=3,width=20,font="Arial 15",fg="black",bg="#adc1ff",relief="ridge",command=opt1).pack()
Button(aken,text="Поиск стран и столиц",heigh=3,width=20,font="Arial 15",fg="black",bg="#adc1ff",relief="ridge",command=lambda:opt2()).pack()
Button(aken,text="Новая страна и столица",heigh=3,width=20,font="Arial 15",fg="black",bg="#adc1ff",relief="ridge",command=lambda:opt3()).pack()
Button(aken,text="Исправление ошибок",heigh=3,width=20,font="Arial 15",fg="black",bg="#adc1ff",relief="ridge",command=lambda:opt4()).pack()
Button(aken,text="Тест",heigh=3,width=20,font="Arial 15",fg="black",bg="#adc1ff",relief="ridge",command=lambda:opt5()).pack()
Button(aken,text="Озвучивание",heigh=3,width=20,font="Arial 15",fg="black",bg="#adc1ff",relief="ridge",command=lambda:opt6()).pack()
aken.mainloop()




