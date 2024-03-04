# Info

Difficulty: Easy
# Desc
> Step into the ApacheBlaze universe, a world of arcade clicky games. Rumor has it that by playing certain games, you have the chance to win a grand prize. However, before you can dive into the fun, you'll need to crack a puzzle.

# Writeup
This is a challenge that requires us to exploit a request smuggling vulnerability in Apache before version 2.4.56.

The website is has a frontend and a backend, and Apache handles the proxy with `Rewrite`.
The backend will give the flag if you access a game called "click_topia" with `X-Forwarded-Host: dev.apacheblaze.local` header.

At first, I thought this is just a simple challenge that I only need to manually add the header.
It turned out I was wrong. 

Apache will always add the value of `Host` header at the end of `X-Forwarded-Host`, and the backend code `request.headers.get()`will not get our payload.

So, I try to look for some CVE in the rewrite module of Apache, and there it is, CVE 2023 25690!
This [link](https://github.com/dhmosfunk/CVE-2023-25690-POC) has a detailed PoC to help us exploit this.
Basically, you can consider that the request part that is selected by regex are urldecoded and threw to the raw http body of the proxy request, which means we can inject malicious things like CRLF.

After some time debugging in docker, I finally made it with the following payload:
```
http://x.x.x.x:xxxxx/api/games/click_topia%20HTTP/1.1%0D%0AHost:%20dev.apacheblaze.local%0D%0A%0D%0AGET%20/
```

Also, it seems that the Host header is required in proxy request, or Apache will return a 400 to you.