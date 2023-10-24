This level will URL encode our input and replace single quotes with space, also it will replace "prompt" with "alert".

This level requires us to exploit a flaw in the code.
We can't use other encodings to bypass the "prompt" filter due to the URL encoding.

But the URL encoding does not encode single quotes, so if we put a single quote in "prompt", it will be remove later and keep "prompt" there.

Payload:
```
promp't(1)
```
