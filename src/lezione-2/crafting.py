#implementare un sistema di crafting per un gioco di ruolo
#definire le classi per gli oggetti, le ricette di crafting e
#permettere al giocatore di combinare oggetti per crearne di nuovi
#


inventory = {
    "acqua": 1,
    "fuoco": 1,
    "aria": 1,
    "terra": 1
}

recipes = {
    frozenset(["acqua", "terra"]): "fango",
    frozenset(["aria", "acqua"]): "pioggia",
    frozenset(["fuoco", "terra"]): "lava",
    frozenset(["aria", "fuoco"]): "energia",
    frozenset(["lava", "aria"]): "pietra",
    frozenset(["fango", "fuoco"]): "argilla"
}


def combina(elemento1, elemento2):
    # Controllo se il giocatore possiede gli elementi
    if elemento1 not in inventory or elemento2 not in inventory:
        print("Non succede nulla...")
        return

    combinazione = frozenset([elemento1, elemento2])

    if combinazione in recipes:
        risultato = recipes[combinazione]

        # Se l'elemento è nuovo, lo aggiungiamo
        if risultato not in inventory:
            inventory[risultato] = 1
            print(f" Hai scoperto un nuovo elemento: {risultato}!")
        else:
            inventory[risultato] += 1
            print(f"Hai creato di nuovo: {risultato}")
    else:
        print(" La combinazione non produce nulla.")


print("Hai accesso a elementi primordiali.")
print("Prova a combinarli. Scrivi 'esci' per terminare.\n")

while True:
    e1 = input("Primo elemento: ").lower()
    if e1 == "esci":
        break

    e2 = input("Secondo elemento: ").lower()
    if e2 == "esci":
        break

    combina(e1, e2)

