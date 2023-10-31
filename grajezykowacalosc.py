import random
import tkinter as tk
from tkinter import messagebox as msg, Toplevel

import mysql.connector as baza
from PIL import ImageTk, Image

import bazadanych





connect = baza.connect(
    host=bazadanych.HOST,
    user=bazadanych.USER,
    password=bazadanych.PASSWORD,
    database=bazadanych.BAZA
)

def schowaj_latwy():
    bledy_latwe_label.place_forget()
    obrazek_label.place_forget()
    przycisk1_latwy.place_forget()
    przycisk2_latwy.place_forget()
    przycisk3_latwy.place_forget()
    przycisk4_latwy.place_forget()
    przycisk5_latwy.place_forget()
    przycisk6_latwy.place_forget()
    start()
def schowaj_sredni():
    bledy_srednie_label.place_forget()
    odp_label.place_forget()
    przycisk1_sredni.place_forget()
    przycisk2_sredni.place_forget()
    przycisk3_sredni.place_forget()
    przycisk4_sredni.place_forget()
    przycisk5_sredni.place_forget()
    przycisk6_sredni.place_forget()
    przycisk7_sredni.place_forget()
    przycisk8_sredni.place_forget()
    start()
def schowaj_st():
    bledy_st_label.place_forget()
    polskie.place_forget()
    angielskie.place_forget()
    dobre_samo_tekst.place_forget()
    dobre_samo.place_forget()
    zle_samo_tekst.place_forget()
    zle_samo.place_forget()
    samogloska_entry.place_forget()
    samogloska_guzik.place_forget()
    start()
def schowaj_trudne():
    bledy_trudne_label.place_forget()
    polish_label.place_forget()
    input_label.place_forget()
    zatwierdz.place_forget()
    wprowadzona_odpowiedz.place_forget()
    start()

def start():
    PoziomLatwy.grid(row=1, column=1, padx=130, pady=150)
    PoziomSredni.grid(row=1, column=2)
    PoziomSredniotrudny.grid(row=2, column=2)
    PoziomTrudny.grid(row=2, column=1)

elo = 0
ogolny_punkty = 0
def dodawanie_elo():
    global elo, ogolny_punkty
    elo += 1
    elo_var.set(elo)
    ogolny_punkty += 1
    ogolne_punkty_var.set("Ogolne punkty: " + str(ogolny_punkty))





bledy = 0

def dodawanie_bledow(TRYB):
    global bledy
    bledy += 1
    TRYB.set("Błędy: " + str(bledy))




def zapomnij_guziki():
    PoziomLatwy.grid_forget()
    PoziomSredniotrudny.grid_forget()
    PoziomTrudny.grid_forget()
    PoziomSredni.grid_forget()

def losowanie():
    global losowe_dobra_odp_latwy, losowe_dobra_odp_sredni, losowe_a, losowe_b, losowe_c, losowe_d, losowe_e, losowe_f, losowe_g, losowe_h
    # Tworzenie listy, która będzie zawierała dostępne liczby
    dostepne_liczby = list(range(1, 21))
    # Losowanie dla pozostałych zmiennych
    losowe_a = random.choice(dostepne_liczby)
    dostepne_liczby.remove(losowe_a)
    losowe_b = random.choice(dostepne_liczby)
    dostepne_liczby.remove(losowe_b)
    losowe_c = random.choice(dostepne_liczby)
    dostepne_liczby.remove(losowe_c)
    losowe_d = random.choice(dostepne_liczby)
    dostepne_liczby.remove(losowe_d)
    losowe_e = random.choice(dostepne_liczby)
    dostepne_liczby.remove(losowe_e)
    losowe_f = random.choice(dostepne_liczby)
    dostepne_liczby.remove(losowe_f)
    losowe_g = random.choice(dostepne_liczby)
    dostepne_liczby.remove(losowe_g)
    losowe_h = random.choice(dostepne_liczby)
    # losowanie dobrej odp
    losowe_dobra_odp_latwy = random.choice([losowe_a, losowe_b, losowe_c, losowe_d, losowe_e, losowe_f])
    losowe_dobra_odp_sredni = random.choice(
        [losowe_a, losowe_b, losowe_c, losowe_d, losowe_e, losowe_f, losowe_g, losowe_h])



