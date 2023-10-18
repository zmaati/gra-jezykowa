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


    odp_a = connect.cursor()
    odp_a.execute(f"SELECT odp_a FROM latwy WHERE id = {losowe}")
    odp_a_wynik = odp_a.fetchone()
    odp_a_wynik_str = str(odp_a_wynik)
    odp_a_strip = odp_a_wynik_str.strip('(),\'')
    print(odp_a_strip)
    
    przycisk1 = tk.Button(root,text=odp_a_strip).pack()
    przycisk2 = tk.Button(root,text="Potem").pack()
    przycisk3 = tk.Button(root,text="Potem").pack()
    przycisk4 = tk.Button(root,text="Potem").pack()
    przycisk5 = tk.Button(root,text="Potem").pack()
    przycisk6 = tk.Button(root,text="Potem").pack()
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