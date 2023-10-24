This level denies any closed tags or even ending tags.

The escape regex:
```
/<\/?[^>]+>/gi
```

And what we can do here is to inject a tag but never close it, and then the browser will automatically close that tag for us to achieve XSS.

Payload:
```
<img src=1 onerror=prompt(1)//
```
or
```
<svg onload=prompt(1) 
```

The difference between these answers is that there is a space at the end of answer 2, so that the `</article>` will be treat as attribute of the tag instead of being put into `onload` or `onerror`.