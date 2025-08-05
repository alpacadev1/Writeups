# URL
https://play.picoctf.org/practice/challenge/237?page=9&solved=1

# Challenge
I thought that my password was super-secret, but it turns out that passwords passed over the AIR can be CRACKED, especially if I used the same wireless network password as one in the rockyou.txt credential dump.
Use this 'pcap file' and the rockyou wordlist. The flag should be entered in the picoCTF{XXXXXX} format.


# Solution
* From this hint, Aircrack-ng can make a pcap file catch big air...and crack a password., I assumed that aircrack can just take the .pcap file and crack the password using the rockyou.txt
```
┌──(kali㉿kali)-[~/picoCTF/forensics]
└─$ aircrack-ng -w /home/kali/Downloads/rockyou.txt wpa-ing_out.pcap
```
* Returned: KEY FOUND! [ mickeymouse ]
* So then the flag is picoCTF{mickeymouse}! 
