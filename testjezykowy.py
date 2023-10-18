import tkinter as tk
import mysql.connector as baza
import random

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
    zapytanie_wynik_strip = zapytanie_wynik_str.strip('(),\'')
    print(zapytanie_wynik_strip)
    elo = 0
    odp_a = connect.cursor()
    odp_a.execute(f"SELECT odp_a FROM latwy WHERE id = {losowe}")
    odp_a_wynik = str(odp_a.fetchone())
    odp_a_strip = odp_a_wynik.strip('(),\'')
    print(odp_a_strip)
    odp_b = connect.cursor()
    odp_b.execute(f"SELECT odp_b FROM latwy WHERE id = {losowe}")
    odp_b_wynik = str(odp_b.fetchone())
    odp_b_strip = odp_b_wynik.strip('(),\'')
    print(odp_b_strip)
    odp_c = connect.cursor()
    odp_c.execute(f"SELECT odp_c FROM latwy WHERE id = {losowe}")
    odp_c_wynik = str(odp_c.fetchone())
    odp_c_strip = odp_c_wynik.strip('(),\'')
    print(odp_c_strip)
    odp_d = connect.cursor()
    odp_d.execute(f"SELECT odp_d FROM latwy WHERE id = {losowe}")
    odp_d_wynik = str(odp_d.fetchone())
    odp_d_strip = odp_d_wynik.strip('(),\'')
    print(odp_d_strip)
    odp_e = connect.cursor()
    odp_e.execute(f"SELECT odp_e FROM latwy WHERE id = {losowe}")
    odp_e_wynik = str(odp_e.fetchone())
    odp_e_strip = odp_e_wynik.strip('(),\'')
    print(odp_e_strip)
    odp_f = connect.cursor()
    odp_f.execute(f"SELECT odp_f FROM latwy WHERE id = {losowe}")
    odp_f_wynik = str(odp_f.fetchone())
    odp_f_strip = odp_f_wynik.strip('(),\'')
    print(odp_f_strip)
    def sprawdzenie_dobrej_odpowiedzi(wybrana_odpowiedz):
        if zapytanie_wynik_strip == wybrana_odpowiedz:
            print("Jest g")
        else:
            print("źle!")

    przycisk1 = tk.Button(root, text=odp_a_strip,command=lambda: (sprawdzenie_dobrej_odpowiedzi(odp_a_strip)))
    przycisk1.pack()
    przycisk2 = tk.Button(root, text=odp_b_strip, command=lambda: sprawdzenie_dobrej_odpowiedzi(odp_b_strip))
    przycisk2.pack()
    przycisk3 = tk.Button(root, text=odp_c_strip, command=lambda: sprawdzenie_dobrej_odpowiedzi(odp_c_strip))
    przycisk3.pack()
    przycisk4 = tk.Button(root, text=odp_d_strip, command=lambda: sprawdzenie_dobrej_odpowiedzi(odp_d_strip))
    przycisk4.pack()
    przycisk5 = tk.Button(root, text=odp_e_strip, command=lambda: sprawdzenie_dobrej_odpowiedzi(odp_e_strip))
    przycisk5.pack()
    przycisk6 = tk.Button(root, text=odp_f_strip, command=lambda: sprawdzenie_dobrej_odpowiedzi(odp_f_strip))
    przycisk6.pack()

def sredni():
    zapomnij_guziki()
    przycisk1 = tk.Button(root,text="Potem").pack()
    przycisk2 = tk.Button(root,text="Potem").pack()
    przycisk3 = tk.Button(root,text="Potem").pack()
    przycisk4 = tk.Button(root,text="Potem").pack()
    przycisk5 = tk.Button(root,text="Potem").pack()
    przycisk6 = tk.Button(root,text="Potem").pack()
def srednio_trudny():
    zapomnij_guziki()
    przycisk1 = tk.Button(root,text="Potem").pack()
    przycisk2 = tk.Button(root,text="Potem").pack()
    przycisk3 = tk.Button(root,text="Potem").pack()
    przycisk4 = tk.Button(root,text="Potem").pack()
    przycisk5 = tk.Button(root,text="Potem").pack()
    przycisk6 = tk.Button(root,text="Potem").pack()
def trudny():
    zapomnij_guziki()
    przycisk1 = tk.Button(root,text="Potem").pack()
    przycisk2 = tk.Button(root,text="Potem").pack()
    przycisk3 = tk.Button(root,text="Potem").pack()
    przycisk4 = tk.Button(root,text="Potem").pack()
    przycisk5 = tk.Button(root,text="Potem").pack()
    przycisk6 = tk.Button(root,text="Potem").pack()

root = tk.Tk()
root.title("Duolingo")
root.geometry("600x400")


PoziomLatwy = tk.Button(root, text="Poziom Łatwy",command=latwy)
PoziomLatwy.pack()
PoziomSredni = tk.Button(root, text="Poziom Średni",command=sredni)
PoziomSredni.pack()
PoziomSredniotrudny = tk.Button(root, text="Poziom Średnio-trudny",command=srednio_trudny)
PoziomSredniotrudny.pack()
PoziomTrudny = tk.Button(root, text="Poziom Trudny",command=trudny)
PoziomTrudny.pack()

root.mainloop()
