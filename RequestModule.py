import http
import requests

req=requests.get("https://ekantipur.com/");
print(req.text)