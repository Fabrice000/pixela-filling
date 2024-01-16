import requests 
import datetime as dt
# first you need to create your account on pixela
USERNAME = "YOUR USERNAME"
TOKEN = "YOUR TOKEN"
user_params = {
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# to verify that you can connect use this
# response = requests.post(url=PIXELA_ENDPOINT,json=user_params)
# print(response.text)
graph_config ={
    "id":"graph1",
    "name":"your activity",
    "unit":"Hr",
    "type":"int",
    "color":"ajisai"
}
headers = {
    "X-USER-TOKEN":TOKEN
}
today = dt.datetime.now()

response = requests.post(url=GRAPH_ENDPOINT,json=graph_config,headers=headers)
print(response.text)
#entry_params = {
   # "date":today.strftime("%Y%m%d"),
    # "quantity":"7",
#}
# for delete your post use this
# response = requests.delete(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}",headers=headers)
# print(response.text)