#calcola la media globale dei voti di un alunno,
#calcola in maniera pesata sulla base delle materie
#
import random
def main():

    MATERIE = [
        {'nome': "matematica", 'cfu':30},
        {'nome': "italiano", 'cfu':25},
        {'nome': "storia", 'cfu':20},
        {'nome': "informatica", 'cfu':30},
        {'nome': "ed. fisica", 'cfu':10},
        {'nome': "religione", 'cfu':5}
    ]

    #generare in maniera randomica una lista di voti(da 1 a 10)
    #10 voti per materia
    #stampare l'output con la media dei vorti per materia e la media pesata globale

    cfu_somma=0
    media_pesata=0
    somma_totale=0
    media_globale=0

    for materia in MATERIE:
        somma=0
        media=0
        for _ in range(10):
            voti = random.randint(1, 10)
            somma+=voti
        media = somma/ 10
        print(f"{materia['nome']}:  media={media:.2f}")
        cfu_somma+=materia['cfu']
        media_pesata=media*materia['cfu']
        somma_totale+=media_pesata
    media_globale=somma_totale/cfu_somma
    print(f"media globale: {media_globale:.2f}")

def mio_range_genexpr(start: int, end: int):
    i = start
    while i < end :
        yield i 
        i+= 1

 

main()

print(mio_range_genexpr(5,15)) 

def increment_generator(step: int =1):
    i = 0
    while i < 2 :
        yield i 
        i+= step
        
incrementatore = increment_generator()

val1 = next(incrementatore)
val2 = next(incrementatore)
val3 = next(incrementatore)
   