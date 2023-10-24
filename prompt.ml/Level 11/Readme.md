This level requires us to execute code by fulfilling javascript valid syntax.

The escape code:
```javascript

var memberName = input.replace(/[[|\s+*/\\<>&^:;=~!%-]/g, '');

var dataString = '{"action":"login","message":"Welcome back, ' + memberName + '."}';

return '                                \n\
<script>                                    \n\
    var data = ' + dataString + ';          \n\
    if (data.action === "login")            \n\
        document.write(data.message)        \n\
</script> ';
```

Basically, our input will be filtered out some special characters first, and then it will be put into a JSON string. Eventually, it will be throw into a script tag to act as a object.

So technically, we can inject some code in the final part, but we can't simply add a new line and comment to execute arbitrary code since the regex sanitization has replaced any new line and space characters with `\s`.

But as I said earlier, the input is used to create object, and we can try to call some functions in the object creation.

We can use double quote to escape the string, and we can use parenthesis to call functions.
Combine these two conditions, we can create a ridiculous situation to run arbitrary code, and most importantly, it's valid!

Example:
```javascript
"A normal javascript string"(console.log("Executed"))
```

The example above is a valid syntax, although it does throw error, but the code we want is already executed.

This behavior also exists in python.
These two programming languages checks the syntax first, when calling a function, the thing that is at the left side of parenthesis is checked if it exists first. And if it does, they will try to run the expression in the parenthesis which is used as argument.

(The definition of exist seems to require the thing to be defined, even `undefined` is defined in javascript. This means the only undefined things are the random variable names you typed.)

Then, the programming language will notice the thing exists but is not a callable function and throws a error.

But that doesn't really matter, since our code is executed already.

After escaping, we still need to take care of the trash behind.
The first thing we do should be adding another double quote to make the trash a string.
And we need valid operators here to make the string behind meaningful.
According to the [Expressions and Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators), we can use text-only operators to do this, such as `in` or `instanceof`.

Payload:
```
"(prompt(1))in"
```