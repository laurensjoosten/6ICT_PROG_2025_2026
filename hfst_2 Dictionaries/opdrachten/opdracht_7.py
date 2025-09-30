artikelen = { 
    "appels": 1.50,
    "nananen": 0.75,
    "brood": 2.30,
    "melk": 1.20,
    "eieren": 2.00,
    "kaas": 3.50,
    "kip": 5.75,
    "tomaten": 1.00,
    "aardappelen": 0.80,
    "ontbijtgranen": 3.25
}


artikel = input("Wat wil je kopen: ")
for sleutel, artikel in artikelen.items():
    if artikel in artikelen:
        teller_prijs = 0
        teller_hoeveelheid = 0
        print(f"{artikel} toegevoegd")
        teller_prijs = (teller_prijs + artikel)
        teller_hoeveelheid = (teller_hoeveelheid + 1)
        print(f"U heeft {teller_hoeveelheid} artikelen gekocht. Deze kosten samen {teller_prijs} euro")

    
    
    elif artikel == "STOP":
        break
    else:
        print(f"{artikel} niet gevonden")

