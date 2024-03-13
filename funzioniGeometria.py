import math

def validazioneNumInput(input_message, error_message):
    input_value = 0
    while True:
        try:
            input_value = float (input (input_message))
        except ValueError:
            print (error_message)
        if (input_value != 0):
            break
    return input_value

def calcolaPerimetro(figura):
    dim_lato = 0
    dim_base = 0
    dim_altezza = 0
    dim_raggio = 0
    if (figura.upper() == "QUADRATO"):
        dim_lato = validazioneNumInput("Inserisci dimensione del lato in cm:\n", "Per favore inserisci un valore numerico!\n")
        return dim_lato*4
    elif (figura.upper() == "RETTANGOLO"):
        dim_base = validazioneNumInput("Inserisci dimensione della base in cm:\n", "Per favore inserisci un valore numerico!\n")
        dim_altezza = validazioneNumInput("Inserisci dimensione dell' altezza in cm:\n", "Per favore inserisci un valore numerico!\n")
        if (dim_base == dim_altezza):
            print ("Base e altezza coincidono, si tratta di un quadrato!")
            return dim_base*4
        else:
            return dim_base*2 + dim_altezza*2
    elif (figura.upper() == "CERCHIO"):
        dim_raggio = validazioneNumInput("Inserisci dimensione del raggio in cm:\n", "Per favore inserisci un valore numerico!\n")
        return dim_raggio*2*math.pi
    else:
        print ("Non è stato inserito nessuno degli input previsti!")

