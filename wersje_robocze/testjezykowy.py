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
    bledy_latwe_label.pack_forget()
    obrazek_label.pack_forget()
    przycisk1_latwy.pack_forget()
    przycisk2_latwy.pack_forget()
    przycisk3_latwy.pack_forget()
    przycisk4_latwy.pack_forget()
    przycisk5_latwy.pack_forget()
    przycisk6_latwy.pack_forget()
    start()
def schowaj_sredni():
    bledy_srednie_label.pack_forget()
    odp_label.pack_forget()
    przycisk1_sredni.pack_forget()
    przycisk2_sredni.pack_forget()
    przycisk3_sredni.pack_forget()
    przycisk4_sredni.pack_forget()
    przycisk5_sredni.pack_forget()
    przycisk6_sredni.pack_forget()
    przycisk7_sredni.pack_forget()
    przycisk8_sredni.pack_forget()
    start()
def schowaj_st():
    bledy_st_label.pack_forget()
    polskie.pack_forget()
    angielskie.pack_forget()
    dobre_samo_tekst.pack_forget()
    dobre_samo.pack_forget()
    zle_samo_tekst.pack_forget()
    zle_samo.pack_forget()
    samogloska_entry.pack_forget()
    samogloska_guzik.pack_forget()
    start()
def schowaj_trudne():
    bledy_trudne_label.pack_forget()
    polish_label.pack_forget()
    input_label.pack_forget()
    zatwierdz.pack_forget()
    wprowadzona_odpowiedz.pack_forget()
    start()

def start():
    PoziomLatwy.pack()
    PoziomSredni.pack()
    PoziomSredniotrudny.pack()
    PoziomTrudny.pack()

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
    PoziomLatwy.pack_forget()
    PoziomSredniotrudny.pack_forget()
    PoziomTrudny.pack_forget()
    PoziomSredni.pack_forget()

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
    elo_label.pack()
    bledy_latwe_label = tk.Label(root, textvariable=bledy_l_var)
    bledy_latwe_label.pack()
    image_path = f"Latwy_Zdjecia/{zapytanie_wynik_strip}.gif"

    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    obrazek_label = tk.Label(root, image=photo, width=400, height=400)
    obrazek_label.image = photo  # Keeping a reference
    obrazek_label.pack()
    przycisk1_latwy = tk.Button(root, textvariable=latwy_guzik1, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi(odp_a_strip), losowanie, usun_uzyte))
    przycisk1_latwy.pack()
    przycisk2_latwy = tk.Button(root, textvariable=latwy_guzik2, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi(odp_b_strip), losowanie, usun_uzyte))
    przycisk2_latwy.pack()
    przycisk3_latwy = tk.Button(root, textvariable=latwy_guzik3, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi(odp_c_strip), losowanie, usun_uzyte))
    przycisk3_latwy.pack()
    przycisk4_latwy = tk.Button(root, textvariable=latwy_guzik4, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi(odp_d_strip), losowanie, usun_uzyte))
    przycisk4_latwy.pack()
    przycisk5_latwy = tk.Button(root, textvariable=latwy_guzik5, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi(odp_e_strip), losowanie, usun_uzyte))
    przycisk5_latwy.pack()
    przycisk6_latwy = tk.Button(root, textvariable=latwy_guzik6, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi(odp_f_strip), losowanie, usun_uzyte))
    przycisk6_latwy.pack()
