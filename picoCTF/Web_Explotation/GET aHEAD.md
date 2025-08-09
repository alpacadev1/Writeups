# URL 
https://play.picoctf.org/practice/challenge/132?page=6

# Challenge
Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:45028/

# Method of Solving
* The title of the challenge gave me a hint that this web challenge likely had to do with GET or HEAD.
* Clicking the buttons and examining the Burp Suite response/request, I noticed this
```
GET /index.php? HTTP/1.1
```
* This worked normally, however, out of curiosity I changed the GET to HEAD
* To my surprise, this returned the flag!
```
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_775f2530}
Content-type: text/html; charset=UTF-8
```
