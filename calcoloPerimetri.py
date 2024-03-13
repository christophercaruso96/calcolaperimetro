from funzioniGeometria import *

nome_figura = ""

while True:
    try:
        nome_figura = str (input("Inserisci una figura geometrica tra le seguenti: Quadrato, Rettangolo, Cerchio\n"))
    except ValueError:
        print ("Inserisci una stringa!\n")
    if (nome_figura != ""):
        break

valore_perimetro = calcolaPerimetro(nome_figura)

if (valore_perimetro):
    print ("Il valore del perimetro/circonferenza risulta essere il seguente. 2p = ", valore_perimetro)
