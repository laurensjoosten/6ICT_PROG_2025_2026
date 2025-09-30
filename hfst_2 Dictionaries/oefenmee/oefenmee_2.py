# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}

fruit = "banaan"

nieuw_fruit  = "mango"
nieuw_aantal = 1
fruitmand[nieuw_fruit] = nieuw_aantal


fruit = "banaan"
nieuw_aantal = 8
fruitmand[fruit] = nieuw_aantal

fruit = "kers"
nieuw_aantal = 43

fruitmand[fruit] = nieuw_aantal

print( fruitmand )
