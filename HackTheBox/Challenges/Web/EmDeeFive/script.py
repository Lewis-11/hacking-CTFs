import requests
import hashlib
while 1:
    s = requests.Session()
    resp = s.get("http://139.59.202.58:32472/")
    string = resp.content[167:187]
    #print "calculating MD5 of: " + string


    m = hashlib.md5()
    m.update(string)
    #print "hash: " + m.hexdigest()

    #proxies = {"http":"http://127.0.0.1:8080"}
    secr = s.post("http://139.59.202.58:32472/", data={"hash":m.hexdigest()})#, proxies=proxies)

    if secr.content[210:219] != "Too slow!":
        print secr.content
        break


