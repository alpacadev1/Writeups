# URL
https://play.picoctf.org/practice/challenge/12?category=3&page=5

# Challenge:
Description
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: VaultDoor1.java

# Method of Solving:
<img width="645" height="763" alt="image" src="https://github.com/user-attachments/assets/07b31d51-663d-48cf-9152-f0209af48fba" />

* The code and the hint mentions charAt(), in Java charAt() simply retrieves the character AT that index (e.g charAt(2) in hello returns "l")
* So, likely the code takes a password input, then compares each index to a character (The first index of input MUST equal d, and so on)
* It would be very tedious to go through each element and figuring out the character that belongs there so I created a simple script
```
public class Main
{
    public static void main(String[] args) {
        
        char[] passwordChars = new char[32];

        passwordChars[0]  = 'd';
        passwordChars[29] = '3';
        passwordChars[4]  = 'r';
        passwordChars[2]  = '5';
        passwordChars[23] = 'r';
        passwordChars[3]  = 'c';
        passwordChars[17] = '4';
        passwordChars[1]  = '3';
        passwordChars[7]  = 'b';
        passwordChars[10] = '_';
        passwordChars[5]  = '4';
        passwordChars[9]  = '3';
        passwordChars[11] = 't';
        passwordChars[15] = 'c';
        passwordChars[8]  = 'l';
        passwordChars[12] = 'H';
        passwordChars[20] = 'c';
        passwordChars[14] = '_';
        passwordChars[6]  = 'm';
        passwordChars[24] = '5';
        passwordChars[18] = 'r';
        passwordChars[13] = '3';
        passwordChars[19] = '4';
        passwordChars[21] = 'T';
        passwordChars[16] = 'H';
        passwordChars[27] = 'f';
        passwordChars[30] = 'b';
        passwordChars[25] = '_';
        passwordChars[22] = '3';
        passwordChars[28] = '6';
        passwordChars[26] = 'f';
        passwordChars[31] = '0';

        // Convert the char array to a String
        String password = new String(passwordChars);
        System.out.println(password);
    }
}
```

<img width="580" height="695" alt="image" src="https://github.com/user-attachments/assets/4ae7fa51-6d88-41ae-956c-54c413f3bedf" />

* Now, take this output and paste it into the input of the Vaultjava1.class file
* Be careful, though, the input requires picoCTF{} in it
<img width="917" height="157" alt="image" src="https://github.com/user-attachments/assets/828bf2d1-3923-4fd5-b4f6-30d002c14df7" />

* If the output is "Access Granted", your input works!
<img width="728" height="107" alt="image" src="https://github.com/user-attachments/assets/80f7ff87-b744-475b-811a-8509337e7c88" />

* That is the flag!



