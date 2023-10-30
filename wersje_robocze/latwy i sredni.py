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



def losowanie():
        global losowe_dobra_odp_latwy,losowe_dobra_odp_sredni, losowe_a, losowe_b, losowe_c, losowe_d, losowe_e, losowe_f,losowe_g,losowe_h
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
        #losowanie dobrej odp
        losowe_dobra_odp_latwy = random.choice([losowe_a, losowe_b, losowe_c, losowe_d, losowe_e, losowe_f])
        losowe_dobra_odp_sredni = random.choice([losowe_a,losowe_b,losowe_c,losowe_d,losowe_e,losowe_f,losowe_g,losowe_h])
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
    global zapytanie_wynik_strip
    zapytanie_wynik_strip = zapytanie_wynik_str.strip('(),\'')
    print(zapytanie_wynik_strip)
    
    
    odp_a = connect.cursor()
    odp_a.execute(f"SELECT odp FROM latwy WHERE id = {losowe_a}")
    odp_a_wynik = str(odp_a.fetchone())
    global odp_a_strip
    odp_a_strip = odp_a_wynik.strip('(),\'')
    latwy_guzik1.set(odp_a_strip)
    print(odp_a_strip)
    odp_b = connect.cursor()
    odp_b.execute(f"SELECT odp FROM latwy WHERE id = {losowe_b}")
    odp_b_wynik = str(odp_b.fetchone())
    global odp_b_strip
    odp_b_strip = odp_b_wynik.strip('(),\'')
    latwy_guzik2.set(odp_b_strip)
    print(odp_b_strip)
    odp_c = connect.cursor()
    odp_c.execute(f"SELECT odp FROM latwy WHERE id = {losowe_c}")
    odp_c_wynik = str(odp_c.fetchone())
    global odp_c_strip
    odp_c_strip = odp_c_wynik.strip('(),\'')
    latwy_guzik3.set(odp_c_strip)
    print(odp_c_strip)
    odp_d = connect.cursor()
    odp_d.execute(f"SELECT odp FROM latwy WHERE id = {losowe_d}")
    odp_d_wynik = str(odp_d.fetchone())
    global odp_d_strip
    odp_d_strip = odp_d_wynik.strip('(),\'')
    latwy_guzik4.set(odp_d_strip)
    print(odp_d_strip)
    odp_e = connect.cursor()
    odp_e.execute(f"SELECT odp FROM latwy WHERE id = {losowe_e}")
    odp_e_wynik = str(odp_e.fetchone())
    global odp_e_strip
    odp_e_strip = odp_e_wynik.strip('(),\'')
    latwy_guzik5.set(odp_e_strip)
    print(odp_e_strip)
    odp_f = connect.cursor()
    odp_f.execute(f"SELECT odp FROM latwy WHERE id = {losowe_f}")
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
        dodawanie_bledow_latwe()