uzyte = []
def latwy():
    def usun_uzyte():
        uzyte.clear()



    losowanie()
    zapomnij_guziki()
    poprawny_wynik = connect.cursor()
    poprawny_wynik.execute(f"SELECT odp FROM latwy WHERE id = {losowe_dobra_odp_latwy}")
    zapytanie_wynik = poprawny_wynik.fetchone()
    zapytanie_wynik_str = str(zapytanie_wynik)
    global zapytanie_wynik_strip, odp_a_strip, odp_b_strip, odp_c_strip, odp_d_strip, odp_e_strip, odp_f_strip, \
        bledy_latwe_label, obrazek_label, przycisk1_latwy, przycisk2_latwy, przycisk3_latwy, przycisk4_latwy, \
        przycisk5_latwy ,przycisk6_latwy
    zapytanie_wynik_strip = zapytanie_wynik_str.strip('(),\'')
    print(zapytanie_wynik_strip)

    odp_a = connect.cursor()
    odp_a.execute(f"SELECT odp FROM latwy WHERE id = {losowe_a}")
    odp_a_wynik = str(odp_a.fetchone())
    odp_a_strip = odp_a_wynik.strip('(),\'')
    latwy_guzik1.set(odp_a_strip)
    print(odp_a_strip)
    odp_b = connect.cursor()
    odp_b.execute(f"SELECT odp FROM latwy WHERE id = {losowe_b}")
    odp_b_wynik = str(odp_b.fetchone())
    odp_b_strip = odp_b_wynik.strip('(),\'')
    latwy_guzik2.set(odp_b_strip)
    print(odp_b_strip)
    odp_c = connect.cursor()
    odp_c.execute(f"SELECT odp FROM latwy WHERE id = {losowe_c}")
    odp_c_wynik = str(odp_c.fetchone())
    odp_c_strip = odp_c_wynik.strip('(),\'')
    latwy_guzik3.set(odp_c_strip)
    print(odp_c_strip)
    odp_d = connect.cursor()
    odp_d.execute(f"SELECT odp FROM latwy WHERE id = {losowe_d}")
    odp_d_wynik = str(odp_d.fetchone())
    odp_d_strip = odp_d_wynik.strip('(),\'')
    latwy_guzik4.set(odp_d_strip)
    print(odp_d_strip)
    odp_e = connect.cursor()
    odp_e.execute(f"SELECT odp FROM latwy WHERE id = {losowe_e}")
    odp_e_wynik = str(odp_e.fetchone())
    odp_e_strip = odp_e_wynik.strip('(),\'')
    latwy_guzik5.set(odp_e_strip)
    print(odp_e_strip)
    odp_f = connect.cursor()
    odp_f.execute(f"SELECT odp FROM latwy WHERE id = {losowe_f}")
    odp_f_wynik = str(odp_f.fetchone())
    odp_f_strip = odp_f_wynik.strip('(),\'')
    latwy_guzik6.set(odp_f_strip)
    print(odp_f_strip)

    elo_label.place(x=430,y=0)



    bledy_latwe_label = tk.Label(root, textvariable=bledy_l_var, font=('Aharoni','14','bold'), bg='#7ac70c')
    bledy_latwe_label.place(x=400,y=30)
    image_path = f"Latwy_Zdjecia/{zapytanie_wynik_strip}.gif"



    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    obrazek_label = tk.Label(root, image=photo, width=400, height=400)
    obrazek_label.image = photo  # Keeping a reference
    obrazek_label.place(x=20,y=100)


    przycisk1_latwy = tk.Button(root, textvariable=latwy_guzik1, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi(odp_a_strip), losowanie, usun_uzyte), font=('Aharoni','14','bold'), bg='#7ac70c',height=1)
    przycisk1_latwy.place(x=450, y=150)

    przycisk2_latwy = tk.Button(root, textvariable=latwy_guzik2, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi(odp_b_strip), losowanie, usun_uzyte), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk2_latwy.place(x=450, y=200)

    przycisk3_latwy = tk.Button(root, textvariable=latwy_guzik3, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi(odp_c_strip), losowanie, usun_uzyte), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk3_latwy.place(x=450,y=250)

    przycisk4_latwy = tk.Button(root, textvariable=latwy_guzik4, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi(odp_d_strip), losowanie, usun_uzyte), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk4_latwy.place(x=450, y=300)

    przycisk5_latwy = tk.Button(root, textvariable=latwy_guzik5, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi(odp_e_strip), losowanie, usun_uzyte), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk5_latwy.place(x=450, y=350)

    przycisk6_latwy = tk.Button(root, textvariable=latwy_guzik6, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi(odp_f_strip), losowanie, usun_uzyte), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk6_latwy.place(x=450, y=400)



