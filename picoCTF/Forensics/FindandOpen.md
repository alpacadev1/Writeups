# URL
https://play.picoctf.org/practice/challenge/348?category=4&page=2

# Challenge:
Author: Mubarak Mikail

Description
Someone might have hidden the password in the trace file.
Find the key to unlock this file. This tracefile might be good to analyze.

# Method of Solving:
* Using the command: strings dump.pcap reveals some interesting output

```
Flying on Ethernet secret: Is this the flag
Flying on Ethernet secret: Is this the flag
Flying on Ethernet secret: Is this the flag
<SNIP>
iBwaWNvQ1RGe1Could the flag have been splitted?
<SNIP>
AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
<SNIP>
PBwaWUvQ1RGe1Maybe try checking the other file
```
* So off the bat, this: AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8= looks interesting because the equals sign likely hints towards base64
* However, in Wireshark, as we can see, the first couple of letters are non-essential as they represent information dedicated to routing and unicast (things we don't care about):

<img width="1738" height="631" alt="image" src="https://github.com/user-attachments/assets/06652719-0ab0-433b-b916-0d06fd55f268" />

* So that means this: VGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8= is our true input
* Paste this in CyberChef
<img width="623" height="563" alt="image" src="https://github.com/user-attachments/assets/4db61c2d-f87a-4046-a890-6d0fe627eb74" />




<img width="1738" height="631" alt="image" src="https://github.com/user-attachments/assets/215af697-4af5-48ce-af2b-56f9216ed537" />
