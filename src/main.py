def main():
   
   # Array --> lista

    lista = [1,1,2,2,3,3,4,4]
    lista[0] = 5 

   # print(lista[3])

    lista.append(6)#aggiunge il 6 in fondo
    lista.insert(3,7)#aggiunge il 7 in posizione 3

    print (lista[2:4])
    
    print (lista[:-1])

    print(lista)
    
    ultimo = lista.pop()#toglie l'ultimo elemento

    len(lista)

    lista.count(1)#return di quante volte è presente in numero nelle parentesi

    tupla = (1,1,2,2,3,3,4,4) #elementi immutabili e definiti dall'inzio

    tupla2 = tuple(lista)

    print(tupla)

    _set = {1,1,2,2,3,3,4,4}# gli elementi non si possono ripetere 

    print(_set)

    set1 = set(lista)

    print(lista.sort())#ordina

    mistero = {
        'prova': 1,
        'valore': 2,
        'chiave': 3
    }#dizionario con stringhe 

    mistero['chiave']#visualizzazione del valore del dizionario
    mistero['mia_chiave']= 101 #creo la chiave e gli assegno un valore 

    

main()
