#TODO Creati o baza de date fake ce contine minim 500 de intrari. 
# O intrare este reprezentata de o instanta a clasei Person (pe care trebuie sa o creati) 
# care are minim 3 atribute (nume, varsta, email). Cheia unica este representata de adresa de mail. 

from dataclasses import dataclass
from faker import Faker


@dataclass
class Person:
    name: str
    age: int
    email: str


def create_fake_database(n=500):
    fake = Faker()
    db = {}

    for _ in range(n):
        profile = fake.simple_profile()
        name = profile["name"]
        email = fake.unique.email()
        birthdate = profile["birthdate"]
        age = fake.random_int(min=18, max=80)

        person = Person(name=name, age=age, email=email)
        db[email] = person

    return db


if __name__ == "__main__":
    database = create_fake_database(500)

    print(f"Number of entries: {len(database)}")

    for i, (email, person) in enumerate(database.items()):
        if i == 5:
            break
        print(person)