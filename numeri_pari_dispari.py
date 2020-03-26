import time as t

print("Titolo : numeri primi")
print("Questo piccolo programma preso un numero in INPUT ")
print("stampa tutti i numeri primi precedenti \n")

print("Avvio... \n")
risposta = 'SI'


def cerca_numeri_primi(n):
    return n%2

while(risposta == 'SI'):

    #acquisisco il numero in input
    n = input("Inserisci un numero:")
    print("Numero inserito :"+n)
    tempo = 10

    if((int(n))<=0):
        print("Numero non valido")
        tempo = 0
        break;
    
    elif((int(n)) ==1):
        print("Risultato trovato : [1]")
        break;
    else:
        print("Sto cercando i numeri.. attendere un attimo")
        print ("__________________________________________")
        
        print("Numeri primi trovati : ")
        cinque_col = i = 0
        
        print ("__________________________________________")
        while(i < (int(n))):
            
            if(cerca_numeri_primi(i)):
                
                stringa_output = "|"+str(i)
                
                if(cinque_col < 5):
                    print (stringa_output,end='')
                else:
                    print (stringa_output+"|")
                    cinque_col = 0
                    
                cinque_col = cinque_col+1
            i=i+1
            
        print("")    
        print ("__________________________________________")    

    t.sleep(tempo)
    risposta = input(" \nVuoi continuare (SI,NO)?\n")

print("arrivederci")
