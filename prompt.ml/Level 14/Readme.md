I didn't find a way to solve this challenge, but I have guessed the concept right.

Since the input in turned into uppercase, we can't execute javascript code directly.
And lots of special characters are replaced, too, so we can't use most of other encodings.

Also the `src` is all changed to `data:` instead, so we cannot exploit `src` to XSS.
After taking a look at the cheatsheet of portswigger, I knew that `data:` can run javascript code with base64 encoding.

But atm I was suspecting that if combining a working payload of a full uppercase base64 string.
Therefore I didn't try this level.

But it turned out that is actually one way to do this level, I guess I'll have to try harder in the future.
