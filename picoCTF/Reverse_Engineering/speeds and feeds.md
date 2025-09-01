# URL
https://play.picoctf.org/practice/challenge/116?category=3&page=5

# Challenge
Description
There is something on my shop network running at nc mercury.picoctf.net 33596, but I can't tell what it is. Can you?

# Method of Solving:
* Connect to the server
* Server outputs:
```
G17 G21 G40 G90 G64 P0.003 F50
G0Z0.1
G0Z0.1
G0X0.8276Y3.8621
G1Z0.1
G1X0.8276Y-1.9310
G0Z0.1
G0X1.1034Y3.8621
G1Z0.1
G1X1.1034Y-1.9310
G0Z0.1
G0X1.1034Y3.0345
G1Z0.1
<SNIP>
```

* So the hint mentions: What language does a CNC machine use?
* Googling this gives us the answer: "A CNC machine uses G-code, also known as the standardized programming language for CNC machines."
* With this knowledge, let's search for a G-code compiler
* The first Google search led me to this website: https://gcodetutor.com/cnc-program-simulator.html
* Paste the server output into the compiler on this website, and boom

<img width="1700" height="582" alt="image" src="https://github.com/user-attachments/assets/8f17b60e-f362-4b1a-b566-a491f0518bfc" />
