import requests, json

url = "https://api.adviceslip.com/advice/search/api"
response_json = requests.get(url).json()

with open("6ICT_PROG_2025_2026/hfst_4 API/oefenmee/adviceslip_data.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")
