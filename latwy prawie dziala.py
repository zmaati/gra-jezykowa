import tkinter as tk
from tkinter import messagebox as msg
from tkinter import Toplevel
import mysql.connector as baza
import random
from PIL import ImageTk, Image

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
BAZA = 'duolingo'

connect = baza.connect(
    host=HOST,
    user=USER,
    password=PASSWORD, 
    database=BAZA
)



def zapomnij_guziki():
    PoziomLatwy.pack_forget()
    PoziomSredniotrudny.pack_forget()
    PoziomTrudny.pack_forget()
    PoziomSredni.pack_forget()


uzyte = []
def latwy():
    def losowanie():
        global losowe_dobra_odp,losowe_a,losowe_b,losowe_c,losowe_d,losowe_e,losowe_f
        while True:
            losowe_dobra_odp = random.randint(1,13)
            losowe_a = random.randint(1,13)
            losowe_b = random.randint(1,13)
            losowe_c = random.randint(1,13)
            losowe_d = random.randint(1,13)
            losowe_e = random.randint(1,13)
            losowe_f = random.randint(1,13)
            if losowe_dobra_odp == losowe_a or  losowe_dobra_odp == losowe_b or losowe_dobra_odp == losowe_c or losowe_dobra_odp == losowe_d or losowe_dobra_odp == losowe_e or losowe_dobra_odp == losowe_f:
             break

        uzyte.append(losowe_a)
        uzyte.append(losowe_b)
        uzyte.append(losowe_c)
        uzyte.append(losowe_d)
        uzyte.append(losowe_e)
        uzyte.append(losowe_f)
    def usun_uzyte():
        uzyte.clear()
    losowanie()
    zapomnij_guziki()
    poprawny_wynik = connect.cursor()
    poprawny_wynik.execute(f"SELECT obrazek FROM latwy WHERE id = {losowe_dobra_odp}")
    zapytanie_wynik = poprawny_wynik.fetchone()
    zapytanie_wynik_str = str(zapytanie_wynik)
    global zapytanie_wynik_strip
    zapytanie_wynik_strip = zapytanie_wynik_str.strip('(),\'')
    print(zapytanie_wynik_strip)
    odp_a = connect.cursor()
    odp_a.execute(f"SELECT obrazek FROM latwy WHERE id = {losowe_a}")
    odp_a_wynik = str(odp_a.fetchone())
    global odp_a_strip
    odp_a_strip = odp_a_wynik.strip('(),\'')
    latwy_guzik1.set(odp_a_strip)
    print(odp_a_strip)
    odp_b = connect.cursor()
    odp_b.execute(f"SELECT obrazek FROM latwy WHERE id = {losowe_b}")
    odp_b_wynik = str(odp_b.fetchone())
    global odp_b_strip
    odp_b_strip = odp_b_wynik.strip('(),\'')
    latwy_guzik2.set(odp_b_strip)
    print(odp_b_strip)
    odp_c = connect.cursor()
    odp_c.execute(f"SELECT obrazek FROM latwy WHERE id = {losowe_c}")
    odp_c_wynik = str(odp_c.fetchone())
    global odp_c_strip
    odp_c_strip = odp_c_wynik.strip('(),\'')
    latwy_guzik3.set(odp_c_strip)
    print(odp_c_strip)
    odp_d = connect.cursor()
    odp_d.execute(f"SELECT obrazek FROM latwy WHERE id = {losowe_d}")
    odp_d_wynik = str(odp_d.fetchone())
    global odp_d_strip
    odp_d_strip = odp_d_wynik.strip('(),\'')
    latwy_guzik4.set(odp_d_strip)
    print(odp_d_strip)
    odp_e = connect.cursor()
    odp_e.execute(f"SELECT obrazek FROM latwy WHERE id = {losowe_e}")
    odp_e_wynik = str(odp_e.fetchone())
    global odp_e_strip
    odp_e_strip = odp_e_wynik.strip('(),\'')
    latwy_guzik5.set(odp_e_strip)
    print(odp_e_strip)
    odp_f = connect.cursor()
    odp_f.execute(f"SELECT obrazek FROM latwy WHERE id = {losowe_f}")
    odp_f_wynik = str(odp_f.fetchone())
    global odp_f_strip
    odp_f_strip = odp_f_wynik.strip('(),\'')
    latwy_guzik6.set(odp_f_strip)
    print(odp_f_strip)
    image_path = f"Latwy_Zdjecia/{zapytanie_wynik_strip}.gif"




    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    global obrazek_label
    obrazek_label = tk.Label(root, image=photo, width=400, height=400)
    obrazek_label.image = photo  # Keeping a reference
    obrazek_label.pack()
    global przycisk1_latwy
    przycisk1_latwy = tk.Button(root, textvariable=latwy_guzik1,command=lambda: (sprawdzenie_dobrej_odpowiedzi(odp_a_strip, przycisk1_latwy),losowanie,usun_uzyte))
    przycisk1_latwy.pack()
    global przycisk2_latwy
    przycisk2_latwy = tk.Button(root, textvariable=latwy_guzik2, command=lambda: (sprawdzenie_dobrej_odpowiedzi(odp_b_strip, przycisk2_latwy),losowanie,usun_uzyte))
    przycisk2_latwy.pack()
    global przycisk3_latwy
    przycisk3_latwy = tk.Button(root, textvariable=latwy_guzik3, command=lambda: (sprawdzenie_dobrej_odpowiedzi(odp_c_strip, przycisk3_latwy),losowanie,usun_uzyte))
    przycisk3_latwy.pack()
    global przycisk4_latwy
    przycisk4_latwy = tk.Button(root, textvariable=latwy_guzik4, command=lambda: (sprawdzenie_dobrej_odpowiedzi(odp_d_strip, przycisk4_latwy),losowanie,usun_uzyte))
    przycisk4_latwy.pack()
    global przycisk5_latwy
    przycisk5_latwy = tk.Button(root, textvariable=latwy_guzik5, command=lambda: (sprawdzenie_dobrej_odpowiedzi(odp_e_strip, przycisk5_latwy),losowanie,usun_uzyte))
    przycisk5_latwy.pack()
    global przycisk6_latwy
    przycisk6_latwy = tk.Button(root, textvariable=latwy_guzik6, command=lambda: (sprawdzenie_dobrej_odpowiedzi(odp_f_strip, przycisk6_latwy),losowanie,usun_uzyte))
    przycisk6_latwy.pack()


       

