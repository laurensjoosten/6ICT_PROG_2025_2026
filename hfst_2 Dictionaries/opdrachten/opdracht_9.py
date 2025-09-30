# Start de opdracht met onderstaande code.
deelnemers = ["Lucas", "Emma", "Jan", "Piet", "Maud"]

deelnemers_talen = {    
    "Lucas": "python",    
    "Piet": "assembly",    
    "Maud": "ruby"
}

for index, deelnemer in enumerate(deelnemers):
    if deelnemer in deelnemers_talen:
        print(f"Dag {deelnemer} bedankt voor de poll in te vullen")
    else:
        print(f"Dag {deelnemer} gelieve de poll in te vullen ")
        vraag = input("  - Wat is je favoriete programmeertaal: ")
        deelnemers_talen[deelnemer] = vraag
        

    
print(deelnemers_talen)
