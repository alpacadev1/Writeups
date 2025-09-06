# URL
[practice/challenge/489?originalEvent=74&page=2](https://play.picoctf.org/practice/challenge/489?originalEvent=74&page=2)

# Challenge
Here is a binary that has enough privilege to read the content of the flag file but will only let you know its hash. If only it could just give you the actual content!
Connect using ssh ctf-player@rescued-float.picoctf.net -p 54781 with the password, 4f5344cd and run the binary named "flaghasher".

# Work

So off the bat, I notice the shell is an rbash shell: 
<img width="749" height="146" alt="image" src="https://github.com/user-attachments/assets/0674de02-bad3-47fb-8397-0172268b3f92" />

* An rbash shell is essentially: "A restricted shell is used to set up an environment more controlled than the standard shell".
* This means accessing basic commands is a struggle since rbash restricts us from doing this

* Now that we know that, let's try to locate where the binary is
```
ctf-player@pico-chall$ which flaghasher
/usr/local/bin/flaghasher
```

* However, since we can't change directories or move around the terminal, we have to escalate our shell into a standard one

<img width="1186" height="56" alt="image" src="https://github.com/user-attachments/assets/1aa5241b-8805-4f3a-a67b-a0a615a8319b" />


* Looking at our environmental variables, the one that pops out is /usr/bin
* /usr/bin is the directory that contains the majority of the executable files and commands available to all users, including /usr/bin/sh, which refers to the Bourne Shell

* In our restricted system, we do have access to this shell
<img width="581" height="648" alt="image" src="https://github.com/user-attachments/assets/be745fa8-a677-4444-ae5e-cd00676505d4" />

* If we run the sh command, we upgrade our shell!
<img width="702" height="57" alt="image" src="https://github.com/user-attachments/assets/ee0a14ec-8494-4d41-8272-f5a3b9e13221" />


* Now that we have upgraded our shell, try to see if we can run the flaghasher binary
<img width="868" height="167" alt="image" src="https://github.com/user-attachments/assets/9c96876c-3170-4554-968c-a52893292af0" />

<img width="848" height="125" alt="image" src="https://github.com/user-attachments/assets/9a6757cc-f723-436e-9720-fa478c4b0464" />
* The s stands for setuid, and it basically means: when this binary is executed, run it with the file owner’s privileges, not the caller’s
* So if you can exploit with this file, you can run commands as root

* This binary takes in the contents of /root/flag.txt and creates a hash
* We are only given the hash, not the contents of flag.txt, so we have to figure out a way to retrieve this content
* If we run strings on the binary, we see some interesting output
<img width="583" height="597" alt="image" src="https://github.com/user-attachments/assets/f792029f-d9a8-4934-903e-c208aa569d54" />

* This command essentially does this: ```system("/bin/bash -c 'md5sum /root/flag.txt'");```
* This is a huge vulnerability because if you can control what binary gets executed as md5sum, you can run any command as root (remember our SUID permission).

* So now what if having md5sum, we instead create a fake md5sum that gives us root privileges.
```
echo "/bin/sh" > /tmp/md5sum
chmod +x /tmp/md5sum
```
* Typically, "/bin/sh" spawns a regular bash shell, but since flaghasher inherits root privileges, we spawn a root shell
* Now place this /tmp at the start of the $PATH
```
export PATH=/tmp:$PATH
```
* This is because the system looks through the directories listed in $PATH, from left to right. Now, when system() looks for md5sum, it finds the fake one before the real one
<img width="1381" height="207" alt="image" src="https://github.com/user-attachments/assets/a8e8fad2-97b3-4610-b5d3-3c783a2d1663" />

* That's the flag! picoCTF{Co-@utH0r_Of_Sy5tem_b!n@riEs_f6f1b3d4}
