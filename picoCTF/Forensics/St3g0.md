# URL
https://play.picoctf.org/practice/challenge/305?page=15

# Challenge
Description
Download this image and find the flag.
Download image

# Method of Solving:
* Use wget to download the PNG file:
```
wget https://artifacts.picoctf.net/c/215/pico.flag.png 
```

* From the challenge name, St3g0, likely means the flag is hidden using an LSB encoding technique (https://wiki.bi0s.in/forensics/lsb/)
* Using zsteg (a forensics tool), we can decode any encoded hidden message within this PNG file

<img width="1260" height="233" alt="image" src="https://github.com/user-attachments/assets/4aaf7350-fb86-4af7-8f61-5a2b78e35130" />

* The flag is: picoCTF{7h3r3_15_n0_5p00n_96ae0ac1}!
