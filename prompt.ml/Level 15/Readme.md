This level is a advanced version of level 7.

This time we can't use multi-line comment, that makes it a lot harder to clean out the garbage.

The code now has another attribute which use single quote to wrap the value.
So we cannot simply use single quote to connect injection points.

After a while, I have found a way to achieve this by using `<script>` tag to connect the injection points, but that's far not enough.
Since we only connect two injection points, but the garbage remains, we'll have to find a way to deal with multi-line garbages.

Here's my way, use template string wrap the whole string between injection points.

Example:
```html
<p title=""><script>`>...garbage...`</script>
```

And if we combine the techniques of force calling functions:
```html
<p title=""><script>`>...garbage...`(prompt(1))</script>
```
This will call `prompt(1)`!
But that's not gonna happen since there is a length restriction.

So after a while, I finally find a working way by connecting 3 injection points to do this.
I constructed two template string to clean the garbages, used forced function calling trick, and used the "+" operator to fit the syntax.

Payload:
```
"><script>`#"`(prompt(1))+`#`</script>
```

HTML:
```html
<script>`" data-comment='{"id":0}'></p>
<p class="comment" title=""`(prompt(1))+`" data-comment='{"id":1}'></p>
<p class="comment" title="`</script>
```

Anyway, there is a much easier answer in the write-ups, since we are both using template string, the answer just create a big template string and use `${expression}` to run code inside template string.
That totally makes sense, I'm too dumb to come up with that.

Better Payload:
```
"><script>`#${prompt(1)}#`</script>
```

Also there are other good solutions, such as using html comment block inside `<svg>` tag.
