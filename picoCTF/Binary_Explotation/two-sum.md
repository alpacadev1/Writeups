# URL
https://play.picoctf.org/practice/challenge/382?page=1&tag=56

# Challenge
Description
Can you solve this?
What two positive numbers can make this possible: n1 > n1 + n2 OR n2 > n1 + n2
Enter them here nc saturn.picoctf.net 49884. Source

# Work
* So, looking at the code, we see that
* <img width="587" height="205" alt="image" src="https://github.com/user-attachments/assets/17532e63-7b97-49fb-9584-eff12356e6c8" />
* <img width="875" height="531" alt="image" src="https://github.com/user-attachments/assets/59a163a1-c006-40bd-8467-7b499062c27f" />
* So for the code to continue, the addIntOvf() function HAS to equal -1
* The said function has only two ways of outputting -1
* Using the hint, integer overflow should hint us to explore how positive integers add up to be a negative number
* First Google search shows us this: For example, if a signed 32-bit integer has a maximum value of 2,147,483,647, adding 1 to this value would result in -2,147,483,648
* Using this hint, let's see if this prints us the flag
```
rxile@MSI:~$ nc saturn.picoctf.net 49884
n1 > n1 + n2 OR n2 > n1 + n2
What two positive numbers can make this possible:
2147483647 1
You entered 2147483647 and 1
You have an integer overflow
YOUR FLAG IS: picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_e06700c0}
```
* Hooray, that got us the flag!

