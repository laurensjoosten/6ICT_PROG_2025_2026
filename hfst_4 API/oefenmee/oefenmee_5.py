import requests, json

url = "https://v2.jokeapi.dev/joke/Programming?amount=3"
response_json = requests.get(url).json() # Haal JSON uit response.

for cijfer in range(3):
    if ("joke" in response_json["jokes"][cijfer]):
        print(response_json["jokes"][cijfer]["joke"])     # De grap
    else:
        print(response_json["jokes"][cijfer]["setup"])    # De setup
        print(response_json["jokes"][cijfer]["delivery"]) # De punchline

with open("6ICT_PROG_2025_2026/hfst_4 API/oefenmee/programmeergrappen_data.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")
