import tkinter as tk
from tkinter import messagebox as msg
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
    while True:
        global losowe
        losowe = random.randint(1,13)
        if losowe in uzyte: # Jeżeli pytanie zostało już uzyte niech dalej losuje
            continue
        else: # Jeżeli nie to koniec losowania
            break

    uzyte.append(losowe)
    zapomnij_guziki()
    zapytanie_latwy = connect.cursor()
    zapytanie_latwy.execute(f"SELECT obrazek FROM latwy WHERE id = {losowe}")
    zapytanie_wynik = zapytanie_latwy.fetchone()
    zapytanie_wynik_str = str(zapytanie_wynik)
    global zapytanie_wynik_strip
    zapytanie_wynik_strip = zapytanie_wynik_str.strip('(),\'')
    print(zapytanie_wynik_strip)
    odp_a = connect.cursor()
    odp_a.execute(f"SELECT odp_a FROM latwy WHERE id = {losowe}")
    odp_a_wynik = str(odp_a.fetchone())
    global odp_a_strip
    odp_a_strip = odp_a_wynik.strip('(),\'')
    latwy_guzik1.set(odp_a_strip)
    print(odp_a_strip)
    odp_b = connect.cursor()
    odp_b.execute(f"SELECT odp_b FROM latwy WHERE id = {losowe}")
    odp_b_wynik = str(odp_b.fetchone())
    global odp_b_strip
    odp_b_strip = odp_b_wynik.strip('(),\'')
    latwy_guzik2.set(odp_b_strip)
    print(odp_b_strip)
    odp_c = connect.cursor()
    odp_c.execute(f"SELECT odp_c FROM latwy WHERE id = {losowe}")
    odp_c_wynik = str(odp_c.fetchone())
    global odp_c_strip
    odp_c_strip = odp_c_wynik.strip('(),\'')
    latwy_guzik3.set(odp_c_strip)
    print(odp_c_strip)
    odp_d = connect.cursor()
    odp_d.execute(f"SELECT odp_d FROM latwy WHERE id = {losowe}")
    odp_d_wynik = str(odp_d.fetchone())
    global odp_d_strip
    odp_d_strip = odp_d_wynik.strip('(),\'')
    latwy_guzik4.set(odp_d_strip)
    print(odp_d_strip)
    odp_e = connect.cursor()
    odp_e.execute(f"SELECT odp_e FROM latwy WHERE id = {losowe}")
    odp_e_wynik = str(odp_e.fetchone())
    global odp_e_strip
    odp_e_strip = odp_e_wynik.strip('(),\'')
    latwy_guzik5.set(odp_e_strip)
    print(odp_e_strip)
    odp_f = connect.cursor()
    odp_f.execute(f"SELECT odp_f FROM latwy WHERE id = {losowe}")
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
    przycisk1_latwy = tk.Button(root, textvariable=latwy_guzik1,command=lambda: (sprawdzenie_dobrej_odpowiedzi(odp_a_strip, przycisk1_latwy)))
    przycisk1_latwy.pack()
    global przycisk2_latwy
    przycisk2_latwy = tk.Button(root, textvariable=latwy_guzik2, command=lambda: sprawdzenie_dobrej_odpowiedzi(odp_b_strip, przycisk2_latwy))
    przycisk2_latwy.pack()
    global przycisk3_latwy
    przycisk3_latwy = tk.Button(root, textvariable=latwy_guzik3, command=lambda: sprawdzenie_dobrej_odpowiedzi(odp_c_strip, przycisk3_latwy))
    przycisk3_latwy.pack()
    global przycisk4_latwy
    przycisk4_latwy = tk.Button(root, textvariable=latwy_guzik4, command=lambda: sprawdzenie_dobrej_odpowiedzi(odp_d_strip, przycisk4_latwy))
    przycisk4_latwy.pack()
    global przycisk5_latwy
    przycisk5_latwy = tk.Button(root, textvariable=latwy_guzik5, command=lambda: sprawdzenie_dobrej_odpowiedzi(odp_e_strip, przycisk5_latwy))
    przycisk5_latwy.pack()
    global przycisk6_latwy
    przycisk6_latwy = tk.Button(root, textvariable=latwy_guzik6, command=lambda: sprawdzenie_dobrej_odpowiedzi(odp_f_strip, przycisk6_latwy))
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
        if wybrana_odpowiedz != zapytanie_wynik_strip:
            przycisk.config(state="disabled")
        else:
            przycisk.config(state="active")
        dodawanie_bledow_latwe()
        print("źle!")
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
