import re
import requests 
import sys 
import time
import os
import random
import threading
from rich import print
import mechanize
def notor():
    
    red="\033[1;31m"
    green="\033[1;32m"
    blue="\033[1;33m"
    u="\033[1;34m"
    print("") 
    print ("")
    red ="\033[1;31m"
    user =str(input (red+f"""
 ---(websweep@Ahmed)-[~{green}/Enter Url{red}]
|
 ---$"""+green))

    print ("")
    r = str(open("directory-list-lowercase-2.3-medium.txt","r").read())

    o = r.splitlines()
   
    print ("--------------:START Search: --------------")
    time.sleep(2)
    print ("")
    print ("[+] Target Url :",user)

    print ("")
    print("---------------------------------------")
    print ("")
    time.sleep(2)

    try:
        for word in o:
            url =user+"/"+f"{word}.json"
            get = requests.get(url,"html.parser")
            done =[]
            if get.status_code == 200:
                done.append(url)
                print ("[bold green on red][+] Found location:[/]",url)
       
        print ("[+] Done :"+done)

             
                
    except:
        print ("[bold red][!] Please Connect in network[/] ")
        sys.exit()




        
           

            
############
def Tor():

  
    time.sleep(8)
 
    time.sleep(1)
    os.system("clear")
    red="\033[1;31m"
    green="\033[1;32m"
    blue="\033[1;33m"
    u="\033[1;34m"                           
     
    s=f""" 
                                                +
                                               | |
    ___________________________________________| |
   |_______Tor___--+______________________ ____| |            
                                               |_|
            Test--> http://localhost
            ERROR--> http://localhost/                                 
    """                                        
    print(s)
    red="\033[1;31m"
    green="\033[1;32m"
    blue="\033[1;33m"
    u="\033[1;34m"
    print ("")
    print("")
    user =str(input (red+f"""
 ---(websweep@Ahmed)-[~{green}/Enter Url{red}]
|
 ---$"""+green))
    #user =str(input(blue+"[*] Enter IP target-->: "+red))
    time.sleep(1)
    
  
   
    proxy ={
        "http":"socks5://127.0.0.1:9050",
        "https":"socks5://127.0.0.1:9050"
    }

    r = str(open("directory-list-lowercase-2.3-medium.txt","r").read())

    o = r.splitlines()
  
    time.sleep(1)
  
    time.sleep(2)
    print ("")
   
    print ("")
    print ("")
   
    print ("")
    time.sleep(2)

    try:
        file =str(input (red+f"""
 ---(websweep@Ahmed)-[{green}~/Do You Want add js or txt [n/y]?{red}]
|
 ---$"""+green))
        red="\033[1;31m"
        green="\033[1;32m"
        blue="\033[1;33m"
        u="\033[1;34m"
        print ("[*] Tor Actvite..")
        time.sleep(1)
        
            
        useragent =['Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.0.1.56','Mozilla/5.0 (Linux; Android 9; LAVA LE9830 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; N155DL Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.153 Mobile Safari/537.36 ','Mozilla/5.0 (Linux; Android 12; N155DL Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36','Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; WebView/2.0; rv:11.0; IEMobile/11.0','Mozilla/5.0 (Linux; Android 11; Nokia 6.1 Plus Build/RQ3A.210905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.153 Mobile Safari/537.36 ','Mozilla/5.0 (Linux; arm; Android 11; Nokia 1 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.4515.159 YaApp_Android/121.81.1 YaSearchBrowser/121.81.1 BroPP/1.0 SA/3 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.1.2; en-US; Nokia_Xplus Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.9.1155 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; Nokia 2 V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36']
       
        headerss ={
             "User-Agent":random.choice(useragent)

        }
        print ("")
        if file == "n":
        
            for word in o:
                url =user+"/"+f"{word}"
                ip =requests.get("http://api.ipify.org",proxies=proxy,headers=headerss).content
                Agent =requests.get("http://httpbin.org/user-agent",proxies=proxy,headers=headerss).content
           
                get = requests.get(url,"html.parser",proxies=proxy,headers=headerss)
                done =[]
                if get.status_code == 200:
                    done.append(url)
                    print ("[bold green on red][+] Found location:[/]",url,"|","[bold green on red]Ip[/]:","[bold red][/]",ip,"|","Random Agent")
                    print ("___________________________________________________________+_+")
                else:
               
                     pass
                     
        elif file == "y":
             namefile =str(input (red+f"""
 ---(websweep@Ahmed)-[~/{green}Enter [txt,json,php,js,perl]?{red}]
|
 ---$"""+green))
             for word in o:
                    url =user+"/"+f"{word}."+f"{namefile}"
                    ip =requests.get("http://api.ipify.org",proxies=proxy,headers=headerss).content
                    Agent =requests.get("http://httpbin.org/user-agent",proxies=proxy,headers=headerss).content
                        
                    get = requests.get(url,"html.parser",proxies=proxy,headers=headerss)
                    done =[]
                    if get.status_code == 200:
                            red="\033[1;31m"
                            green="\033[1;32m"
                            blue="\033[1;33m"
                            u="\033[1;34m"
                            done.append(url)
                            print ("")
                            print ("")
                            print ("[bold green on red][+] Found location:[/]",url,"|","[bold green on red]MyIp[/]:","[bold red][/]",ip,"|","Random Agent")
                            print ("___________________________________________________________+_+")
                    else:
                             
                        pass
                
      
    except:
        print ("[!] Please Connect in network Or http://127.0.0.1:9050")
        sys.exit()

