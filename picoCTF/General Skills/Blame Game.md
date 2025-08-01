# URL 
https://play.picoctf.org/practice/challenge/405?page=1&solved=1
# Method of solving

 
```
┌──(kali㉿kali)-[~/picoCTF/general/drop-in]
└─$ ls -lah
total 16K
drwxr-xr-x 3 kali kali 4.0K Jul 30 23:12 .
drwxrwxr-x 3 kali kali 4.0K Jul 30 23:11 ..
drwxr-xr-x 8 kali kali 4.0K Jul 30 23:22 .git
-rw-r--r-- 1 kali kali   23 Jul 30 23:12 message.py
```

* the list command gave .git as a directory so I chose to explore that
* after cd'ing into logs directory I used vim to look into the HEAD file
* The very second line of the HEAD file gave the flag!
