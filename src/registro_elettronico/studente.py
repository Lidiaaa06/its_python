from datetime import date

class Studente:
    nome : str
    cognome : str

    data_nascita : date
    luogo_nascita : str


    def __init__(self,nome: str = "",cognome : str = ""):
        self.nome = ""
        self.cognome = ""

        self.data_nascita = date(1970,1,1)
        self.luogo_nascita = ""


    def calcola_eta(self):
        today = date.today()
        age = today.year - self.data_nascita.year
        if (today.month, today.day) < (self.data_nascita.month, self.data_nascita.day):
            age -= 1
        return age

class Voti:
    nome_materia : str
    valutazione : float
    data_valutazione : date 