def sredni():
    zapomnij_guziki()
    losowanie()
    global odp_a_sredni_strip,odp_b_sredni_strip,odp_c_sredni_strip,odp_d_sredni_strip,odp_e_sredni_strip,odp_f_sredni_strip,odp_g_sredni_strip,odp_h_sredni_strip
    global odp_a_sprawdzenie,odp_b_sprawdzenie,odp_c_sprawdzenie,odp_d_sprawdzenie,odp_e_sprawdzenie,odp_f_sprawdzenie,odp_g_sprawdzenie,odp_h_sprawdzenie
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

    global odp_label
    global przycisk1_sredni
    global przycisk2_sredni    
    global przycisk3_sredni
    global przycisk4_sredni
    global przycisk5_sredni
    global przycisk6_sredni
    global przycisk7_sredni
    global przycisk8_sredni    
    odp_label = tk.Label(root,textvariable=sredni_odp_label)
    odp_label.pack()
    przycisk1_sredni = tk.Button(root,textvariable=sredny_guzik1,command=lambda: (sprawdzenie_dobrej_odpowiedzi_sredni(odp_a_sprawdzenie,przycisk1_sredni),losowanie))
    przycisk1_sredni.pack()
    przycisk2_sredni = tk.Button(root,textvariable=sredny_guzik2,command=lambda: (sprawdzenie_dobrej_odpowiedzi_sredni(odp_b_sprawdzenie,przycisk2_sredni),losowanie))
    przycisk2_sredni.pack()
    przycisk3_sredni = tk.Button(root,textvariable=sredny_guzik3,command=lambda: (sprawdzenie_dobrej_odpowiedzi_sredni(odp_c_sprawdzenie,przycisk3_sredni),losowanie))
    przycisk3_sredni.pack()
    przycisk4_sredni = tk.Button(root,textvariable=sredny_guzik4,command=lambda: (sprawdzenie_dobrej_odpowiedzi_sredni(odp_d_sprawdzenie,przycisk4_sredni),losowanie))
    przycisk4_sredni.pack()
    przycisk5_sredni = tk.Button(root,textvariable=sredny_guzik5,command=lambda: (sprawdzenie_dobrej_odpowiedzi_sredni(odp_e_sprawdzenie,przycisk5_sredni),losowanie))
    przycisk5_sredni.pack()
    przycisk6_sredni = tk.Button(root,textvariable=sredny_guzik6,command=lambda: (sprawdzenie_dobrej_odpowiedzi_sredni(odp_f_sprawdzenie,przycisk6_sredni),losowanie))
    przycisk6_sredni.pack()
    przycisk7_sredni = tk.Button(root,textvariable=sredny_guzik7,command=lambda: (sprawdzenie_dobrej_odpowiedzi_sredni(odp_g_sprawdzenie,przycisk7_sredni),losowanie))
    przycisk7_sredni.pack()
    przycisk8_sredni = tk.Button(root,textvariable=sredny_guzik8,command=lambda: (sprawdzenie_dobrej_odpowiedzi_sredni(odp_h_sprawdzenie,przycisk8_sredni),losowanie))
    przycisk8_sredni.pack()
def sprawdzenie_dobrej_odpowiedzi_sredni(wybrana_odpowiedz,przycisk):
    if dobra_odp_sredni_strip == wybrana_odpowiedz:
        dodawanie_elo()
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
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk1_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_b_sprawdzenie:
             top = Toplevel()
             top.title(odp_b_sredni_strip)
             a = Image.open(f"sredni_zdjecia/{odp_b_sredni_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk2_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_c_sprawdzenie:
             top = Toplevel()
             top.title(odp_c_sredni_strip)
             a = Image.open(f"sredni_zdjecia/{odp_c_sredni_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk3_sredni.config(state="disabled")     

        elif wybrana_odpowiedz == odp_d_sprawdzenie:
             top = Toplevel()
             top.title(odp_d_sredni_strip)
             a = Image.open(f"sredni_zdjecia/{odp_d_sredni_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk4_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_e_sprawdzenie:
             top = Toplevel()
             top.title(odp_e_sredni_strip)
             a = Image.open(f"sredni_zdjecia/{odp_e_sredni_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk5_sredni.config(state="disabled")

        elif wybrana_odpowiedz == odp_f_sprawdzenie:
             top = Toplevel()
             top.title(odp_f_sredni_strip)
             a = Image.open(f"sredni_zdjecia/{odp_f_sredni_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk6_sredni.config(state="disabled")
        elif wybrana_odpowiedz == odp_g_sprawdzenie:
             top = Toplevel()
             top.title(odp_g_sredni_strip)
             a = Image.open(f"sredni_zdjecia/{odp_g_sredni_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk7_sredni.config(state="disabled")
        elif wybrana_odpowiedz == odp_h_sprawdzenie:
             top = Toplevel()
             top.title(odp_h_sredni_strip)
             a = Image.open(f"sredni_zdjecia/{odp_h_sredni_strip}.gif")
             a1 = ImageTk.PhotoImage(a)
             ashowinfo = tk.Label(top, image=a1,width=400,height=400)
             ashowinfo.image = a1
             ashowinfo.pack()
             przycisk8_sredni.config(state="disabled")
        dodawanie_bledow_latwe()

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

sredni_odp_label = tk.StringVar()
sredny_guzik1 = tk.StringVar()
sredny_guzik2 = tk.StringVar()
sredny_guzik3 = tk.StringVar()
sredny_guzik4 = tk.StringVar()
sredny_guzik5 = tk.StringVar()
sredny_guzik6 = tk.StringVar()
sredny_guzik7 = tk.StringVar()
sredny_guzik8 = tk.StringVar()

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