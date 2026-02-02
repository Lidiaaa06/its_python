from datetime import date
from registro_elettronico.studente import Studente 

def main():


    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    studente1 = Studente(nome,cognome)
    studente1.data_nascita = date(1990,1,1)
    
    print(f"{nome}\t{cognome} : {studente1.calcola_eta()}")
   
    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    studente2 = Studente()
    studente2.data_nascita = date(2000,1,12)

    print(f"{nome}\t{cognome} : {studente2.calcola_eta()}")

    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    studente3 = Studente()
    studente3.data_nascita = date(2010,1,13)

    print(f"{nome}\t{cognome}: {studente3.calcola_eta()}")


if __name__ == "__main__":
    main()
