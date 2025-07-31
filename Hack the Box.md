# Details
Run an nmap script scan on the target. What is the Apache version running on the server? (answer format: X.X.XX)
# Work
* nmap -sV -sC 10.129.100.69
``` 
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
```
