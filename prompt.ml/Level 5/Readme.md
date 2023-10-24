This challenge sanitizes ">", "on.+="  and "focus".

Learned something new here, first is we can change the type of `<input>` to image and use `src` and `onerror` attributes, the second is new line characters are ignored in html or in browser.

If we hit enter in the textarea, we can see our input has a new line there, but if you put a new line in html, it just gets ignored.

So what we have to do here are:
1. Change the type of input to image
2. Bypass the regex check by adding new line characters and cause the desync of javascript string and our browser DOM content.

Payload:
```
" type=image src onerror
=alert() 
```