# URL
https://play.picoctf.org/practice/challenge/503?originalEvent=75&page=1

# Challenge:
Description
Identify and connect to 4 open ports on the target system. Each successful connection will reveal part of the flag. The flag seems too long, though. Can you write a Python script that is able to decode the flag and saves it with the appropriate extension?

# Work
* playing around with the program it gave me this:
```
┌──(kali㉿kali)-[~]
└─$ nc activist-birds.picoctf.net 53810

===== PORT SCANNING CHALLENGE =====
Mission: Identify and connect to 4 open ports on the target system.
Each successful connection will reveal part of the encrypted flag.

Available commands:
  scan              - Scan for open ports
  connect <port>    - Connect to a specific port
  status            - Display current progress
  help              - Display this help message
  exit              - Exit the challenge

The ports you choose may affect your success. Choose wisely!
Good luck, hacker.


Enter command: scan

[+] Starting Nmap 7.94 ( https://nmap.org )
[+] Scanning target [10.10.X.X] ( Challenge Server )
[+] Initiating SYN Stealth Scan
[+] Scanning 65535 ports
... scan in progress

Nmap scan report for 10.10.X.X
Host is up (0.042s latency).

PORT         STATE   SERVICE
----         -----   -------
80/tcp       open    http
668/tcp      open    irc
67/tcp       open    dhcp
53/tcp       open    dns
5000/tcp     open    vcenter
6423/tcp     open    rdp
22/tcp       open    ssh
2354/tcp     open    tftp

# Nmap done: 1 IP address (1 host up) scanned
# 8 ports found open, 65527 ports filtered

Hint: The ports you choose may affect your success. Choose wisely!

Enter command: connect
Invalid command. Use 'scan', 'connect <port>', 'status', or 'exit'.

Enter command: connect 80

Milestone: You found the first encoded part!

[+] Connection established to 80/tcp...
[+] Service banner: HTTP Hypertext Transfer Protocol server
[+] HTTP response: 200 OK
[+] Server: Apache/2.4.41
[+] Content-Type: text/html
[+] Discovered hidden directory
 scan in progress ...
Encoded part: SNIPPED
[+] You need to connect to another port for the next part.

Enter command: connect 5000

[+] Connection established to 5000/tcp...
[+] Service banner: vCenter VMware vCenter Server management (TCP)
[+] Connected to service: VMware vCenter Server management (TCP)
[+] Found hidden data in service response
 scan in progress ...
Encoded part: SNIPPED
[+] You need to connect to another port for the next part.

Enter command: connect 53

[+] Connection established to 53/tcp...
[+] Service banner: DNS Domain Name System server
[+] Connected to service: Domain Name System server
[+] Found hidden data in service response
 scan in progress ...
Encoded part: SNIPPED
[+] You need to connect to another port for the next part.

Enter command: connect 67

Milestone: You found all encoded parts!

[+] Connection established to 67/tcp...
[+] Service banner: DHCP Dynamic Host Configuration Protocol server
[+] Connected to service: Dynamic Host Configuration Protocol server
[+] Found hidden data in service response
Encoded part: SNIPPED
 scan in progress ...

🎯 Target successfully compromised! 🎯
```

* From here I decided to put all these encoded parts into a .txt file where I can concencate all encoded parts into one large string
* One thing I noticed was "iVBORw0KGgo" which is the telltale sign that this base64 is likely represents a PNG image
* On that note, I decided to visit this website: https://base64.guru/converter/decode/image. On here, I simply copy pasted the base64 and converted it to an image
* The image was the flag!

