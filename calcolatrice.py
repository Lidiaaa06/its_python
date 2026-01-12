print("\n Calcolatrice \n")
numero1=int(input("Inserisci il primo valore: "))
numero2=int(input("Inserisci il secondo valore: "))
operatore=str(input("Inserisci l'operatore: "))

if operatore == "+":
    risultato=numero1 + numero2
    print(f"Il risultato è: {risultato}")

elif operatore == "-":
    risultato=numero1 - numero2
    print(f"Il risultato è: {risultato}")

elif operatore == "*":
    risultato=numero1 * numero2
    print(f"Il risultato è: {risultato}")

elif operatore == "/":
    risultato=numero1 / numero2
    print(f"Il risultato è: {risultato}")
    