def sprawdzenie_dobrej_odpowiedzi(wybrana_odpowiedz):
    if zapytanie_wynik_strip == wybrana_odpowiedz:
        dodawanie_elo()
        global elo, bledy
        if elo == 20:
            elo_label.place_forget()
            print(elo)
            schowaj_latwy()
            info = msg.showinfo("Koniec", f"Udało ci się ukonczyć ten test ze wszystkimi punktami ("
                                          f"{elo}).\nGratulacje!")
            if info == "ok":
                bledy = 0
                elo = 0
                elo_var.set(elo)

        else:
            bledy_latwe_label.place_forget()
            obrazek_label.place_forget()
            przycisk1_latwy.place_forget()
            przycisk2_latwy.place_forget()
            przycisk3_latwy.place_forget()
            przycisk4_latwy.place_forget()
            przycisk5_latwy.place_forget()
            przycisk6_latwy.place_forget()
            latwy()
    else:
        if wybrana_odpowiedz == odp_a_strip:
            top = Toplevel()
            top.title(odp_a_strip)
            a = Image.open(f"Latwy_Zdjecia/{odp_a_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1,width=400,height=400)
            ashowinfo.image = a1
            ashowinfo.grid(row=0, column=0)
            przycisk1_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_b_strip:
             top = Toplevel()
             top.title(odp_b_strip)
             a = Image.open(f"Latwy_Zdjecia/{odp_b_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.grid(row=0, column=0)
             przycisk2_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_c_strip:
             top = Toplevel()
             top.title(odp_c_strip)
             a = Image.open(f"Latwy_Zdjecia/{odp_c_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.grid(row=0, column=0)
             przycisk3_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_d_strip:
             top = Toplevel()
             top.title(odp_d_strip)
             a = Image.open(f"Latwy_Zdjecia/{odp_d_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.grid(row=0, column=0)
             przycisk4_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_e_strip:
             top = Toplevel()
             top.title(odp_e_strip)
             a = Image.open(f"Latwy_Zdjecia/{odp_e_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.grid(row=0, column=0)
             przycisk5_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_f_strip:
             top = Toplevel()
             top.title(odp_f_strip)
             a = Image.open(f"Latwy_Zdjecia/{odp_f_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.grid(row=0, column=0)
             przycisk6_latwy.config(state="disabled")
        dodawanie_bledow(bledy_l_var)
        if bledy > 4:
            elo_label.place_forget()
            print(elo)
            schowaj_latwy()
            if elo >= 1:
                info = msg.showinfo("Koniec", f"Udało ci się zdobyć {elo} punktów przed zrobieniem 5 blędów.\nGratulacje!")
                if info == "ok":
                    bledy = 0
                    elo = 0
                    elo_var.set(elo)
            else:
                info = msg.showinfo("Koniec",
                                    f"Niestety nie udało ci się zdobyć żadnych punktów")
                if info == "ok":
                    bledy = 0
                    elo = 0
                    elo_var.set(elo)


def sredni():
    zapomnij_guziki()
    losowanie()
    global odp_a_sredni_strip, odp_b_sredni_strip, odp_c_sredni_strip, odp_d_sredni_strip, odp_e_sredni_strip, odp_f_sredni_strip, odp_g_sredni_strip, odp_h_sredni_strip
    global odp_a_sprawdzenie, odp_b_sprawdzenie, odp_c_sprawdzenie, odp_d_sprawdzenie, odp_e_sprawdzenie, odp_f_sprawdzenie, odp_g_sprawdzenie, odp_h_sprawdzenie
    dobra_odp_sredni = connect.cursor()
    dobra_odp_sredni.execute(f"SELECT polski FROM sredni WHERE id = {losowe_dobra_odp_sredni}")
    dobra_odp_sredni_wynik = str(dobra_odp_sredni.fetchone())
    global dobra_odp_sredni_strip
    dobra_odp_sredni_strip = dobra_odp_sredni_wynik.strip('(),\'')
    sredni_odp_label.set(dobra_odp_sredni_strip)

    odp_a_sredni = connect.cursor()
    odp_a_sredni.execute(f"SELECT odp FROM sredni WHERE id = {losowe_a}")
    odp_a_wynik_sredni = str(odp_a_sredni.fetchone())
    odp_a_sredni_strip = odp_a_wynik_sredni.strip('(),\'')
    sredny_guzik1.set(odp_a_sredni_strip)

    odpa_spawdz = connect.cursor()
    odpa_spawdz.execute(f"SELECT polski FROM sredni WHERE id = {losowe_a}")
    odpa_sprawdz_wynik = str(odpa_spawdz.fetchone())
    odp_a_sprawdzenie = odpa_sprawdz_wynik.strip('(),\'')

    odp_b_sredni = connect.cursor()
    odp_b_sredni.execute(f"SELECT odp FROM sredni WHERE id = {losowe_b}")
    odp_b_wynik_sredni = str(odp_b_sredni.fetchone())
    odp_b_sredni_strip = odp_b_wynik_sredni.strip('(),\'')
    sredny_guzik2.set(odp_b_sredni_strip)

    odpb_spawdz = connect.cursor()
    odpb_spawdz.execute(f"SELECT polski FROM sredni WHERE id = {losowe_b}")
    odpb_sprawdz_wynik = str(odpb_spawdz.fetchone())
    odp_b_sprawdzenie = odpb_sprawdz_wynik.strip('(),\'')

    odp_c_sredni = connect.cursor()
    odp_c_sredni.execute(f"SELECT odp FROM sredni WHERE id = {losowe_c}")
    odp_c_wynik_sredni = str(odp_c_sredni.fetchone())
    odp_c_sredni_strip = odp_c_wynik_sredni.strip('(),\'')
    sredny_guzik3.set(odp_c_sredni_strip)

    odpc_spawdz = connect.cursor()
    odpc_spawdz.execute(f"SELECT polski FROM sredni WHERE id = {losowe_c}")
    odpc_sprawdz_wynik = str(odpc_spawdz.fetchone())
    odp_c_sprawdzenie = odpc_sprawdz_wynik.strip('(),\'')

    odp_d_sredni = connect.cursor()
    odp_d_sredni.execute(f"SELECT odp FROM sredni WHERE id = {losowe_d}")
    odp_d_wynik_sredni = str(odp_d_sredni.fetchone())
    odp_d_sredni_strip = odp_d_wynik_sredni.strip('(),\'')
    sredny_guzik4.set(odp_d_sredni_strip)

    odpd_spawdz = connect.cursor()
    odpd_spawdz.execute(f"SELECT polski FROM sredni WHERE id = {losowe_d}")
    odpd_sprawdz_wynik = str(odpd_spawdz.fetchone())
    odp_d_sprawdzenie = odpd_sprawdz_wynik.strip('(),\'')

    odp_e_sredni = connect.cursor()
    odp_e_sredni.execute(f"SELECT odp FROM sredni WHERE id = {losowe_e}")
    odp_e_wynik_sredni = str(odp_e_sredni.fetchone())
    odp_e_sredni_strip = odp_e_wynik_sredni.strip('(),\'')
    sredny_guzik5.set(odp_e_sredni_strip)

    odpe_spawdz = connect.cursor()
    odpe_spawdz.execute(f"SELECT polski FROM sredni WHERE id = {losowe_e}")
    odpe_sprawdz_wynik = str(odpe_spawdz.fetchone())
    odp_e_sprawdzenie = odpe_sprawdz_wynik.strip('(),\'')

    odp_f_sredni = connect.cursor()
    odp_f_sredni.execute(f"SELECT odp FROM sredni WHERE id = {losowe_f}")
    odp_f_wynik_sredni = str(odp_f_sredni.fetchone())
    odp_f_sredni_strip = odp_f_wynik_sredni.strip('(),\'')
    sredny_guzik6.set(odp_f_sredni_strip)

    odpf_spawdz = connect.cursor()
    odpf_spawdz.execute(f"SELECT polski FROM sredni WHERE id = {losowe_f}")
    odpf_sprawdz_wynik = str(odpf_spawdz.fetchone())
    odp_f_sprawdzenie = odpf_sprawdz_wynik.strip('(),\'')

    odp_g_sredni = connect.cursor()
    odp_g_sredni.execute(f"SELECT odp FROM sredni WHERE id = {losowe_g}")
    odp_g_wynik_sredni = str(odp_g_sredni.fetchone())
    odp_g_sredni_strip = odp_g_wynik_sredni.strip('(),\'')
    sredny_guzik7.set(odp_g_sredni_strip)

    odpg_spawdz = connect.cursor()
    odpg_spawdz.execute(f"SELECT polski FROM sredni WHERE id = {losowe_g}")
    odpg_sprawdz_wynik = str(odpg_spawdz.fetchone())
    odp_g_sprawdzenie = odpg_sprawdz_wynik.strip('(),\'')

    odp_h_sredni = connect.cursor()
    odp_h_sredni.execute(f"SELECT odp FROM sredni WHERE id = {losowe_h}")
    odp_h_wynik_sredni = str(odp_h_sredni.fetchone())
    odp_h_sredni_strip = odp_h_wynik_sredni.strip('(),\'')
    sredny_guzik8.set(odp_h_sredni_strip)

    odph_spawdz = connect.cursor()
    odph_spawdz.execute(f"SELECT polski FROM sredni WHERE id = {losowe_h}")
    odph_sprawdz_wynik = str(odph_spawdz.fetchone())
    odp_h_sprawdzenie = odph_sprawdz_wynik.strip('(),\'')

    elo_label.place(x=430,y=0)

    global odp_label, przycisk1_sredni, przycisk2_sredni, przycisk3_sredni, przycisk4_sredni, przycisk5_sredni, \
        przycisk6_sredni, przycisk7_sredni, przycisk8_sredni, bledy_srednie_label
    bledy_srednie_label = tk.Label(root, textvariable=bledy_s_var,font=('Aharoni','14','bold'), bg='#7ac70c', height=1)

    bledy_srednie_label.place(x=400,y=30)

    odp_label = tk.Label(root, textvariable=sredni_odp_label, font=('Aharoni','18','bold'), bg='#7ac70c', height=1)
    odp_label.place(x=150,y=200)
    
    przycisk1_sredni = tk.Button(root, textvariable=sredny_guzik1, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_a_sprawdzenie, przycisk1_sredni), losowanie), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk1_sredni.place(x=415, y=100)

    przycisk2_sredni = tk.Button(root, textvariable=sredny_guzik2, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_b_sprawdzenie, przycisk2_sredni), losowanie), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk2_sredni.place(x=415,y=150)

    przycisk3_sredni = tk.Button(root, textvariable=sredny_guzik3, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_c_sprawdzenie, przycisk3_sredni), losowanie), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk3_sredni.place(x=415,y=200)

    przycisk4_sredni = tk.Button(root, textvariable=sredny_guzik4, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_d_sprawdzenie, przycisk4_sredni), losowanie), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk4_sredni.place(x=415,y=250)

    przycisk5_sredni = tk.Button(root, textvariable=sredny_guzik5, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_e_sprawdzenie, przycisk5_sredni), losowanie), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk5_sredni.place(x=415,y=300)

    przycisk6_sredni = tk.Button(root, textvariable=sredny_guzik6, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_f_sprawdzenie, przycisk6_sredni), losowanie), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk6_sredni.place(x=415,y=350)

    przycisk7_sredni = tk.Button(root, textvariable=sredny_guzik7, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_g_sprawdzenie, przycisk7_sredni), losowanie), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk7_sredni.place(x=415,y=400)

    przycisk8_sredni = tk.Button(root, textvariable=sredny_guzik8, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_h_sprawdzenie, przycisk8_sredni), losowanie), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    przycisk8_sredni.place(x=415,y=450)


