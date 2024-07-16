![image](https://github.com/user-attachments/assets/207902fe-2e60-497b-9a79-1ddcb460b7ca)
## WafflesFORCE
### -> Multi-threaded Login Bruteforcer for Bypassing CRSF Tokens Protection
I created this script to bruteforce logins and bypass CSRF Tokens protection. This works by grabbing the CSRF Token, before performing a login attempt.

### Usage Example
```Python
# Basic Example
python3 wafflesforce.py --host "https://web-security-academy.net/login" --data 'username=*USER*&password=*PASS*' -U 'users.txt' -P 'passwords.txt' -mr '/login2' -ms '200-299,301,302' --csrf-param 'csrf' --csrf-regex 'name="csrf" value="(.*?)">' --threads 5 --output results.txt
# Using CSRF URL Example
python3 wafflesforce.py --host "https://web-security-academy.net/login" --data 'username=*USER*&password=*PASS*' -U 'users.txt' -P 'passwords.txt' -mr '/login2' -ms '200-299,301,302' --csrf-param 'csrf' --csrf-regex 'name="csrf" value="(.*?)">' --threads 5 --csrf-url "https://web-security-academy.net/login" --output results.txt
```

### Preview
![image](https://github.com/user-attachments/assets/6572f919-b586-405a-a365-ebeef00830a2)