def sprawdzenie_dobrej_odpowiedzi(wybrana_odpowiedz):
    if zapytanie_wynik_strip == wybrana_odpowiedz:
        dodawanie_elo()
        global elo, bledy
        if elo == 20:
            elo_label.pack_forget()
            print(elo)
            schowaj_latwy()
            info = msg.showinfo("Koniec", f"Udało ci się ukonczyć ten test ze wszystkimi punktami ("
                                          f"{elo}).\nGratulacje!")
            if info == "ok":
                bledy = 0
                elo = 0
                elo_var.set(elo)

        else:
            bledy_latwe_label.pack_forget()
            obrazek_label.pack_forget()
            przycisk1_latwy.pack_forget()
            przycisk2_latwy.pack_forget()
            przycisk3_latwy.pack_forget()
            przycisk4_latwy.pack_forget()
            przycisk5_latwy.pack_forget()
            przycisk6_latwy.pack_forget()
            latwy()
    else:
        if wybrana_odpowiedz == odp_a_strip:
            top = Toplevel()
            top.title(odp_a_strip)
            a = Image.open(f"Latwy_Zdjecia/{odp_a_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1,width=400,height=400)
            ashowinfo.image = a1
            ashowinfo.pack()
            przycisk1_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_b_strip:
             top = Toplevel()
             top.title(odp_b_strip)
             a = Image.open(f"Latwy_Zdjecia/{odp_b_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk2_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_c_strip:
             top = Toplevel()
             top.title(odp_c_strip)
             a = Image.open(f"Latwy_Zdjecia/{odp_c_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk3_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_d_strip:
             top = Toplevel()
             top.title(odp_d_strip)
             a = Image.open(f"Latwy_Zdjecia/{odp_d_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk4_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_e_strip:
             top = Toplevel()
             top.title(odp_e_strip)
             a = Image.open(f"Latwy_Zdjecia/{odp_e_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk5_latwy.config(state="disabled")
        elif wybrana_odpowiedz == odp_f_strip:
             top = Toplevel()
             top.title(odp_f_strip)
             a = Image.open(f"Latwy_Zdjecia/{odp_f_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk6_latwy.config(state="disabled")
        dodawanie_bledow(bledy_l_var)
        if bledy > 4:
            elo_label.pack_forget()
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
    elo_label.pack()
    global odp_label, przycisk1_sredni, przycisk2_sredni, przycisk3_sredni, przycisk4_sredni, przycisk5_sredni, \
        przycisk6_sredni, przycisk7_sredni, przycisk8_sredni, bledy_srednie_label
    bledy_srednie_label = tk.Label(root, textvariable=bledy_s_var)
    bledy_srednie_label.pack()
    odp_label = tk.Label(root, textvariable=sredni_odp_label)
    odp_label.pack()
    przycisk1_sredni = tk.Button(root, textvariable=sredny_guzik1, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_a_sprawdzenie, przycisk1_sredni), losowanie))
    przycisk1_sredni.pack()
    przycisk2_sredni = tk.Button(root, textvariable=sredny_guzik2, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_b_sprawdzenie, przycisk2_sredni), losowanie))
    przycisk2_sredni.pack()
    przycisk3_sredni = tk.Button(root, textvariable=sredny_guzik3, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_c_sprawdzenie, przycisk3_sredni), losowanie))
    przycisk3_sredni.pack()
    przycisk4_sredni = tk.Button(root, textvariable=sredny_guzik4, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_d_sprawdzenie, przycisk4_sredni), losowanie))
    przycisk4_sredni.pack()
    przycisk5_sredni = tk.Button(root, textvariable=sredny_guzik5, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_e_sprawdzenie, przycisk5_sredni), losowanie))
    przycisk5_sredni.pack()
    przycisk6_sredni = tk.Button(root, textvariable=sredny_guzik6, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_f_sprawdzenie, przycisk6_sredni), losowanie))
    przycisk6_sredni.pack()
    przycisk7_sredni = tk.Button(root, textvariable=sredny_guzik7, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_g_sprawdzenie, przycisk7_sredni), losowanie))
    przycisk7_sredni.pack()
    przycisk8_sredni = tk.Button(root, textvariable=sredny_guzik8, command=lambda: (
    sprawdzenie_dobrej_odpowiedzi_sredni(odp_h_sprawdzenie, przycisk8_sredni), losowanie))
    przycisk8_sredni.pack()


