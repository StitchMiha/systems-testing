# TODO Creati un stub si o functie fake care sa simuleze 
# functionalitatea metodei get(cheie_unica) pe o baza de date. 
# Puteti sa folositi baza de date creata anterior. 

from ex4.ex4 import Person


class DatabaseStub:
    def get(self, key):
        if key == "test@mail.com":
            return Person("Test User", 25, "test@mail.com")
        return None
    
    