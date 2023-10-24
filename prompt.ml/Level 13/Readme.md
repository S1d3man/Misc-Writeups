This is a prototype pollution challenge.
Also learned a interesting usage of `replace()`

The code will take a JSON input, and check if "source" looks like a URL, if not, it will delete the attribute.

And then it will `JSON.parse()` the JSON to a object and manually combine it with a config object.
There is a default "source" value of the config object, which is a safe value and we need to get rid of it.

What we need to do here is that we have to to PP the "source" value and also set normal "source" value for the config.

Why? Because when javascript looks for an attribute, it first checks if the object has that attribute, if not, it will check its prototype.

And we can exploit the "delete attribute" behavior here to let it delete normal "source" but keep the polluted "source".

And here is the second part, we can't escape the double quote because it's filtered.
But there are interesting usages in `replace()`, let's look at the following example:
```javascript
"ABC{{target}}DEF".replace('{{target}}', "$`test")
// This will return:
// "ABCABCtestDEF"
```

This usage will clone the strings before the replaced string again.
Of course, there are other usage, too.

But this shows that if the user can control replaced value, it might be dangerous.

Payload:
```
{"__proto__":{"source": "$`><svg/onload=prompt(1) "}, "source": "("}
```