def pentest():
    red="\033[1;31m"
    green="\033[1;32m"
    blue="\033[1;33m"
    u="\033[1;34m"
    print ("""[bold red]



     ____                          _       
    |  _ \ ___ _ __   __   ___   _| |_ __  
    | |_) / _ \ '_ \  \ \ / / | | | |  _ \ 
    |  __/  __/ | | |  \ V /| |_| | | | | |
    |_|   \___|_| |_|___\_/  \___|_|_|  |_|
               |_____|                 

                         Version 1.0
                         
            Test:-> http://localhost.com
            Error:-> http://localhost.com/
   [/] """)

    print ("")
    proxy ={
        "http":"socks5://127.0.0.1:9050",
        "https":"socks5://127.0.0.1:9050"
    }
    useragent =['Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.0.1.56','Mozilla/5.0 (Linux; Android 9; LAVA LE9830 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; N155DL Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.153 Mobile Safari/537.36 ','Mozilla/5.0 (Linux; Android 12; N155DL Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36','Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; WebView/2.0; rv:11.0; IEMobile/11.0','Mozilla/5.0 (Linux; Android 11; Nokia 6.1 Plus Build/RQ3A.210905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.153 Mobile Safari/537.36 ','Mozilla/5.0 (Linux; arm; Android 11; Nokia 1 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.4515.159 YaApp_Android/121.81.1 YaSearchBrowser/121.81.1 BroPP/1.0 SA/3 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.1.2; en-US; Nokia_Xplus Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.9.1155 Mobile Safari/537.36']
    headerss ={
             "User-Agent":random.choice(useragent)

        }
    print ("")
    print ("")
    time.sleep(1)
    
    ta=input (red+f"""
 ---(websweep@Ahmed)-[{green}~/Enter Target{red}]
|
 ---$"""+green)
    print ("")
    time.sleep(2)
    print ("[bold green]________________[/]STARTING[bold red]_________________[/]")
    print ("")
    time.sleep(1)
    word =requests.get(ta,proxies=proxy,headers=headerss).text
    if "wp-content" in word:
        print ("[bold green][+] Found Wordpress[/]")
        print ("____________________________________-")
        print ("[bold green][*] Test Wordpress...[/]")
        print ("____________________________________")
        time.sleep(2)
        f =requests.get(ta+"/wp-content/uploads/",proxies=proxy,headers=headerss)
        url =ta+"/wp-content/upload"
        if f.status_code == 200:
            print (f"[bold green][+] Found :[bold red]{url}[/]")
        users =ta+"/wp-json/wp/v2/users"
        user =requests.get(ta+"/wp-json/wp/v2/users",proxies=proxy,headers=headerss)
        if user.status_code == 200:
             print (f"[bold green][+] Found usernames:[bold red]{users}[/]")
        x =ta+"/readme.html"
        c =requests.get(ta+"/readme.html",proxies=proxy,headers=headerss)
        if c.status_code == 200:
             print (f"[bold green][+] Found :[bold red]{x}[/]")
        
    print ("")
    print ("__________________________^_^GO")
    robots =requests.get(ta+"/robots.txt",proxies=proxy,headers=headerss)
    if robots.status_code == 200:
        print ("[bold green][Info] robots.txt[/]")
        time.sleep(2)
        x =robots.text
        r= x.splitlines()
        for i in r:
            print (i)
    
              
    print ("")        
    print ("")
    print ("[bold green][+]  Technology used...[/]")
    time.sleep(1)
    info =requests.get(ta,proxies=proxy,headers=headerss)
    with open("info.txt","w") as k:
        for key ,value in info.headers.items():
            k.write(f"{key}:{value}")
    print ("[Info]",info.headers.items)
    time.sleep(1)

    infos = open("info.txt","rb").read()

    x =re.findall(f"PHP/\d+(?:\.\d+)*",str(infos))

    if x:
        for i in x:
            c =i.replace("/"," ")
            print("______________________________")
            print (f"[bold green][*] Test Exploit-->[/]:[bold red]{c}[/]")
            print ("_____________________________")
            print ("")
            c =i.replace("/"," ")
            time.sleep(2)
            os.system(f"searchsploit {c}")

    
    ##########APche
    x =re.findall(f"Apache/\d+(?:\.\d+)*",str(infos))
    if x:
        for i in x:
            c =i.replace("/"," ")
            print("______________________________")
            print (f"[bold green][*] Test Exploit-->[/]:[bold red]{c}[/]")
            print ("_____________________________")
            print ("")
            c =i.replace("/"," ")
            time.sleep(2)
            os.system(f"searchsploit {c}")
    ###############openssl

    x =re.findall(f"OpenSSL/\d+(?:\.\d+)*",str(infos))
    if x:
        for i in x:
            c =i.replace("/"," ")
            print("______________________________")
            print (f"[bold green][*] Test Exploit-->[/]:[bold red]{c}[/]")
            print ("_____________________________")
            print ("")
            c =i.replace("/"," ")
            time.sleep(2)
            os.system(f"searchsploit {c}")
    
    
    time.sleep(1)
    print ("")
    print  ("[bold green][*] Scan ports...[/]")
    print ("")
    time.sleep(2)
    ports =[]
    
    for i in ['21','22','23','25','443','80','51','110','512','1099','514','3632','2049','49180','8080','10000','5432']:
        try: 
            test=requests.get(f"{ta}:{i}",proxies=proxy,headers=headerss,timeout=1)
            ports.append(i)
            print (f"[bold green][+] open :{i}[/]")
        except:
            print (f"[bold red][-] closed port: {i}[/]")
    time.sleep(1)
    for i in ports:
        print("")
        print ("_______________________________________________")
        print (f"[bold green][*] Test port:[/] [bold red]{i}[/]")
        print ("_______________________________________________")
        time.sleep(1)
        print ("")
        urls = f"{ta}:{i}\n"
        print ("")
        print ("_______________________________________________")
        print ("[bold green] [*] Test:[/]",f"[bold red]{urls}[/]")
        print ("_______________________________________________")
    
        with open("u.txt","a") as url:
            url.write(urls)
        para =[]    
        print ("")
        time.sleep(2)
        
        time.sleep(1)
       
        os.system(f"proxychains cat u.txt |waybackurls > url.txt")
        time.sleep(2)
        if os.path.getsize("url.txt") == 0:
         
            print ("[bold red][-] Url NotFound ![/]")

        else:
            s=open("url.txt","rb").read()
            p =s.splitlines()
            c=len(p)
            print (f"[bold green][+] Found [/]{c} [bold red]Link +_+[/]")
            time.sleep(4)
            for js in p:
                
               
                print ("")
                print (f"[bold green][+] Found Link[/] :[bold red] {js}[/]")
        print ("")
        print ("")
        print ("_________________________________")
        print ("[bold green][*] Test File js...[/]")
        print ("_________________________________")
        time.sleep(1)
        with open("js.sh","a") as js:
            js.write(f"proxychains echo '{ta}' |gospider|grep '.js$' > js ")
           
        
        time.sleep(2)
        os.system("bash js.sh")
        with open("js","rb") as k:
            s =k.read()

            if s.strip() == '':
                print ("[-] Js Notfound ")
            else:
                s=open("js","rb").read()
                p =s.splitlines()
                for js in p:
                    print (f"[bold green][+] Found[/] :[bold red] {js}[/]")
                    print ("")
        if os.path.getsize("js") == 0:
        
            print ("[bold red][-] Js File Notfound [/]")

        else:
            print ("__________________________~")
            print ("[bold green][*] Test Vuln... [/]")
            print ("___________________________")
            time.sleep(2)
            os.system("cat js |mantra")

        time.sleep(2)
        print ("____________________________")
        print ("[bold green on red][*] Test Xss.. [/]")
        print ("____________________________")
        print ("")
        if os.path.getsize("url.txt") == 0:
            print ("[bold red][-] NotFound Xss[/]")
        else:
            os.system("proxychains cat url.txt |kxss > xss.txt")
        time.sleep(1)
        try:
            if os.path.getsize("xss.txt") == 0:
                print ("[bold red][-] Notfound Xss[/]")
            else:
                s =open("xss.txt",'rb').read()

                x= s.splitlines()
                s =len(x)
                print(f"[bold green][+] Found {s}[/] [bold red]Link Xss -_+[/]")
                time.sleep(4)
                for z in x:
                    
                   
                    print (f"[bold green][+] Found [/]:[bold red]{z}[/]")
        except:
            print ("[bold red][-] Sorry Please waite....[/]")
            time.sleep(2)
        print ("")
        print ("_______________________")            
        print ("[bold green][*] Search Subdomain...[/]")
        print ("_______________________")
        s= f"{ta}"
        domin = s.split("//")[-1].split("/")[0]

        os.system(f"subfinder -d {domin} > sub.txt ")

        if os.path.getsize("sub.txt") == 0:
            print ("[bold red][-] Subdomin NotFound [/]")

        else:
            s =open("sub.txt","rb").read()

            v =s.splitlines()
            l =len(v)
            print (f"[bold green ][+] Found Subdomin[/]:[bold red]{l}[/]")
            for i in v:
                print (f"[bold green][+] Sub Found[/]: [bold red]{i}[/]")

        print ("")
        print ("__________________________")        
        print ("[bold green][*] Test Takeover Vuln...[/]")
        print ("__________________________")
        time.sleep(2)
        os.system("proxychains subzy run --targets sub.txt")
        print ("")
        print ("[bold green][+_+] Done Bay[/]")
    try:
        os.remove("info.txt")
    except:
        print("[ERROR] ~_! Notfound Port")
    try:
        os.remove("js")
    except:
        print ("[ERROR] !_+ Notfound Port")
    try:
        os.remove("u.txt")
    except:
         print("[ERROR] ~_! Notfound Port")
    try:
        os.remove("sub.txt")
    except:
        print("[ERROR] ~_! Notfound Port")
    try: 
        os.remove("xss.txt")
    except:
         print("[ERROR] ~_! Notfound Port")
    try:
        os.remove("url.txt")
    except:
        print("[ERROR] ~_! Notfound Port")
    try:
        os.remove("js.sh")
    except:
        print("[ERROR] ~_! Notfound Port")
