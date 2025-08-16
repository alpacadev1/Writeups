# URL
https://play.picoctf.org/practice/challenge/473?originalEvent=74&page=3&search=

# Challenge
Description
Try to decrypt the secret cheese password to prove you're not the imposter!

# Work
* I inputted some different chesse to gain some extra insight on how the key was made
```
Here's my secret cheese -- if you're Squeexy, you'll be able to guess it:  XDMJWALLVJM
Hint: The cheeses are top secret and limited edition, so they might look different from cheeses you're used to!
Commands: (g)uess my cheese or (e)ncrypt a cheese
What would you like to do?
e

What cheese would you like to encrypt? cheddar
Here's your encrypted cheese:  TUJOODW
Not sure why you want it though...*squeak* - oh well!

I don't wanna talk to you too much if you're some suspicious character and not my BFF Squeexy!
You have 2 more chances to prove yourself to me!

Commands: (g)uess my cheese or (e)ncrypt a cheese
What would you like to do?
e

What cheese would you like to encrypt? Asiago
Here's your encrypted cheese:  DRPDZL
Not sure why you want it though...*squeak* - oh well!
```
* Since the hint mentions something related to linear equations, a Google search leads to the conclusion that this is an affinity cipher
* https://www.dcode.fr/affine-cipher
* I copied the ciphertext, then brute-forced to find the key, which is y=21x+3
* Applied the same strategy for the original ciphertext, which outputted "A=21,B=3	WATERLOOMET"
* Pass input and get flag!