def sprawdzenie_dobrej_odpowiedzi_sredni(wybrana_odpowiedz, przycisk):
    if dobra_odp_sredni_strip == wybrana_odpowiedz:
        dodawanie_elo()
        global elo, bledy
        if elo == 20:
            elo_label.pack_forget()
            print(elo)
            schowaj_sredni()
            info = msg.showinfo("Koniec", f"Udało ci się ukonczyć ten test ze wszystkimi punktami ("
                                          f"{elo}).\nGratulacje!")
            if info == "ok":
                bledy = 0
                elo = 0
                elo_var.set(elo)
        else:
            bledy_srednie_label.pack_forget()
            odp_label.pack_forget()
            przycisk1_sredni.pack_forget()
            przycisk2_sredni.pack_forget()
            przycisk3_sredni.pack_forget()
            przycisk4_sredni.pack_forget()
            przycisk5_sredni.pack_forget()
            przycisk6_sredni.pack_forget()
            przycisk7_sredni.pack_forget()
            przycisk8_sredni.pack_forget()
            sredni()
    else:
        if wybrana_odpowiedz == odp_a_sprawdzenie:
            top = Toplevel()
            top.title(odp_a_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_a_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.pack()
            przycisk1_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_b_sprawdzenie:
            top = Toplevel()
            top.title(odp_b_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_b_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.pack()
            przycisk2_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_c_sprawdzenie:
            top = Toplevel()
            top.title(odp_c_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_c_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.pack()
            przycisk3_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_d_sprawdzenie:
            top = Toplevel()
            top.title(odp_d_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_d_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.pack()
            przycisk4_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_e_sprawdzenie:
            top = Toplevel()
            top.title(odp_e_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_e_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.pack()
            przycisk5_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_f_sprawdzenie:
            top = Toplevel()
            top.title(odp_f_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_f_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.pack()
            przycisk6_sredni.config(state="disabled")
        elif wybrana_odpowiedz == odp_g_sprawdzenie:
            top = Toplevel()
            top.title(odp_g_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_g_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.pack()
            przycisk7_sredni.config(state="disabled")
        elif wybrana_odpowiedz == odp_h_sprawdzenie:
            top = Toplevel()
            top.title(odp_h_sredni_strip)
            a = Image.open(f"sredni_zdjecia/{odp_h_sredni_strip}.gif")
            a1 = ImageTk.PhotoImage(a)
            ashowinfo = tk.Label(top, image=a1, width=400, height=400)
            ashowinfo.image = a1
            ashowinfo.pack()
            przycisk8_sredni.config(state="disabled")
        dodawanie_bledow(bledy_s_var)
        if bledy > 4:
            elo_label.pack_forget()
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
    elo_label.pack()
    bledy_st_label = tk.Label(root, textvariable=bledy_st_var)
    bledy_st_label.pack()
    polskie = tk.Label(root, textvariable=pl_var)
    polskie.pack()
    angielskie = tk.Label(root, textvariable=en_czesci_var)
    angielskie.pack()
    dobre_samo_tekst = tk.Label(root, text="Dobre samogłoski:")
    dobre_samo_tekst.pack()
    dobre_samo = tk.Label(root, textvariable=dobre_samo_var, fg="green")
    dobre_samo.pack()
    zle_samo_tekst = tk.Label(root, text="Złe samogłoski:")
    zle_samo_tekst.pack()
    zle_samo = tk.Label(root, textvariable=zle_samo_var, fg="red")
    zle_samo.pack()
    samogloska_entry = tk.Entry(root, textvariable=samogloska_entry_var)
    samogloska_entry.pack()
    samogloska_guzik = tk.Button(root, text="Sprawdź", command=lambda: sprawdzanie_srednio_trudne())
    samogloska_guzik.pack()
    samo = samogloska_strip.split("#")

dobre = []
zle = []
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
                elo_label.pack_forget()
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
                bledy_st_label.pack_forget()
                polskie.pack_forget()
                angielskie.pack_forget()
                dobre_samo_tekst.pack_forget()
                dobre_samo.pack_forget()
                zle_samo_tekst.pack_forget()
                zle_samo.pack_forget()
                samogloska_entry.pack_forget()
                samogloska_guzik.pack_forget()
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
            elo_label.pack_forget()
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
    elo_label.pack()
    bledy_trudne_label = tk.Label(root, textvariable=bledy_t_var)
    bledy_trudne_label.pack()
    polish_label = tk.Label(root, textvariable=trudny_pl)
    polish_label.pack()
    input_label = tk.Entry(root, textvariable=trudny_input)
    input_label.pack()
    wprowadzona_odpowiedz = tk.Label(root, textvariable=wprowadzony_text, fg="green")
    zatwierdz = tk.Button(root, text="Zatwierdź", command=lambda: sprawdz_trudny())
    zatwierdz.pack()

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

            elo_label.pack_forget()
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
            bledy_trudne_label.pack_forget()
            polish_label.pack_forget()
            input_label.pack_forget()
            zatwierdz.pack_forget()
            wprowadzona_odpowiedz.pack_forget()
            trudny()
    else:
        dodawanie_bledow(bledy_t_var)
        literki_trudny()
        if bledy > 4:
            elo_label.pack_forget()
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

    # wprowadzona_odpowiedz.pack()

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
    wprowadzona_odpowiedz.pack()


root = tk.Tk()
root.title("Duolingo")
root.geometry("900x650")
root.resizable(False, False)

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

elo_label = tk.Label(root, textvariable=elo_var)

ogolne_punkty_label = tk.Label(root, textvariable=ogolne_punkty_var)
ogolne_punkty_label.pack()
PoziomLatwy = tk.Button(root, text="Poziom Łatwy", command=latwy)
PoziomLatwy.pack()
PoziomSredni = tk.Button(root, text="Poziom Średni", command=sredni)
PoziomSredni.pack()
PoziomSredniotrudny = tk.Button(root, text="Poziom Średnio-trudny", command=srednio_trudny)
PoziomSredniotrudny.pack()
PoziomTrudny = tk.Button(root, text="Poziom Trudny", command=trudny)
PoziomTrudny.pack()

root.mainloop()
