""" Voorbeelden (API geeft enkel Engelse zinnen terug):

Advies 1:
    Input || Topic for advice: spiders
    Print || Remember that spiders are more afraid of you, than you are of them.
Advies 2:
    Input || Topic for advice: teeth
    Print || You don't need to floss all of your teeth. Only the ones you want to keep.
Advies 3:
    Input || Topic for advice: programming
    Print || No advice slips found matching that search term.

"""

import requests
import json

query = input("Topic for advice: ")


url = f"https://api.adviceslip.com/advice/search/{query}"
response = requests.get(url)
respons_json = response.json()

with open(r"hfst_4 API\opdrachten\vragen.json", "w") as fp:
        json.dump(respons_json, fp)

if "slips" in respons_json: 
    advies = respons_json["slips"][0]["advice"]
    print(advies)

else:
    print("No advice slips found matching that search term.")