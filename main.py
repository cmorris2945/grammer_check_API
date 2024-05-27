### This API will send a post some text to a server
# and it will check our grammer for us, then it will send it back to us or ##our client
import requests
import json

url = "https://api.languagetool.org/v2/check"
data = {'text': 'Tis is a nic day jackass!', 'language': 'auto'}

response = requests.post(url, data=data)
result = json.loads(response.text)

print(result)
