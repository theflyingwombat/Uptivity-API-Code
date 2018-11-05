import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

baseUrl = "http://uptivitystore.loves.com:2012/Webapi.aspx"

querystring = {"requestid": "17",
               "type": "test"}

r = requests.post(baseUrl, params=querystring, verify=False)

print(r)
print(r.text)
