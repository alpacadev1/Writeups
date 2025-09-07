# picoCTF: PIE TIME 2 (Writeup)

**Challenge URL:**  
[PIE TIME 2 on picoCTF](https://play.picoctf.org/practice/challenge/491?originalEvent=74&page=2)

---

## Challenge

> Can you try to get the flag? I'm not revealing anything anymore!!

**Hints:**
- What vulnerability can be exploited to leak the address?
- Please be mindful of the size of pointers in this binary

---

## Solution Approach

### 1. **Initial Analysis**

The challenge binary's `main()` function calls `call_function()`. 

![call_function() code](https://github.com/user-attachments/assets/f9208dd8-e24d-48de-bd72-0b0f08d8a134)

Inside `call_function()`, there's a call to `printf()` **without a format specifier**. This is a classic format string vulnerability, which allows us to leak stack data if we control the format string.

---

### 2. **Locating Our Input on the Stack**

When sending input (`AAAA`), we observe its position in the stack:

![Buffer location](https://github.com/user-attachments/assets/7ca28bb5-7651-4177-9d5a-594a77af06c9)

- The value `41414141` (hex for "AAAA") appears as the **8th parameter** to `printf`.
- This means our input is accessible via the 8th format argument (e.g., `%8$p`).

---

### 3. **Understanding the Return Address**

After `call_function()` finishes, the program returns to `main()`. The stack stores the address to return to:

![Return address location](https://github.com/user-attachments/assets/3ae74e5c-af55-467d-8f43-129886c3400b)

- The address ending in `441` is the return location.
- Our goal: **Overwrite the return address to jump to the `win()` function instead of returning to main.**
- The address for `win()` ends with `36a` (see image below).

![win() function address](https://github.com/user-attachments/assets/cc25f5a1-10e0-439a-b6ae-1534be27492a)

---

### 4. **Finding the Right Stack Offset**

Through experimentation, we find:

- The return address (`...441`) is the **19th parameter** on the stack.
- Using `%19$p` in our format string, we can leak this address.

![19th parameter leak](https://github.com/user-attachments/assets/126fb83c-d334-4d66-9f8d-ed153954da88)
![19th %p shows 441](https://github.com/user-attachments/assets/9abd994b-0687-43ce-be87-27b5668afef3)

---

### 5. **Flag Retrieval**

- Alter the last 3 digits of the leaked return address (`441`) to the `win()` address (`36a`).
- Craft the payload to overwrite the return address with that of `win()`.

---

**References:**
- [Format String Exploits](https://owasp.org/www-community/attacks/Format_string_vulnerability)
