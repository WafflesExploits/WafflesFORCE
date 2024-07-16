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

### Installation
```bash
git clone https://github.com/WafflesExploits/WafflesFORCE.git
cd WafflesFORCE
python3 wafflesforce.py ...
```
### Commands 
```
╦ ╦╔═╗╔═╗╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╦═╗╔═╗╔═╗
║║║╠═╣╠╣ ╠╣ ║  ║╣ ╚═╗╠╣ ║ ║╠╦╝║  ║╣ 
╚╩╝╩ ╩╚  ╚  ╩═╝╚═╝╚═╝╚  ╚═╝╩╚═╚═╝╚═╝
usage: wafflesforce.py [-h] [--host HOST] [-U [USERS]] [-u [USER]]
                       [-P [PASSWORDS]] [-p [PASSWORD]] [-cr CSRF_REGEX]
                       [-cp CSRF_PARAM] [-cu [CSRF_URL]] [-mr [MATCH_REGEX]]
                       [-ms [MATCH_STATUS]] [-d [DATA]] [-q [QUERY]]
                       [-t [THREADS]] [-o [OUTPUT]] [-vr] [--verbose]

-> Multi-threaded Login Bruteforcer for Bypassing CSRF Token Protection
 

options:
  -h, --help            show this help message and exit
  --host HOST           Target URL.
  -U [USERS], --users [USERS]
                        Path to usernames' wordlist file.
  -u [USER], --user [USER]
                        Specify one username to use.
  -P [PASSWORDS], --passwords [PASSWORDS]
                        Path to passwords' wordlist file.
  -p [PASSWORD], --password [PASSWORD]
                        Specify one password to use.
  -cr CSRF_REGEX, --csrf-regex CSRF_REGEX
                        Specify Regex pattern to extract CSRF Token. Example:'name="csrf" value="(.*?)">'
  -cp CSRF_PARAM, --csrf-param CSRF_PARAM
                        Specify Regex pattern to extract CSRF Token. Example:'csrf'
  -cu [CSRF_URL], --csrf-url [CSRF_URL]
                        URL Path to csrf token.
  -mr [MATCH_REGEX], --match-regex [MATCH_REGEX]
                        Match specified Regex pattern. Example:'/login2'
  -ms [MATCH_STATUS], --match-status [MATCH_STATUS]
                        Match specified Status codes. Default:'200-299,301,302'
  -d [DATA], --data [DATA]
                        Body parameters for POST request. Example:'username=*USER*&password=*PASS*'
  -q [QUERY], --query [QUERY]
                        Query parameters for GET request.
  -t [THREADS], --threads [THREADS]
                        Number of threads to use. Default: 5
  -o [OUTPUT], --output [OUTPUT]
                        Outputs results to a file.
  -vr, --verify         Set verify to false. Use if the website doesn't use SSL.
  --verbose             Increase Verbosity.

[Usage Example]
python3 wafflesforce.py --host "https://web-security-academy.net/login" --data 'username=*USER*&password=*PASS*' -U 'users.txt' -P 'passwords.txt' -mr '/login2' -ms '200-299,301,302' --csrf-param 'csrf' --csrf-regex 'name="csrf" value="(.*?)">' --threads 5 --output results.txt

[Using CSRF URL Example]
python3 wafflesforce.py --host "https://web-security-academy.net/login" --data 'username=*USER*&password=*PASS*' -U 'users.txt' -P 'passwords.txt' -mr '/login2' -ms '200-299,301,302' --csrf-param 'csrf' --csrf-regex 'name="csrf" value="(.*?)">' --threads 5 --csrf-url "https://web-security-academy.net/login" --output results.txt
```