elo = 0
def dodawanie_elo():
    global  elo
    elo += 1
    elo_var.set(elo)
bledy_latwe = 0
def dodawanie_bledow_latwe():
    global bledy_latwe
    bledy_latwe +=1
    bledy_latwe_var.set("Błędy: " + str(bledy_latwe))
    if bledy_latwe >4:
        info = msg.showinfo("Koniec", "koniec")
        if info == "ok":
            root.destroy()

def sprawdzenie_dobrej_odpowiedzi(wybrana_odpowiedz, przycisk):
    if zapytanie_wynik_strip == wybrana_odpowiedz:
        dodawanie_elo()
        obrazek_label.pack_forget()
        przycisk1_latwy.pack_forget()
        przycisk2_latwy.pack_forget()
        przycisk3_latwy.pack_forget()
        przycisk4_latwy.pack_forget()
        przycisk5_latwy.pack_forget()
        przycisk6_latwy.pack_forget()
        latwy()
        print("Jest g")
    else:
        if wybrana_odpowiedz == odp_a_strip:
            top = Toplevel()
            top.title("dobra odp")
            a = Image.open(f"Latwy_Zdjecia/{odp_a_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1,width=400,height=400)
            ashowinfo.image = a1
            ashowinfo.pack()
            przycisk1_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_b_strip:
             top = Toplevel()
             top.title("dobra odp")
             a = Image.open(f"Latwy_Zdjecia/{odp_b_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk2_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_c_strip:
             top = Toplevel()
             top.title("dobra odp")
             a = Image.open(f"Latwy_Zdjecia/{odp_c_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk3_latwy.config(state="disabled")     
        elif wybrana_odpowiedz == odp_d_strip:
             top = Toplevel()
             top.title("dobra odp")
             a = Image.open(f"Latwy_Zdjecia/{odp_d_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk4_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_e_strip:
             top = Toplevel()
             top.title("dobra odp")
             a = Image.open(f"Latwy_Zdjecia/{odp_e_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk5_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_f_strip:
             top = Toplevel()
             top.title("dobra odp")
             a = Image.open(f"Latwy_Zdjecia/{odp_f_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk6_latwy.config(state="disabled")
        dodawanie_bledow_latwe()
def sredni():
    zapomnij_guziki()
    przycisk1_sredni = tk.Button(root,text="Potem").pack()
    przycisk2_sredni = tk.Button(root,text="Potem").pack()
    przycisk3_sredni = tk.Button(root,text="Potem").pack()
    przycisk4_sredni = tk.Button(root,text="Potem").pack()
    przycisk5_sredni = tk.Button(root,text="Potem").pack()
    przycisk6_sredni = tk.Button(root,text="Potem").pack()
def srednio_trudny():
    zapomnij_guziki()
    przycisk1_srednio_trudny = tk.Button(root,text="Potem").pack()
    przycisk2_srednio_trudny = tk.Button(root,text="Potem").pack()
    przycisk3_srednio_trudny = tk.Button(root,text="Potem").pack()
    przycisk4_srednio_trudny = tk.Button(root,text="Potem").pack()
    przycisk5_srednio_trudny = tk.Button(root,text="Potem").pack()
    przycisk6_srednio_trudny = tk.Button(root,text="Potem").pack()
def trudny():
    zapomnij_guziki()
    przycisk1_trudny = tk.Button(root,text="Potem").pack()
    przycisk2_trudny = tk.Button(root,text="Potem").pack()
    przycisk3_trudny = tk.Button(root,text="Potem").pack()
    przycisk4_trudny = tk.Button(root,text="Potem").pack()
    przycisk5_trudny = tk.Button(root,text="Potem").pack()
    przycisk6_trudny = tk.Button(root,text="Potem").pack()















root = tk.Tk()
root.title("Duolingo")
root.geometry("900x600")
root.resizable(False, False)

elo_var = tk.IntVar()
bledy_latwe_var = tk.IntVar()
latwy_guzik1 = tk.StringVar()
latwy_guzik2 = tk.StringVar()
latwy_guzik3 = tk.StringVar()
latwy_guzik4 = tk.StringVar()
latwy_guzik5 = tk.StringVar()
latwy_guzik6 = tk.StringVar()

bledy_latwe_var.set("Błędy: 0")
elo_label = tk.Label(root, textvariable=elo_var)
elo_label.pack()
bledy_latwe_label = tk.Label(root, textvariable=bledy_latwe_var)
bledy_latwe_label.pack()
PoziomLatwy = tk.Button(root, text="Poziom Łatwy",command=latwy)
PoziomLatwy.pack()
PoziomSredni = tk.Button(root, text="Poziom Średni",command=sredni)
PoziomSredni.pack()
PoziomSredniotrudny = tk.Button(root, text="Poziom Średnio-trudny",command=srednio_trudny)
PoziomSredniotrudny.pack()
PoziomTrudny = tk.Button(root, text="Poziom Trudny",command=trudny)
PoziomTrudny.pack()


root.mainloop()