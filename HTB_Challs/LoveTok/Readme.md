# Info
Difficulty: Easy
# Desc
>True love is tough, and even harder to find. Once the sun has set, the lights close and the bell has rung... you find yourself licking your wounds and contemplating human existence. You wish to have somebody important in your life to share the experiences that come with it, the good and the bad. This is why we made LoveTok, the brand new service that accurately predicts in the threshold of milliseconds when love will come knockin' (at your door). Come and check it out, but don't try to cheat love because love cheats back. 💛

# Writeup
This is a website that produce a timestamp based on what we input in the query string "format".
After reading the provided code, it seems that the website eval-ed the format after sanitizing it with `addslashes()`.

Example code:
```php
$format = $_GET['format'];
$this->format = addslashes($format);
eval('$time = date("' . $this->format . '", strtotime("' . $this->prediction . '"));');
```

`addslashes()` is not a good choice to prevent malicious input, since what it does is only adding backslashes before `"`, `'`, and `\`.

At first, I tried using something like `$_GET[1]` to bypass `addslashes()` and put a double quote into the eval string to code injection, but it turned out that the string is still backslash-ed.
I'm still not sure why, need to test this later.

I spent some time searching for other ways, it turned out I can simply abuse "string interpolation" to call functions.
```
http://x.x.x.x:xxxxx/?format=${phpinfo()}
```
> "string interpolation" is deprecated after php 8.2, but it can still be used.

The example above will break the page, though.

Therefore, I only need to call `system()` to execute system commands.
Still need to bypass `addslashes()`, so I just get the string from `$_GET[1]`.
Combining the techniques above, here is the final payload:
```
http://x.x.x.x:xxxxx/?format=${system($_GET[1])}&1=cat%20/flagXXXXX
```
