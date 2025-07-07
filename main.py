from robloxreverse import Roblox
import requests
from bs4 import BeautifulSoup
import json

def csrf():
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = "https://www.roblox.com/CreateAccount"
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    csrf_meta = soup.find("meta", attrs={"name": "csrf-token"})
    if csrf_meta:
        csrf_token = csrf_meta.get("data-token")
        print("[*] CSRF Token:", csrf_token)
        return csrf_token
    else:
        print("[!] CSRF token not found.")
        return None

def cookies():
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = "https://www.roblox.com/CreateAccount"
    response = session.get(url, headers=headers)
    cookies_dict = session.cookies.get_dict()

    print("[*] All Cookies from response:")
    for key, value in cookies_dict.items():
        print(f"    {key}: {value}")

    cookie_keys = ["rbx-ip2", "RBXEventTrackerV2", "GuestData", "RBXcb"]
    filtered_cookies = []

    for key in cookie_keys:
        if key in cookies_dict:
            filtered_cookies.append(f"{key}={cookies_dict[key]}")

    cookie_header = "; ".join(filtered_cookies)
    cookie_header += "; RBXcb=RBXViralAcquisition=false&RBXSource=false&GoogleAnalytics=false"
    print("[*] Formatted Cookie Header:", cookie_header)
    return cookie_header

roblox = Roblox()

auth = roblox.reverse()
print("[*] Secure Authentication Info:")
print(json.dumps(auth, indent=4))

secure_auth = {
    "clientPublicKey": auth["clientPublicKey"],
    "clientEpochTimestamp": auth["clientEpochTimestamp"],
    "serverNonce": auth["serverNonce"],
    "saiSignature": auth["saiSignature"]
}

token = csrf()
cookie_string = cookies()

print("\n==================== SUMMARY ====================")
print("[+] CSRF Token:", token)
print("[+] Cookie Header:", cookie_string)
print("[+] Secure Auth:")
print(json.dumps(secure_auth, indent=4))
