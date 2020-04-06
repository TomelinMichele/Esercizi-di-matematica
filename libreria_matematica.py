import time as tempo
import math as matem

Class Operazioni_matematiche(self):
     
        def __init__(self):
            risultato=0
            
        def do_somma(self,a,b):
            return a+b
        
        def do_divisione(self,a,b):
            return a/b
        
        def do_sottrazione(self,a,b):
            return a-b
        
        def do_potenza(self,a):
            #primo parametro numero es 2
            return matem.pow(a,2)
        
        def do_potenza_n(self,a,b):
            #primo parametro numero es 2
            #secondo parametro esponente
            return matem.pow(a,b)
        
         def do_radice(self,a,b):
            #primo parametro radicando
            #secondo parametro esponente della radice
            
            return matem.pow(a,