def Tors():
    s =threading.Thread(target=Tor)
    s.start()
##################net
def update():
    red="\033[1;31m"
    green="\033[1;32m"
    blue="\033[1;33m"
    u="\033[1;34m"



    ##########
    print("")
    user =input (red+f"""
 ---(websweep@Ahmed)-[{green}~/DO You Want Update [n/y] ?{red}]
|
 ---$"""+green)
    if user == "y":

        br=mechanize.Browser()
        url= "http://websweeb.unaux.com/v1.txt"
        test =br.open(url)
        upp =test.read().decode()
        with open(__file__ ,"w") as up:
            up.write(str(upp))
        time.sleep(3)
        print ("[bold green][+] Done Update[/][bold red] *_*[/]")  
        time.sleep(2)
        print ("")
        print ("[bold green][+] Please return run websweep[/]")
    elif user == "n":
        b=mechanize.Browser()
        ur ="http://websweeb.unaux.com/v2.txt"
        t=b.open(ur)
        dd =t.read().decode()
        with open(__file__,"w") as d:
            d.write(str(dd))
            sys.exit()
    else:
       print("[bold red][-] Comnd Not found[/]")
       sys.exit()




#################
def net():
    red="\033[1;31m"
    green="\033[1;32m"
    blue="\033[1;33m"
    u="\033[1;34m"
    print(f"""[bold blue ]


      <-----------------------WELCOME TO WebSweep---------------------->  
                                                                  version:1.0

                         Ethical Hacker: Ahmed_mahmoud 
                         
           |   FACEBOOK:https://www.facebook.com/ahmed.mahmou.2025  |
                         |_____________________________|
                                   |Years:20|
    [/]""")
    print ("")
    os.system("sudo echo """)
    print("[bold red][*] Cheack Internet...[/]")
    time.sleep(2)
    proxy ={
             "http":"socks5://127.0.0.1:9050",
             "https":"socks5://127.0.0.1:9050"
         }
    useragent =['Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.0.1.56','Mozilla/5.0 (Linux; Android 9; LAVA LE9830 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; N155DL Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.153 Mobile Safari/537.36 ','Mozilla/5.0 (Linux; Android 12; N155DL Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36','Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; WebView/2.0; rv:11.0; IEMobile/11.0','Mozilla/5.0 (Linux; Android 11; Nokia 6.1 Plus Build/RQ3A.210905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.153 Mobile Safari/537.36 ','Mozilla/5.0 (Linux; arm; Android 11; Nokia 1 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.4515.159 YaApp_Android/121.81.1 YaSearchBrowser/121.81.1 BroPP/1.0 SA/3 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.1.2; en-US; Nokia_Xplus Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.9.1155 Mobile Safari/537.36']
    headerss ={
                  "User-Agent":random.choice(useragent)
     
             }
    try:
        test=requests.get("https://google.com")
        print ("")
        print ("[bold green][+] Found INTERNET[/] [bold red] +_+[/]")
        time.sleep(1)
        os.system("sudo service tor start")
        print("")
        print ("[bold red][*] Cheack Update...[/]")
        time.sleep(2)
    except:
        print("[bold red ][-] Please Connect in Internet ~_~[/]")
    br=mechanize.Browser()
    url= "http://websweeb.unaux.com/v1.txt"
    test =br.open(url)
    upp =test.read().decode()
    print ("")
    s =open(__file__,"r").read()
    if upp == s:
        time.sleep(3)
        print ("")
        print ("[bold red][+] NOT FOUND UPDATE[/]")
        time.sleep(3)
        os.system("clear")
        main()
    else:
        print ("")     
        print ("[bold green][+] FOUND UPDATE ^_^[/]")
        time.sleep(2)
        print("")
        update()
