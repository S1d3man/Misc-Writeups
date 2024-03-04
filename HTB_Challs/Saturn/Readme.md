# Info

Difficulty: Easy
# Desc
> Saturn corp just launched their new proxy service. According to them, they have made sure their proxy service contains no security issues as they have implemented decent security measures with up to date components.

# Writeup
This is a SSRF filter bypass challenge, the target uses `python-safeurl` library to prevent SSRF attacks.
But there is a option in the code that make `python-safeurl` follow redirects.
And after taking a look at the source code, it seems that the library will resolve IP address, if the IP is in the blacklisted IP range, it will raise an error.
Not sure if it will also resolve the URLs after following the redirection.

So basically, I tried to setup a php server to redirect requests with `header("Location: http://127.0.0.1:1337/secret")`, but it seems the server won't send request to my computer.
I looked for other URL shortener to do the same thing, and it seems most URL shortener will block 127.0.0.1 for redirection, but it's okay, since we can use other domain name that resolves to 127.0.0.1 to be shortened, such as localtest.me.

After shortening `http://localtest.me:1337/secret`, I sent the URL to the target, and the flag showed up.