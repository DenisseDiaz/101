#importar al modulo time

import time 

#crear variable segundo que pide el tiempo en segunds
seconds= input("Ingresa el tiempo en segundos")

#define la funcion cuenta atras
def cuenta_atras(seconds):
    #obtener los residuos
    while seconds>0:
      
      min =int(seconds/60)
      sec= int(seconds% 60)

      timer=f'{min}:{sec}'

      print(timer,end='\r')
      time.sleep(1)
      seconds-=1

    print("se acabo el tiempo")

cuenta_atras(int(seconds))