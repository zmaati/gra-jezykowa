import tkinter as tk
import mysql.connector as baza

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


root = tk.Tk()
root.title("Duolingo")
root.geometry("600x400")


PoziomLatwy = tk.Button(root, text="Poziom Łatwy")
PoziomLatwy.pack()
PoziomSredni = tk.Button(root, text="Poziom Średni")
PoziomSredni.pack()
PoziomSredniotrudny = tk.Button(root, text="Poziom Średnio-trudny")
PoziomSredniotrudny.pack()
PoziomTrudny = tk.Button(root, text="Poziom Trudny")
PoziomTrudny.pack()


root.mainloop()