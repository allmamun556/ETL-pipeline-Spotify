import requests
import datetime
import base64
from urllib.parse import urlencode
client_id="1df3805bb6424abf82cb5b388389a0a0"
client_secret="77cfa385632b46dc9236d9aac46f1b4a"
client_creds = f"{client_id}:{client_secret}"


print(type(client_creds))

#base address of Web Api
# "https://accounts.spotify.com"
''' base address and token url is different.'''
#convert to 64 bytes encoded format using base64
client_creds_b64 = base64.b64encode(client_creds.encode())
type(client_creds_b64)

##############
#authorization_url="https://accounts.spotify.com/authorize"
#PARAMS = urlencode({'client_id':client_id,'response_type':'code','redirect_url':'http://localhost:5088/callback'})
#urll=authorization_url+'?'+PARAMS
#print(urll)
#rr = requests.get(urll)
#print(f"this is respone {rr}")



#token_url
token_url="https://accounts.spotify.com/api/token"
method="POST"
token_data={
    "grant_type":"client_credentials"
}

token_headers={
    "Authorization":f"Basic {client_creds_b64.decode()}"
}
print(token_headers)

r=requests.post(token_url, data=token_data, headers=token_headers)
print(r.json())
#token_response_data=r.json()
valid_request=r.status_code in range(200,299)
print(valid_request)

if valid_request:
    token_response_data=r.json()
    now=datetime.datetime.now()
    #print(now)
    access_token=token_response_data['access_token']
    expires_in=token_response_data['expires_in']
    #calculating expireing time. current_time+expire_in
    expires=now+datetime.timedelta(seconds=expires_in)
    did_expire=expires<now
    #print(did_expire)
    #print(expires)
    #print(access_token)
    #print(expires_in) #second 