def sprawdzenie_dobrej_odpowiedzi_sredni(wybrana_odpowiedz, przycisk):
    if dobra_odp_sredni_strip == wybrana_odpowiedz:
        dodawanie_elo()
        global elo, bledy
        if elo == 20:
            elo_label.place_forget()
            print(elo)
            schowaj_sredni()
            info = msg.showinfo("Koniec", f"Udało ci się ukonczyć ten test ze wszystkimi punktami ("
                                          f"{elo}).\nGratulacje!")
            if info == "ok":
                bledy = 0
                elo = 0
                elo_var.set(elo)
        else:
            bledy_srednie_label.place_forget()
            odp_label.place_forget()
            przycisk1_sredni.place_forget()
            przycisk2_sredni.place_forget()
            przycisk3_sredni.place_forget()
            przycisk4_sredni.place_forget()
            przycisk5_sredni.place_forget()
            przycisk6_sredni.place_forget()
            przycisk7_sredni.place_forget()
            przycisk8_sredni.place_forget()
            sredni()
    else:
        if wybrana_odpowiedz == odp_a_sprawdzenie:
            top = Toplevel()
            top.title(odp_a_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_a_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.grid(row=0, column=0)
            przycisk1_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_b_sprawdzenie:
            top = Toplevel()
            top.title(odp_b_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_b_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.grid(row=0, column=0)
            przycisk2_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_c_sprawdzenie:
            top = Toplevel()
            top.title(odp_c_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_c_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.grid(row=0, column=0)
            przycisk3_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_d_sprawdzenie:
            top = Toplevel()
            top.title(odp_d_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_d_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.grid(row=0, column=0)
            przycisk4_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_e_sprawdzenie:
            top = Toplevel()
            top.title(odp_e_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_e_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.grid(row=0, column=0)
            przycisk5_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_f_sprawdzenie:
            top = Toplevel()
            top.title(odp_f_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_f_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.grid(row=0, column=0)
            przycisk6_sredni.config(state="disabled")
        elif wybrana_odpowiedz == odp_g_sprawdzenie:
            top = Toplevel()
            top.title(odp_g_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_g_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.grid(row=0, column=0)
            przycisk7_sredni.config(state="disabled")
        elif wybrana_odpowiedz == odp_h_sprawdzenie:
            top = Toplevel()
            top.title(odp_h_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_h_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.grid(row=0, column=0)
            przycisk8_sredni.config(state="disabled")
        dodawanie_bledow(bledy_s_var)
        if bledy > 4:
            elo_label.place_forget()
            print(elo)
            schowaj_sredni()
            if elo >= 1:
                info = msg.showinfo("Koniec", f"Udało ci się zdobyć {elo} punktów przed zrobieniem 5 blędów.\nGratulacje!")
                if info == "ok":
                    bledy = 0
                    elo = 0
                    elo_var.set(elo)
            else:
                info = msg.showinfo("Koniec",
                                    f"Niestety nie udało ci się zdobyć żadnych punktów")
                if info == "ok":
                    bledy = 0
                    elo = 0
                    elo_var.set(elo)

def srednio_trudny():
    global polskie_slowo_strip, ang_slowo_strip, samogloska_strip, samo, polskie, angielskie, dobre_samo_tekst, \
        dobre_samo, zle_samo_tekst, zle_samo, samogloska_entry,samogloska_guzik, bledy_st_label
    zapomnij_guziki()
    for i in range (20):
        global losowe
        losowe = random.randint(1, 20)
        if losowe in uzyte:  # Jeżeli pytanie zostało już uzyte niech dalej losuje
            continue
        else:
            uzyte.append(losowe)
    polskie_zapytanie = connect.cursor()
    polskie_zapytanie.execute(f"SELECT pl FROM srednio_trudny WHERE id = {losowe}")
    polskie_slowo = polskie_zapytanie.fetchone()
    polskie_slowo_str = str(polskie_slowo)
    polskie_slowo_strip = polskie_slowo_str.strip('(),\'')
    pl_var.set(polskie_slowo_strip)
    ang_zapytanie = connect.cursor()
    ang_zapytanie.execute(f"SELECT text FROM srednio_trudny WHERE id = {losowe}")
    ang_slowo = ang_zapytanie.fetchone()
    ang_slowo_str = str(ang_slowo)
    ang_slowo_strip = ang_slowo_str.strip('(),\'')
    en_czesci_var.set(ang_slowo_strip)
    samogloska_zapytanie = connect.cursor()
    samogloska_zapytanie.execute(f"SELECT odp FROM srednio_trudny WHERE id = {losowe}")
    samogloska_slowo = samogloska_zapytanie.fetchone()
    samogloska_str = str(samogloska_slowo)
    samogloska_strip = samogloska_str.strip('(),\'')




    elo_label.place(x=430,y=0)


    bledy_st_label = tk.Label(root, textvariable=bledy_st_var, font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    bledy_st_label.place(x=400,y=30)

    polskie = tk.Label(root, textvariable=pl_var, font=('Aharoni','18','bold'), bg='#7ac70c', width=13, height=1)
    polskie.place(x=345, y=100)

    angielskie = tk.Label(root, textvariable=en_czesci_var, font=('Aharoni','14','bold'), bg='#7ac70c', width=13, height=1)
    angielskie.place(x=365,y=150)

    dobre_samo_tekst = tk.Label(root, text="Dobre samogłoski:", font=('Aharoni','18','bold'), bg='#7ac70c', height=1)
    dobre_samo_tekst.place(x=333,y= 200)

    dobre_samo = tk.Label(root, textvariable=dobre_samo_var, fg="green", font=('Aharoni','14','bold'), bg='#7ac70c', width=10, height=1)
    dobre_samo.place(x=380,y=250)

    zle_samo_tekst = tk.Label(root, text="Złe samogłoski:", font=('Aharoni','18','bold'), bg='#7ac70c', height=1)
    zle_samo_tekst.place(x=350,y=300)

    zle_samo = tk.Label(root, textvariable=zle_samo_var, fg="red", font=('Aharoni','14','bold'), bg='#7ac70c', width=10, height=1)
    zle_samo.place(x=380,y=350)

    samogloska_entry = tk.Entry(root, textvariable=samogloska_entry_var, font=('Aharoni','14','bold'), bg='#7ac70c')
    samogloska_entry.place(x=333,y=400)

    samogloska_guzik = tk.Button(root, text="Sprawdź", command=lambda: sprawdzanie_srednio_trudne(), font=('Aharoni','14','bold'), bg='#7ac70c', height=1)
    samogloska_guzik.place(x=390,y=450)


    samo = samogloska_strip.split("#")

dobre = []
zle = []
jedna = []
samogloski = ["a","e","i","y","u","o"]
def sprawdzanie_srednio_trudne():
    odpowiedz = samogloska_entry_var.get()

    if odpowiedz in samo:
        dobre.append(odpowiedz)
        samo.remove(odpowiedz)
        dobre_samo_var.set(dobre)
        samogloska_entry_var.set("")
        if len(samo) < 1:
            global elo, bledy
            if elo > 19:
                elo_label.place_forget()
                print(elo)
                schowaj_st()
                info = msg.showinfo("Koniec", f"Udało ci się ukonczyć ten test ze wszystkimi punktami ("
                                              f"{elo}).\nGratulacje!")
                if info == "ok":
                    bledy = 0
                    elo = 0
                    elo_var.set(elo)
                    uzyte.clear()
            else:
                bledy_st_label.place_forget()
                polskie.place_forget()
                angielskie.place_forget()
                dobre_samo_tekst.place_forget()
                dobre_samo.place_forget()
                zle_samo_tekst.place_forget()
                zle_samo.place_forget()
                samogloska_entry.place_forget()
                samogloska_guzik.place_forget()
                srednio_trudny()
            dobre.clear()
            zle.clear()
            dobre_samo_var.set("")
            zle_samo_var.set("")
            dodawanie_elo()
    elif odpowiedz == "" or odpowiedz not in samogloski:
        try:
            zle.remove(odpowiedz)
        except:
            samogloska_entry_var.set("")
            print("Nic nie zostało wpisane lub została podana spółgłoska")
    elif odpowiedz in dobre or odpowiedz in zle:
        try:
            zle.remove(dobre)
            zle.remove(odpowiedz)
        except:
            print("Podana samogłoska została już użyta")
            samogloska_entry_var.set("")
    else:
        zle.append(odpowiedz)
        zle_samo_var.set(zle)
        samogloska_entry_var.set("")
        dodawanie_bledow(bledy_st_var)
        if bledy > 4:
            elo_label.place_forget()
            print(elo)
            schowaj_st()
            if elo >= 1:
                info = msg.showinfo("Koniec", f"Udało ci się zdobyć {elo} punktów przed zrobieniem 5 blędów.\nGratulacje!")
                if info == "ok":
                    bledy = 0
                    elo = 0
                    elo_var.set(elo)
            else:
                info = msg.showinfo("Koniec",
                                    f"Niestety nie udało ci się zdobyć żadnych punktów")
                if info == "ok":
                    bledy = 0
                    elo = 0
                    elo_var.set(elo)


def trudny():
    
    global polish_label, input_label, zatwierdz, wprowadzony_text, wprowadzona_odpowiedz, bledy_trudne_label
    zapomnij_guziki()
    elo_label.place(x=430,y=0)

    bledy_trudne_label = tk.Label(root, textvariable=bledy_t_var, font=('Aharoni','13','bold'), bg='#7ac70c')
    bledy_trudne_label.place(x=400,y=30)

    polish_label = tk.Label(root, textvariable=trudny_pl, font=('Aharoni','18','bold'), bg='#7ac70c')
    polish_label.place(x=407,y=100)

    input_label = tk.Entry(root, textvariable=trudny_input, font=('Aharoni','13','bold'), bg='#7ac70c')
    input_label.place(x=365, y=150)


    wprowadzona_odpowiedz = tk.Label(root, textvariable=wprowadzony_text, fg="black", bg="#7ac70c", font=('Aharoni','13','bold'))


    zatwierdz = tk.Button(root, text="Zatwierdź", command=lambda: sprawdz_trudny(), font=('Aharoni','13','bold'), bg='#7ac70c')
    zatwierdz.place(x=405, y=200)

    for i in range(20):
        global losowe
        losowe = random.randint(1, 20)
        if losowe in uzyte:  # Jeżeli pytanie zostało już uzyte niech dalej losuje
            continue
        else:
            uzyte.append(losowe)

    pl = connect.cursor()
    pl.execute(f"SELECT pl FROM trudny WHERE id = {losowe}")
    pl_text = str(pl.fetchone())
    pl_text_strip = pl_text.strip('(),\'')
    trudny_pl.set(pl_text_strip)


def sprawdz_trudny():
    global odp_text_strip
    user_answer = trudny_input.get()
    odp = connect.cursor()
    odp.execute(f"SELECT odp FROM trudny WHERE id = {losowe}")
    odp_text = str(odp.fetchone())
    odp_text_strip = odp_text.strip('(),\'')
    wprowadzony_text.set(user_answer)
    if user_answer == odp_text_strip:
        dodawanie_elo()
        global elo, bledy
        if elo > 19:

            elo_label.place_forget()
            print(elo)
            schowaj_trudne()
            info = msg.showinfo("Koniec", f"Udało ci się ukonczyć ten test ze wszystkimi punktami ("
                                          f"{elo}).\nGratulacje!")
            if info == "ok":
                bledy = 0
                elo = 0
                elo_var.set(elo)
                uzyte.clear()
        else:
            print("Poprawna odpowiedz!")
            bledy_trudne_label.place_forget()
            polish_label.place_forget()
            input_label.place_forget()
            zatwierdz.place_forget()
            wprowadzona_odpowiedz.place_forget()
            trudny()
    else:
        dodawanie_bledow(bledy_t_var)
        literki_trudny()
        if bledy > 4:
            elo_label.place_forget()
            print(elo)
            schowaj_trudne()
            if elo >= 1:
                info = msg.showinfo("Koniec", f"Udało ci się zdobyć {elo} punktów przed zrobieniem 5 blędów.\nGratulacje!")
                if info == "ok":
                    bledy = 0
                    elo = 0
                    elo_var.set(elo)
            else:
                info = msg.showinfo("Koniec",
                                    f"Niestety nie udało ci się zdobyć żadnych punktów")
                if info == "ok":
                    bledy = 0
                    elo = 0
                    elo_var.set(elo)

    # wprowadzona_odpowiedz.place()

    trudny_input.set("")
    print("Odpowiedź gracza:", user_answer)


def literki_trudny():
    podpowiedz = ""
    user_answer = trudny_input.get()
    if user_answer == odp_text_strip or len(user_answer) > len(
            odp_text_strip):  # działa tylko i tylko wtedy, gdy długość odpowiedzi GRACZA jest równa długości POPRAWNEJ odpowiedzi lub jej długość jest większa niż porawna odpowiedź
        for i in range(len(str(odp_text_strip))):
            if odp_text_strip[i] == user_answer[i]:
                podpowiedz = podpowiedz + user_answer[i]
            else:
                podpowiedz = podpowiedz + "_"
    else:  # patrząc, że pętla "for" jest uzależniona od długości poprawnej odpowiedzi tj. będzie działać nawet gdy długość odpowiedzi gracza jest dłuższa bierzemy przypadek gdy odpowiedź gracza może być krótsza od tej porpawnej
        dlugosc_do_nadrobienia = len(odp_text_strip) - len(user_answer)
        for x in range(len(str(user_answer))):
            if odp_text_strip[x] == user_answer[x]:
                podpowiedz = podpowiedz + user_answer[x]
            else:
                podpowiedz = podpowiedz + "_"
        for x in range(dlugosc_do_nadrobienia):
            podpowiedz = podpowiedz + "_"
    wprowadzony_text.set(podpowiedz)
    wprowadzona_odpowiedz.place(x=430, y=270)


root = tk.Tk()
root.title("Duolingo")
root.geometry("900x650")
root.resizable(False, False)


root.configure(background='#8ee000')

latwy_guzik1 = tk.StringVar()
latwy_guzik2 = tk.StringVar()
latwy_guzik3 = tk.StringVar()
latwy_guzik4 = tk.StringVar()
latwy_guzik5 = tk.StringVar()
latwy_guzik6 = tk.StringVar()

sredni_odp_label = tk.StringVar()
sredny_guzik1 = tk.StringVar()
sredny_guzik2 = tk.StringVar()
sredny_guzik3 = tk.StringVar()
sredny_guzik4 = tk.StringVar()
sredny_guzik5 = tk.StringVar()
sredny_guzik6 = tk.StringVar()
sredny_guzik7 = tk.StringVar()
sredny_guzik8 = tk.StringVar()

bledy_l_var = tk.IntVar()
bledy_s_var = tk.IntVar()
bledy_st_var = tk.IntVar()
bledy_t_var = tk.IntVar()

pl_var = tk.StringVar()
en_czesci_var = tk.StringVar()
samogloska_entry_var = tk.StringVar()
dobre_samo_var = tk.StringVar()
zle_samo_var = tk.StringVar()

trudny_pl = tk.StringVar()
trudny_input = tk.StringVar()
wprowadzony_text = tk.StringVar()

elo_var = tk.IntVar()
ogolne_punkty_var = tk.IntVar()

bledy_l_var.set("Błędy: 0")
bledy_s_var.set("Błędy: 0")
bledy_st_var.set("Błędy: 0")
bledy_t_var.set("Błędy: 0")
ogolne_punkty_var.set("Ogolne punkty: 0")


elo_label = tk.Label(root, textvariable=elo_var, font=('Aharoni','13','bold'), bg='#7ac70c')



ogolne_punkty_label = tk.Label(root, textvariable=ogolne_punkty_var, bg='#7ac70c', font=('Aharoni', '13', 'bold'))
ogolne_punkty_label.place(x=0, y=0)

PoziomLatwy = tk.Button(root, text="Poziom Łatwy", command=latwy, height=3, width=20, font=('Aharoni', '14', 'bold'), bg='#43C000')
PoziomLatwy.grid(row=1, column=1, padx=130, pady=150)

PoziomSredni = tk.Button(root, text="Poziom Średni", command=sredni, height=3, width=20, font=('Aharoni', '14', 'bold'), bg='#43C000')
PoziomSredni.grid(row=1, column=2)

PoziomSredniotrudny = tk.Button(root, text="Poziom Średnio-trudny", command=srednio_trudny, height=3, width=20, font=('Aharoni', '14', 'bold'), bg='#43C000')
PoziomSredniotrudny.grid(row=2, column=2)

PoziomTrudny = tk.Button(root, text="Poziom Trudny", command=trudny, height=3, width=20, font=('Aharoni', '14', 'bold'), bg='#43C000')
PoziomTrudny.grid(row=2, column=1)




root.mainloop()