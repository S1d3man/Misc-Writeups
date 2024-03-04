# Info
Difficulty: Easy
# Desc
> Experience the freedom of the web with ProxyAsAService. Because online privacy and access should be for everyone, everywhere.
# Writeup
This is a SSRF Filter Bypass challenge.
The website is used as proxy server, it gets pages information from reddits.

The proxy URL is pre-fixed with `reddit.com`, and the URL will be like: `http://reddit.com{URL}`.
We can control the string behind `reddit.com`, and it didn't filter out special characters, so we can simply ignore the `reddit.com` with "@", which makes the URL parser thinks it is a username instead.

Also, the URL filter is quite lame, since it only blocks private network IP keywords.
Therefore, we can bypass it with external DNS record that resolves to 127.0.0.1 to bypass it, such as:
```
http://x.x.x.x:xxxxx/url=@localtest.me:1337/debug/environment
```