def main():
    red="\033[1;31m"
    green="\033[1;32m"
    blue="\033[1;33m"
    u="\033[1;34m"
    print(f"""[bold blue ]


      <-----------------------WELCOME TO WebSweep---------------------->  
                                                                  version:1.0

                         Ethical Hacker: Ahmed_mahmoud 
                         
           |   FACEBOOK:https://www.facebook.com/ahmed.mahmou.2025  |
                         |_____________________________|
                                   |Years:20|
    [/]""")
    
    red="\033[1;31m"
    green="\033[1;32m"
    blue="\033[1;33m"
    u="\033[1;34m" 
    print ("")
    print ("")
    print ("")
    time.sleep(1)
    p="""
                                [1] Pentest website
    """
    s ="""
                                [2] Search Files in Website
       """
    ex="""
                                [3] Exit
   """
    print (f"[bold  red] {p}[/]")
    time.sleep(1)
    print ("")
    time.sleep(1)
    print (f"[bold  red] {s}[/]")
    print ("")
    time.sleep(1)
    print(f"[bold  red] {ex}[/]")
    red="\033[1;31m"
    green="\033[1;32m"
    blue="\033[1;33m"
    u="\033[1;34m"
    mainus =input (red+f"""
 ---(websweep@Ahmed)-[{green}~/Enter Number{red}]
|
 ---$"""+green)
    if mainus == "1":
        
        time.sleep(1)
        os.system("clear")
        pentest()
        time.sleep(1)
    if  mainus == "2":
        search()
        


    elif mainus == "3":
        sys.exit()

    else:
        print ("[!] Comnd notFound ")
        
def search(): 
    red="\033[1;31m"
    green="\033[1;32m"
    blue="\033[1;33m"
    u="\033[1;34m"
    user =input (red+f"""
 ---(websweep@Ahmed)-[~/{green}Do You want Search in network Tor [n/y]{red}]
|
 ---$"""+green)

        
            
    if user == "n":
        notor()
        
    elif user == "y":
        Tors()
              
    else:
        return user
        
    


 
        
    


net()
