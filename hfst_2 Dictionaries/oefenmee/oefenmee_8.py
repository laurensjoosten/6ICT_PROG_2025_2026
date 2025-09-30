# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}

vraag = input("In welke stad bent u: ")
temp = steden_temp.get(vraag)

if vraag in steden_temp:
    print(f"Het is hier {temp} °C")
else:
    print("Het is hier ??? °C")