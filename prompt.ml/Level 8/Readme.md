Learned something interesting in this level, another two valid new line characters, and a new way to comment in javascript.

This challenge requires us to escape a single line comment.
It's pretty clear that we have to switch to the next line to execute our code, but that's not possible with `\r\n` since they're filtered out.

What we have to do is looking for other new line characters.
In other's write-ups, they mentioned "Line Separator (U+2028)" and "Paragraph Separator (U+2029)" are also valid new line characters in javascript, so we just need to use them to execute our code.

Example:
```
/**/ prompt(1) // There is a U+2028 between the multi-line comment and prompt(1)
```

By using the technique above, we can escape the single line comment.

The next part is also interesting, even if we escape the comment, there is still some trash behind our code.
The trash starts with double quote, but the double quote is filtered out so we cannot close it.
Also the slash is filtered, so we cannot comment it either...... or can we?

After taking a look at the writeu-ups, there is a discussion thread about the comment syntax "-->" that works in javascript.
After testing it in developer console, it actually works!

But it only support one line comment and no code can be put at the left side of the comment tag.

Right:
```javascript
--> This is comment
```

Wrong:
```javascript
1 --> This is commment
```

So here's the payload for this challenge:
```
/*U+2028->*/ prompt(1) --> <-U+2028 after prompt(1)
```