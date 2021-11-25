import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = "source=uz&target=en&q=Salom Dunyo!"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "ec26a7ec78msh531fa5521adb411p1157e0jsn4224d1eb51c1"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text["data"])
print(response.text)