import tkinter as tk
from tkinter import filedialog
import os

app = tk.Tk()
app.geometry("400x400")
app.resizable(False,False)

Do_Pliku_Var = tk.StringVar()
Ile_Liter_Var = tk.IntVar()
Ile_Liter_Var.set("")

#tk.Label(text="Wpisz tekst który chcesz zaszyfrować").pack()
#Do_Pliku_Entry = tk.Entry(textvariable=Do_Pliku_Var).pack()
tk.Label(text="O ile liter chcesz przesunąć tekst").pack()
Ile_Liter_Entry = tk.Entry(textvariable=Ile_Liter_Var).pack()
def sciezka():
    tekst_pliku = Do_Pliku_Var.get()
    ile_liter = Ile_Liter_Var.get()
    file = filedialog.askopenfile()
    file_path = os.path.abspath(file.name)
    #fw = open(file_path,"w")
    #fw.write(tekst_pliku)
    #fw.close()
    fw = open(file_path,"r")
    tekst = fw.read()
    print(tekst)

    szyfr = "".join(chr(((ord(char) + ile_liter) % 26) + 97) for char in tekst)  
    fw.close()
    file_name = input("Podaj nazwe nowego pliku ")
    file_name = file_name+".txt"
    fw = open(file_name, 'w')
    fw.write(szyfr)

przycisk = tk.Button(text="Wybierz Plik", command=sciezka).pack()

app.mainloop()    
