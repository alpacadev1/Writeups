# URL
https://play.picoctf.org/practice/challenge/42?difficulty=3&page=9&search=


# Challenge:
Description
We found this packet capture and key. Recover the flag.

# Method of Solving:

<img width="1828" height="380" alt="image" src="https://github.com/user-attachments/assets/d652db11-2099-40dc-a34c-528aa429540a" />

* So, looking at Wireshark, it seems like we're dealing with encrypted traffic via TLS v1.2:
* From Microsoft: Transport Layer Security (TLS), like Secure Sockets Layer (SSL), is an encryption protocol intended to keep data secure when being transferred over a network
* The hint mentions "How can you decrypt the TLS stream?"
* So we are using the key that they provided us to decrypt the TLS stream

<img width="1127" height="788" alt="image" src="https://github.com/user-attachments/assets/1e06d5a8-ac59-408f-a7a4-0dc4b464a748" />

<img width="395" height="257" alt="image" src="https://github.com/user-attachments/assets/09d0537e-f7f9-47e1-8f1c-1fc87cbd78b6" />

* Using this HackTheBox guide, let's import a key into Wireshark

<img width="1172" height="735" alt="image" src="https://github.com/user-attachments/assets/9e952d7b-6358-44ff-9f3b-2c6cf7e76471" />

* So the IP address we input is the address of the server (denoted in Wireshark as the one having port 443 (HTTPS port))
* Port = 443
* The key you import is the one you download from the challenge
* After you hit apply, you should start to see some HTTP traffic (unencrypted)

<img width="1911" height="262" alt="image" src="https://github.com/user-attachments/assets/773ac15b-9b32-4052-a38d-ef6df8049ab2" />

* Using a filter, we can isolate the traffic
* If we follow the HTTP stream, we find some interesting information

<img width="1222" height="766" alt="image" src="https://github.com/user-attachments/assets/f96a3081-c0e0-483a-9e4a-1d3101b3d169" />

* The response header indicates a secret page and a .jpg file that follows that
* Let's try to extract this vulture.jpg onto our system
* File -> Export Objects -> HTTP

<img width="1428" height="770" alt="image" src="https://github.com/user-attachments/assets/f5d62720-d678-4349-98f3-3d61d2a62c4a" />

* Opening the JPG file:

<img width="1410" height="726" alt="image" src="https://github.com/user-attachments/assets/c1db5edc-1b6e-4b4a-8ad8-cec036e46f8e" />

* Using aperisolve: https://www.aperisolve.com/, I can upload the JPG file and look for any anomalies
* THERE IT IS, OUR FLAG!

<img width="1821" height="852" alt="image" src="https://github.com/user-attachments/assets/7edfa4c2-d78d-4e67-8cf8-56af5222e2a8" />



