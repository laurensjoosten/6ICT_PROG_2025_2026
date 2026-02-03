""" Oefening 2 (   / 6): API -- CO2 uitstoot van websites 

API: https://api.websitecarbon.com/

Voorbeelden (CO2 uitstoot afgerond op 3 cijfers na de komma):
    Opgelet! De API geeft 2 soorten CO2 terug. Kies voor de optie 'grid'.

    Als jouw script dezelfde prints heeft als onderstaande voorbeelden,
    dan mag je ervanuit gaan dat het script correct gemaakt is.

    Website 1:
        Input || Welke website opzoeken: https://www.w3schools.com/
        Print || Deze website is 1578905 bytes groot, en veroorzaakt 0.397 gram CO2 uitstoot.
    Website 2:
        Input || Welke website opzoeken: https://github.com/
        Print || Deze website is 1948243 bytes groot, en veroorzaakt 0.490 gram CO2 uitstoot.
    Website 3:
        Input || Welke website opzoeken: abc
        Print || Geen geldige site opgegeven.

"""

import requests
import json

website = input("Welke website opzoeken: ")


url = f"https://api.websitecarbon.com/site?url={website}"

try:
    response = requests.get(url)
    data = response.json()
    with open(r"6ICT_PROG_2025_2026/hfst_4 API/oefenmee/co2_uitstoot_data.json", "w") as fp:
        json.dump(response, fp)

    
    if "error" in data:
        print("Geen geldige site opgegeven.")
    else:
        bytes = data["bytes"]
        co2 = data["statistics"]["co2"]["gram"]   
    
        print(f"Deze website is {bytes} bytes groot, en veroorzaakt {co2} gram CO2 uitstoot.")

except:
    print("Geen geldige site opgegeven.")
