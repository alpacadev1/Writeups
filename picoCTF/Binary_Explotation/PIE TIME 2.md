# URL
https://play.picoctf.org/practice/challenge/491?originalEvent=74&page=2

# Challenge
Can you try to get the flag? I'm not revealing anything anymore!!

Hints: What vulnerability can be exploited to leak the address?
Hints: Please be mindful of the size of pointers in this binary

# Work
<img width="776" height="176" alt="image" src="https://github.com/user-attachments/assets/438bf28c-9f73-4177-9b64-188af8a56343" />

* So in the code, the main function calls call_function() let's see what that's about

<img width="692" height="317" alt="image" src="https://github.com/user-attachments/assets/f9208dd8-e24d-48de-bd72-0b0f08d8a134" />
* The function has a printf without any formatting specifiers. The format argument has many different specifiers, which could allow an attacker to leak data if they control the format argument to printf - CTF101
* So knowing this, we can try to figure out where the buffer begins

<img width="1192" height="92" alt="image" src="https://github.com/user-attachments/assets/7ca28bb5-7651-4177-9d5a-594a77af06c9" />

* In here, the 414141 is our input since A = 41 in hex
* This means our input gets passed in the 8th parameter of the stack, which represents the start of the buffer
  
<img width="1918" height="1017" alt="image" src="https://github.com/user-attachments/assets/3ae74e5c-af55-467d-8f43-129886c3400b" />
* So after the call_functions() ends, it needs to go back to main to continue executing. Before executing call_function(), the stack saves the address of the next instruction of main to return back to
* This ends in 441
* So basically, we need to create a buffer that eventually leads us to this 441 address and change 441 to 36a (look at win() address in the image below)
* <img width="1918" height="1020" alt="image" src="https://github.com/user-attachments/assets/cc25f5a1-10e0-439a-b6ae-1534be27492a" />

* So through trial and error, look for the address ending in 441 
<img width="1900" height="228" alt="image" src="https://github.com/user-attachments/assets/126fb83c-d334-4d66-9f8d-ed153954da88" />
* We find this 441 address at the 19th parameter! However, this isn't the actual address we need to use the %p format
  


<img width="1895" height="185" alt="image" src="https://github.com/user-attachments/assets/9abd994b-0687-43ce-be87-27b5668afef3" />

* Here at the 19th %p we see 441 again
* Now alter the last 3 digits to point to win()
* Boom! thats the flag!
