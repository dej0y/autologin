#!/usr/bin/python3
import re
import urllib.request
import urllib.parse
import urllib.error

username = "usnm"
password = "pswd"

try:

    response = urllib.request.urlopen('http://detectportal.firefox.com/')
    html_content = response.read().decode()
    print(response.geturl()) 
    print(response.read().decode())
    print("html_content", html_content)

    redirect_url_match = re.search(r'window\.location="(http[^"]+)"', html_content)
    if not redirect_url_match:
        print("Redirection URL not found")
        exit(1)
    redirect_url = redirect_url_match.group(1)
    print(f"Redirecting to: {redirect_url}")

    response_redirect = urllib.request.urlopen(redirect_url)
    magic = re.search(r"[0-9a-f]{16}", response_redirect.read().decode()).group()
    data = urllib.parse.urlencode({'4Tredir': '', 'magic': magic, 'username': username, 'password': password}).encode('utf-8')
    response_final = urllib.request.urlopen(redirect_url, data=data)

    if b"Failed" in response_final.read():
        print("Failed")
    else:
        print("Success")
except AttributeError:
    print("Already Logged in")
except urllib.error.URLError as e:
    print("Can't connect:", e.reason)
except Exception as e:
    print(type(e), e)


