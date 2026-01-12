nome = input("inserisci il tuo nome: ")
print(f"Hello,{nome}") #commento 

eta= int (input (f"Ciao,{nome}!, Inserisci la tua età: "))
print(f"La tua età è : {eta}")
print(f"il tuo anno di nascita è: {2026 - eta }")

if nome =="":
    nome="World"
elif nome=="Lidia":
    pass

i=0
while i<10:
    print(f"il numero è: {i}")

    i += 1

for i in [0,11,21,34]:
    print(f"il numero è: {i}")

for i in range [0,101]:
    print(f"il numero è: {i}")
    

def compreso(num,max,min):
    return min < num < max

compreso (10,2,20)
       
def crazy_input(message:str, is_int:bool)-> int | str :   #la "->" indica il tipo che restituisce 
    val: str = input(message)
    
    if is_int:
        return int(val)
    
    else:
        return val
