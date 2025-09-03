# URL
https://play.picoctf.org/practice/challenge/202?originalEvent=67&page=1

# Challenge
Author: BrownieInMotion
Description
Now presenting cowsay as a service

# Work
* So off the bat, the website tells us this:
<img width="693" height="160" alt="image" src="https://github.com/user-attachments/assets/928ee1fe-fa54-4680-aad6-509b5dcd249a" />

* To test it out, I said hello
<img width="675" height="290" alt="image" src="https://github.com/user-attachments/assets/32fbb71a-ff76-4517-bfd9-53a052af79d2" />

* Output from cowsay is sent back to the client as plain text.
* The challenge provides us with an index.js file, so let's take a look at that
<img width="1122" height="402" alt="image" src="https://github.com/user-attachments/assets/70889d46-69b0-45fc-87d4-be5346d7bdaf" />

* Visiting /cowsay/hello runs the shell command: /usr/games/cowsay hello
* Output from cowsay is sent back to the client as plain text.
* However, this is a huge problem as seen in the picture: req.params.message is passed directly into a shell command.
* So, for example, if I ran /cowsay/hello;ls it would run /usr/games/cowsay hello;ls, which lists files on the server

<img width="585" height="381" alt="image" src="https://github.com/user-attachments/assets/5d3f2154-350c-4f4f-ae24-715b137b1228" />

* By doing that, we can see a falg.txt file
* Use the cat command to list out the contents of falg.txt

<img width="831" height="267" alt="image" src="https://github.com/user-attachments/assets/1ffc6cb6-eed5-406e-906e-8555657b229b" />

* That's our flag! picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}
