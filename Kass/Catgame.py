import random


sündmused = [
    ("Leidsid mahajäetud toiduvaru", +2, 0, 0),
    ("Sind ründas metskass!", -1, -1, -5),
    ("Sõbralik kass jagas toitu", +1, 0, +3),
    ("Sa eksisid ära ja väsisid", 0, -1, -10),
    ("Leidsid varjupaiga ja puhkasid", 0, 0, +10),
    ("Toit läks halvaks!", -2, 0, 0)
]


class Kass:

    def __init__(self, nimi, health=5, food=3, energy=50, max_päevi=10):
        self.nimi = nimi
        self.health = health
        self.food = food
        self.energy = energy
        self.max_päevi = max_päevi
        self.päev = 1

    def staatus(self):
        print(f"\n Päev {self.päev}/{self.max_päevi}")
        print(f" {self.nimi} – Tervis: {'/' * self.health} | Toit: {'/' * self.food} | Energia: {self.energy}")

    def puhka(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 10
            print(f"{self.nimi} puhkas ja sai +10 energiat.")
        else:
            print("Pole toitu! Ei saa puhata.")

    def liigu(self):
        self.energy -= 5
        print(f"{self.nimi} liikus edasi. -5 energiat.")

    def sündmus(self):
        sündmus = random.choice(sündmused)
        nimi, food_muudatus, health_muudatus, energy_muudatus = sündmus

        print(f"SÜNDMUS: {nimi}")
        self.food += food_muudatus
        self.health += health_muudatus
        self.energy += energy_muudatus

   
        self.food = max(0, self.food)
        self.health = max(0, self.health)
        self.energy = max(0, self.energy)

    def varu_toitu(self):
        print(f"{self.nimi} otsib toitu...")
        edu = random.randint(0, 1)
        if edu:
            saadud = random.randint(1, 3)
            self.food += saadud
            print(f"Leidsid {saadud} ühikut toitu!")
        else:
            print("Ei leidnud midagi...")

    def käik(self):
        print("\nValikud: [puhka] [liigu] [risk] [otsi]")
        tegevus = input("Vali tegevus: ").strip().lower()

        if tegevus == "puhka":
            self.puhka()
        elif tegevus == "liigu":
            self.liigu()
        elif tegevus == "risk":
            self.sündmus()
        elif tegevus == "otsi":
            self.varu_toitu()
        else:
            print("Tundmatu valik, midagi ei juhtunud.")

    def mängi(self):
        print(f" Tere tulemast ellujäämismängu, {self.nimi}!")
        while self.päev <= self.max_päevi and self.health > 0:
            self.staatus()
            self.käik()
            self.päev += 1

        self.staatus()
        if self.health <= 0:
            print(f"\n {self.nimi} kahjuks ei jäänud ellu...")
        else:
            print(f"\n {self.nimi} jäi ellu {self.max_päevi} päeva! Tubli!")

if __name__ == "__main__":
    nimi = input("Sisesta oma kassi nimi: ")
    minu_kass = Kass(nimi)
    minu_kass.mängi()