#inicio
import random
paises={1:'Brasil'
  ["1 cruzador",
  "2 torpedeiro",
  "1 destroyer",
  "1 couracado",
  "1 porta-avioes"], 
  2:'França'
  ["3 cruzador",
  "1 porta-avioes",
   "1 destroyer",
   "1 submarino",
   "1 couracado"],
 3:'Austrália'
 ["1 couracado",
   "3 cruzador",
   "1 submarino",
   "1 porta-avioes",
   "1 torpedeiro"],
  4:'Rússia'
   ["1 cruzador",
   "1 porta-avioes",
   "2 couracado",
   "1 destroyer",
   "1 submarino"],
 5:'Japão'
 ["2 torpedeiro",
   "1 cruzador",
   "2 destroyer",
   "1 couracado",
   "1 submarino"]}
lista_pais=[]
for pais in paises.keys():
    lista_pais.append(pais)   
jogador1=input('escolhe o um numero para seu pais?')

for PAIS in lista_pais:
    jogador1=random.choice(lista_pais)
    jogador2=random.choice(lista_pais)
while jogador1==jogador2:
    jogador2=random.choice(lista_pais)
lista_jogador=[jogador1,jogador2]

