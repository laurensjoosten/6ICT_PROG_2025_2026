# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}

vraag = ''
while vraag != "stop":
    vraag = input("Welke gast zoek je? ")
    if vraag in gasten:   
        print(f"Welkom {gasten[vraag]} {vraag}. Kom binnen")
        gasten.pop(vraag)
    elif vraag not in gasten:
        print(f"De naam {vraag} staat niet in de lijst")
        
        
   
        







