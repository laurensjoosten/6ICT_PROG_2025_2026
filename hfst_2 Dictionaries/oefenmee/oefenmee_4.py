# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}

fruit = input("Welk soort fruit zoek je: ")

if fruit in fruitmand:
    print( fruitmand[fruit] )

else:
    print(f"Kon {fruit} niet vinden in fruitmand")