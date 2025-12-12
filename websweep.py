import re
import requests 
import sys 
import time
import os
import random
import threading
from rich import print
import mechanize





        
           

            
############
def logo():

                            



                                                                                         
    s=f""" [bold green]                                                          
                                                                                           Search urls
                                                                                          |
                                                                                  __ Search Subdomain
                                                                                 |        
                                                                         Scan Ports  
                                                                                 |________
                                                                                           |
                                                                                    Search Hidden Files
             [bold blue]    Status[/]:[bold green]On[/]                      ________                                    |_  
                                               |        |                                    |
        PenTest_Web_Application                |        |                              ______|____________Takeover
    ___________________________________________|        |                             |
   |__________--+_________Websweep___ver 1.0__ |        |                  sql<---------------->Xss                                                                                                                                                                
                                               |________|                             |                                                                                                                               
                                               [/]                       [bold red]          Open redirct[/] 
                                               
            [bold green ]Test--> http://localhost.com[/]
         [bold green]   Code by--->[/][bold red] https://www.facebook.com/ahmed.Zeroz.2025[/] 
            [bold red]ERROR--> http://localhost.com/ [/]                                 
    """                                        
    print(s)
    print ("")

def pentest():
    logo()
  
    print ("")
    try:
        os.system("rm -rf results")
    except:
        pass
    try:
        os.remove("urlactive.txt")
    except:
        pass
    try:
        os.remove("active.txt")
    except:
        pass
    try:
        os.remove("info.txt")
    except:
        pass
    try:
        os.remove("js")
    except:
        pass
    try:
        os.remove("u.txt")
    except:
        pass
    try:
        os.remove("sub.txt")
    except:
        pass
    try: 
        os.remove("xss.txt")
    except:
        pass
    try:
        os.remove("url.txt")
    except:
        pass
    try:
        os.remove("js.sh")
    except:
        pass
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
    red="\033[1;31m"
    green="\033[1;32m"
    blue="\033[1;33m"
    u="\033[1;34m"

    
    ta=input (red+f"""
 ---(websweep@Ahmed)-[{green}~/Enter Target url{red}]
|
 ---$"""+green)
    print ("")
    time.sleep(2)
    if ta.endswith("/"):
        print (f"[bold red][!] Try -> http://localhost.com [/]")
        sys.exit()
    print ("[bold white on green]|*|_____________|-STARTING Websweep-|___________|*|[/]")
    time.sleep(2)
    print("")
    print ("[bold green on red][*][/][bold green] Test WAF ....[/]")
    time.sleep(1)
    print ("")
    os.system(f"wafw00f {ta}")    
  #  print ("[bold green]________________[/]STARTING[bold red]_________________[/]")
    print ("")
    #time.sleep(1)
    
    print ("")
    time.sleep(2)
    word =requests.get(ta,headers=headerss).text
    if "wp-content" in word:
        print ("______________________________________")
        print ("[bold green on red][+] Found Wordpress[/]")
        print ("")
        print ("________________________________________")
        print ("[bold green][*][/][bold blue] Test Wordpress..[/]")
        
        print("")
        time.sleep(2)
        f =requests.get(ta+"/wp-content/uploads/",headers=headerss)
        url =ta+"/wp-content/upload"
        if f.status_code == 200:
            print (f"[bold green][+] Found :[bold red]{url}[/]")
        users =ta+"/wp-json/wp/v2/users"
        user =requests.get(ta+"/wp-json/wp/v2/users",headers=headerss)
        if user.status_code == 200:
             print (f"[bold green][+] Found usernames:[bold red]{users}[/]")
        x =ta+"/readme.html"
        c =requests.get(ta+"/readme.html",headers=headerss)
        if c.status_code == 200:
             print (f"[bold green][+] Found :[bold red]{x}[/]")
        print("")
        print ("************************************")
        print ("[bold green][*][/][bold red] Starting Wpscan PLease waite.....[/]")
        print ("")
        time.sleep(2)
        os.system(f"wpscan --url {ta}")
        
    print ("")

    robots =requests.get(ta+"/robots.txt",headers=headerss)
    if robots.status_code == 200:
        print ("[bold green on red][+][/] [bold green]robots.txt[/]")
        time.sleep(2)
        x =robots.text#_______++
        print (x)
        time.sleep(1)
        print ("")
        if "wp-content" not in word:
            if "wp-admin" in x:
                print ("________________________")
                print (f"[bold green on red][+] %40 Found Wordpress [/]")
                print ("")
                print ("____________________________________")
                print ("[bold white on green][*] Starting Wpscan PLease waite.....[/]")
                time.sleep(1)
                os.system(f"wpscan --url {ta}")
            else:
                pass
                
            time.sleep(1)
            print ("")
            
        #r= x.splitlines()
        #for i in r:
        #    print (i)
    
              
    print ("")        
    print ("")
  #  print ("[bold white on green][+]  Technology used...[/]")
    print ("")
    #os.system(f"whatweb {ta}")

    ###############openssl
    print ("[bold white on green][+]  Technology used...[/]")
    time.sleep(1)
    info =requests.get(ta)
    with open("info.txt","w") as k:
        for key ,value in info.headers.items():
            k.write(f"{key}:{value}")
    os.system(f"whatweb {ta}")
    print ("[Info]",info.headers.items)
    time.sleep(1)
    
    infos = open("info.txt","rb").read()
    
    x =re.findall(f"PHP/\d+(?:\.\d+)*",str(infos))
    
    if x:
        for i in x:
            c =i.replace("/"," ")
            print("______________________________")
            print (f"[bold green on red][*] Search Exploit-->[/]:[bold red]{c}[/]")
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
            print (f"[bold green on red][*] Search Exploit-->[/]:[bold red]{c}[/]")
            print ("_____________________________")
            print ("")
            c =i.replace("/"," ")
            time.sleep(2)
            os.system(f"searchsploit {c}")
        ##################nginx
    x =re.findall(f"nginx/\d+(?:\.\d+)*",str(infos))
    if x:
        for i in x:
            c =i.replace("/"," ")
            print("______________________________")
            print (f"[bold green on red][*] Search Exploit-->[/]:[bold red]{c}[/]")
            print ("_____________________________")
            print ("")
            c =i.replace("/"," ")
            time.sleep(2)
            os.system(f"searchsploit {c}")

        #######Bo
    x =re.findall(f"Bootstrap/\d+(?:\.\d+)*",str(infos))
    if x:
        for i in x:
            c =i.replace("/"," ")
            print("______________________________")
            print (f"[bold green on red][*] Search Exploit-->[/]:[bold red]{c}[/]")
            print ("_____________________________")
            print ("")
            c =i.replace("/"," ")
            time.sleep(2)
            gos.system(f"searchsploit {c}")
            ##################nginx
        x =re.findall(f"nginx/\d+(?:\.\d+)*",str(infos))
        if x:
                for i in x:
                    c =i.replace("/"," ")
                    print("______________________________")
                    print (f"[bold green on red][*] Search Exploit-->[/]:[bold red]{c}[/]")
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
            print (f"[bold green on red][*] Search Exploit-->[/]:[bold red]{c}[/]")
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
            test=requests.get(f"{ta}:{i}",headers=headerss,timeout=1)
            ports.append(i)
            print (f"[bold green][+] open :{i}[/]")
        except:

            print (f"[bold red][-] closed port: {i}[/]")
    Url =f"{ta}"
    o=Url.split("//")[-1].split("/")[0]
    
    
    time.sleep(1)
    for p in ports:
        print("")
        print ("_______________________________________________")
        print (f"[bold white on green][*] Test port:[/] [bold red]{p}[/]")
        os.system(f"nmap -T4 -Pn -sVC {o} --script='vuln' -p {i}")
        time.sleep(1)
        print ("")
        urls = f"{ta}:{p}\n"
        print ("")
        print ("_______________________________________________")
    try:
        print (f"[bold white on green] [*] Search Urls:[/]",f"[bold red]{urls}[/]")
    except:
        print("[bold red][!][/] [bold green]Sorry Not Open Port Please Try Again[/]")  
        sys.exit()  
    
    with open("u.txt","a") as url:
        url.write(urls)
    para =[]    
    print ("")
    time.sleep(2)
        
    time.sleep(1)
       
    os.system(f"  cat u.txt |timeout 250 waybackurls > url.txt")
    time.sleep(2)
    if os.path.getsize("url.txt") == 0:
         
        print ("[bold red][-] Url NotFound ![/]")

    else:
        s=open("url.txt","rb").read()
        p =s.splitlines()
        c=len(p)
        print (f"[bold green][+] Found [/]{c} [bold red]Link +_+[/]")
        time.sleep(4)
        print ("")
        for js in p:
                
               
            print ("[bold green] [+] Found Url:[/]",js)
        #print (s)
    print("")
    print (f"[bold white on green][*] Cheack URL Active :[/] [bold red]*_*[/]")
    print("")
    os.system("cat url.txt |timeout 250 httpx > urlactive.txt")
    if os.path.getsize("urlactive.txt") == 0:
        print ("")
        print ("[bold red][!][/] [bold green]NotFound Url Active[/]")
    else:
        ac =open("urlactive.txt","r").read()
        u =ac.splitlines()
        l =len(u)
        print ("")
        print(f"[bold green on red][+][/] [bold green]Found URL {l} Active[/]")
    time.sleep(2)
    print ("")
    print ("")
    print ("_________________________________")
    print ("[bold white on green][*] Search File js...[/]")
    print ("_________________________________")
    time.sleep(1)
    with open("js.sh","a") as js:
        js.write(f" echo '{ta}' |gospider|grep '.js$' > js ")
           
        
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
        print ("[bold green on red][*] Search Vuln... Js [/]")
        print ("___________________________")
        time.sleep(2)
        os.system("cat js |mantra")

    time.sleep(2)
    print ("____________________________")
    print ("[bold white on green][*][/][bold green] search url 45% Xss [/]")
    print ("____________________________")
    print ("")
            #time.sleep(2)
    if os.path.getsize("urlactive.txt") == 0:
            print ("[bold red][-] NotFound Xss[/]")
    else:
        
        os.system("cat url.txt |timeout 90 kxss > xss.txt")
        time.sleep(3)
       # pyautogui.hotkey("ctrl","z")
        #print ("Done Save Xss.txt")
        
        #print ("erorr Save Xss.txt")
        time.sleep(1)
        if os.path.isfile("xss.txt"):   
            if os.path.getsize("xss.txt") == 0:
                print ("[bold red][-] Notfound Xss[/]")
            else:
                s =open("xss.txt",'r').read()
        
                x= s.splitlines()
                s =len(x)
                print(f"[bold green][+] Found {s}[/] [bold red]Link 44% Xss -_+[/]")
                print ("")
                time.sleep(4)
                for z in x:
                    print (f"[bold green][+] Found [/]:[bold red]{z}[/]")
                    ###################TEST Xss
                    print ("")
               
                    
                
                time.sleep(2) 
        else:
            print  ("[bold red][!][/][bold green] Xss url NotFound[/] ")
    print("")
    do = ta.split("//")[-1].split("/")[0]    
    print (f"[bold green on red][*][/] [bold green]Search Parametar[/] ->[bold red] {do} [/]")
    print ("")
    os.system(f'paramspider -d ""{do}"" ')
    pat =os.path.abspath(sys.argv[0]).split("Websweep")[0]
    
    try:
        if os.path.getsize(f"{pat}Websweep/results/{do}.txt") != 0:
            print ("")
            xx =open(f"{pat}Websweep/results/{do}.txt","r").read()
            ones =xx.splitlines()
            l =len(ones)
            print (f"[bold green on red][+][/] [bold red] Found {l} Parametar [/] ")
            ######dalfox!
            print ("___________________________________________")
            print ("")
            print (f"[bold green on red][*][/] [bold green] Test Xss [/]")
            print ("")
            time.sleep(2)
            os.system(f"dalfox file {pat}Websweep/results/{do}.txt")
            print("")
            print ("[bold green][*][/] [bold red] Test Sql Ingeqtion ...[/]")
            time.sleep(4)
            os.system(f"sqlmap -m  {pat}Websweep/results/{do}.txt --batch --random-agent")
            print ("")
            time.sleep(2)
            ##########redirct
            print ("[bold green][*][/] [bold red]Test Redirct..[/]")
            time.sleep(2)
            os.system("cat {pat}Websweep/results/{do}.txt |openredirex")
            print ("")
            def path():
                print ("[bold green][*][/] [bold red ]Test Path traversal ...[/]")
                time.sleep(1)
            
                par =open(f"results/{do}.txt","r").read()
            
                ones =par.splitlines()
                print ("")
                for i in ones:
                    p =i.split("?")[-1].split("FUZZ")[0]
                    print (f"[bold green][*][/] [bold blue]Test Parameter[/] :[bold red]{p}[/]")
                    time.sleep(3)
                    os.system(f"ffuf -u {i} -w payload/path.txt -mc 200,302 -fs 0")
                    print ("[bold red]<===============================================================>[/]")
            path()
            
        else:
            print ("[bold red][!][/] [bold green] Sorry Parameter NotFound[/] ")
    except:
        print ("[bold red][!][/] [bold green] Sorry Parameter NotFound[/] ")
        
        
    print ("[bold yellow]<===============================================================>[/]")    
    print ("")
    print ("[bold green][*][/] [bold red] Search Hidden Files..[/]")
    time.sleep(2)
    os.system(f"ffuf -w payload/files.txt -u {ta}/FUZZ -t 30 -mc 200,302")    
    print ("")
    print ("_______________________")            
    print ("[bold white on green][*] Search Subdomain...[/]")
    print ("_______________________")
    s= f"{ta}"
    
    domin = s.split("//")[-1].split("/")[0]

    os.system(f"subfinder -d {domin} > sub.txt ")

    if os.path.getsize("sub.txt") == 0:
            print ("[bold red][-] Subdomin NotFound [/]")

    else:
            #s =open("sub.txt","rb").read()

            #v =s.splitlines()
            #l =len(v)
            #print (f"[bold green ][+] Found Subdomin[/]:[bold red]{l}[/]")
        time.sleep(2)
        print ("")
            #print (f"[bold green ][*] Cheack Subdomin[/]:[bold red]{l}[/]")
        print("")
       # num =[]
      #  on =[]
        sub =open("sub.txt","rb").read()
       
        t =sub.splitlines()
       # on.append(t)
       # x =len(t)
      #  print (f"[bold green on red] [+] Found[/] {x} Subdomain ")
        print ("")
        time.sleep(2)
        print("")
        print ("[bold green on red][*] Cheack Subdomain Active[/] ")
        os.system("cat sub.txt |httpx > active.txt")
        print ("")
        sub =open("active.txt","rb").read()
       
        s =sub.splitlines()
       # on.append(t)
        x =len(s)
        print (f"[bold green on red] [+] Found[/] {x} Subdomain Active")
        print ("__________________________")        
        print ("[bold white on green ][*] Test Takeover Vuln...[/]")
        print ("__________________________")
        time.sleep(2)
        os.system("  subzy run --targets active.txt")
        time.sleep(2)

        
       
        time.sleep(2)
        print ("")
        ############ScanSubdoman--
        def subscan():
                print ("")
                time.sleep(1)
                print ("")
                time.sleep(2)
                        
                subs =open("active.txt","r").read()
                        
                sone =subs.splitlines()
                        #http =ta.split(":")[0]
                for sub in sone:
                        print ("[bold blue]<==================================================>[/]")
                        print (f"[bold green][*] Scan Subdomain-->:[/][bold red] {sub} [/]")
                        print("")
                           
                            ###################################3
                            
                            
                        tas =f"{sub}"
                          #  print (ta)
                        word =requests.get(tas).text
                        if "wp-content" in word:
                            print ("______________________________________")
                            print ("[bold green on red][+] Found Wordpress[/]")
                            print ("")
                            print ("________________________________________")
                            print ("[bold green][*][/] [bold red] Test Wordpress..[/]")
                                    
                            print("")
                            time.sleep(2)
                            f=requests.get(tas+"/wp-content/uploads/")
                            url =tas+"/wp-content/upload"
                            if f.status_code == 200:
                                print (f"[bold green][+] Found :[bold red]{url}[/]")
                            users =tas+"/wp-json/wp/v2/users"
                            user =requests.get(tas+"/wp-json/wp/v2/users")
                            if user.status_code == 200:
                                print (f"[bold green][+] Found usernames:[bold red]{users}[/]")
                            x =ta+"/readme.html"
                            c =requests.get(tas+"/readme.html")
                            if c.status_code == 200:
                                print (f"[bold green][+] Found :[bold red]{x}[/]")
                            print("")
                            print ("************************************")
                            print ("[bold green][*][/] [bold red] Starting Wpscan PLease waite.....[/]")
                            print ("")
                            time.sleep(2)
                            os.system(f"wpscan --url {tas}")
                                    
                            print ("")
                            
                        robots =requests.get(tas+"/robots.txt")
                        if robots.status_code == 200:
                            print ("[bold green on red][+][/] [bold green]robots.txt[/]")
                            time.sleep(2)
                            x =robots.text#_______++
                            print (x)
                            time.sleep(1)
                            print ("")
                            if "wp-content" not in word:
                                if "wp-admin" in x:
                                    print ("________________________")
                                    print (f"[bold green on red][+] %40 Found Wordpress [/]")
                                    print ("")
                                    print ("____________________________________")
                                    print ("[bold green][*][/] [bold red]Starting Wpscan PLease waite.....[/]")
                                    time.sleep(1)
                                    os.system(f"wpscan --url {tas}")
                                else:
                                    pass
                                    
                                            
                                            
                                            
                                            
                                time.sleep(1)
                                print ("")
                                       
                                    #r= x.splitlines()
                                    #for i in r:
                                    #    print (i)
                                
                                          
                        print ("")        
                        print ("[bold white on green][+]  Technology used...[/]")
                        print ("")
                        os.system(f"whatweb {tas}")
                        
                            
                                
                        time.sleep(1)
                        print ("[bold red]<=====================================================>[/]")
                        print  ("[bold green][*] Scan ports...[/]")
                        print ("")
                        time.sleep(2)
                        ports =[]
                            
                        for i in ['21','22','23','25','443','80','51','110','512','1099','514','3632','2049','49180','8080','10000','5432']:
                            try: 
                                test=requests.get(f"{tas}:{i}",timeout=1)
                                ports.append(i)
                                print (f"[bold green][+] open :{i}[/]")
                            except:
                            
                                print (f"[bold red][-] closed port: {i}[/]")
                        Url =f"{tas}"
                        o=Url.split("//")[-1].split("/")[0]
                                
                                
                        time.sleep(1)
                        for p in ports:
                            print("")
                            print ("_______________________________________________")
                            print (f"[bold white on green][*] Test port:[/] [bold red]{p}[/]")
                            os.system(f"nmap -Pn {o}  -p {p}")
                            time.sleep(1)
                            ######################
                            #######xX##########33
                        urls = f"{tas}\n"
                        print ("")
                        print ("_______________________________________________")
                        try:
                            print (f"[bold white on green] [*] Search Urls:[/]",f"[bold red]{urls}[/]")
                        except:
                            print("[bold red][!][/] [bold green]Sorry Not Open Port Please Try Again[/]")  
                            sys.exit()  
                            
                        with open("u.txt","a") as url:
                            url.write(urls)
                        para =[]    
                        print ("")
                        time.sleep(2)
                                
                        time.sleep(1)
                               
                        os.system(f"  cat u.txt |timeout 290 waybackurls > url.txt")
                        time.sleep(2)
                        if os.path.getsize("url.txt") == 0:
                                 
                            print ("[bold red][-] Url NotFound ![/]")
                        
                        else:
                            s=open("url.txt","rb").read()
                            p =s.splitlines()
                            c=len(p)
                            print (f"[bold green][+] Found [/][bold blue]{c}[/] [bold red]Link +_+[/]")
                            time.sleep(4)
                            #print ("")
                        
                                #print (s)
                        print("")
                        print (f"[bold white on green][*] Cheack URL Active :[/] [bold red]*_*[/]")
                        print("")
                        os.system("cat url.txt |timeout 280 httpx > urlactive.txt")
                        if os.path.getsize("urlactive.txt") == 0:
                            print ("")
                            print ("[bold red][!][/] [bold green]NotFound Url Active[/]")
                        else:
                            ac =open("urlactive.txt","r",encoding='utf-8',errors='ignore').read()
                            u =ac.splitlines()
                            l =len(u)
                            print ("")
                            print(f"[bold green on red][+][/] [bold green]Found URL {l} Active[/]")
                            print ("")
                            for x in u:
                                print (f"[bold green][+] Found [/]{x} [bold red]Link +_+[/]")
                        time.sleep(2)
                        print ("")
                        print ("")
                        print ("_________________________________")
                        print ("[bold white on green][*] Search File js...[/]")
                        print ("_________________________________")
                        time.sleep(1)
                        with open("js.sh","a") as js:
                            js.write(f" echo '{tas}' |gospider|grep '.js$' > js ")
                                   
                                
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
                            print ("[bold green on red][*] Search api or Token...  [/]")
                            print ("___________________________")
                            time.sleep(2)
                            os.system("cat js |mantra")
                        
                        time.sleep(2)
                        print ("____________________________")
                        print ("[bold white on green][*][/][bold green] search url 45% Xss [/]")
                        print ("____________________________")
                        print ("")
                                    #time.sleep(2)
                        if os.path.getsize("urlactive.txt") == 0:
                                print ("[bold red][-] NotFound Xss[/]")
                        else:
                                
                            os.system("cat url.txt |timeout 190 kxss > xss.txt")
                            time.sleep(3)
                               # pyautogui.hotkey("ctrl","z")
                                #print ("Done Save Xss.txt")
                                
                                #print ("erorr Save Xss.txt")
                            time.sleep(1)
                            if os.path.isfile("xss.txt"):   
                                if os.path.getsize("xss.txt") == 0:
                                    print ("[bold red][-] Notfound Xss[/]")
                                else:
                                    s =open("xss.txt",'r').read()
                                
                                    x= s.splitlines()
                                    s =len(x)
                                    print(f"[bold green][+] Found {s}[/] [bold red]Link 44% Xss -_+[/]")
                                    print ("")
                                    time.sleep(4)
                                    for z in x:
                                        print (f"[bold green][+] Found [/]:[bold red]{z}[/]")
                                            ###################TEST Xss
                                        print ("")
                                        time.sleep(2)
                            
                            
                                            
                                        
                                 
                            else:
                                print  ("[bold red][!][/][bold green] Xss url NotFound[/] ")
                        print ("[bold green][*][/] [bold red] Search Hidden Files..[/]")
                        time.sleep(2)
                        os.system(f"ffuf -w payload/files.txt -u {tas}/FUZZ -t 30")
            
            
            
        subscan()
        
        try:
            os.remove("info.txt")
        except:
            print("[~] -> Exit ")
        try:
            os.remove("js")
        except:
            print ("[~] -> Exit ")
        try:
            os.remove("u.txt")
        except:
            print("[~] -> Exit ")
        try:
            os.remove("sub.txt")
        except:
            print("[~] -> Exit ")
       # try: 
         #   os.remove("xss.txt")
       # except:
            print("[~] -> Exit ")
        try:
            os.remove("url.txt")
        except:
            print("[~] -> Exit ")
        try:
            os.remove("js.sh")
        except:
            print("[~] -> Exit ")
       # try:
        #    os.remove("active.txt")
        #except:
            print ("[*] Refresh ")
        try:
            os.remove("urlactive.txt")
        except:
            print ("[*] Refresh ")
        #############################################ScanSub
        





        ###################del file
        try:
            os.remove("info.txt")
        except:
            print("[~] -> Exit ")
        try:
            os.remove("js")
        except:
            print ("[~] -> Exit ")
        try:
            os.remove("u.txt")
        except:
            print("[~] -> Exit ")
        try:
            os.remove("sub.txt")
        except:
            print("[~] -> Exit ")
       # try: 
         #   os.remove("xss.txt")
       # except:
            print("[~] -> Exit ")
        try:
            os.remove("url.txt")
        except:
            print("[~] -> Exit ")
        try:
            os.remove("js.sh")
        except:
            print("[~] -> Exit ")
        try:
            os.remove("active.txt")
        except:
            print ("[*] Refresh ")
        try:
            os.remove("urlactive.txt")
        except:
            print ("[*] Refresh ")
        try:
            os.system("rm -rf results")
        except:
            print ("[*] Refresh ")
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

#################s

def tools():
    u = ['httpx','openredirex','whatweb','sqlmap','dalfox','gospider','nmap','wpscan','waybackurls','subfinder','searchsploit','kxss','wafw00f','mantra','subzy']

    tools =[]
    for i in u:
        if os.path.isfile(f'/usr/bin/{i}') or os.path.isfile(f'/usr/sbin/{i}') or os.path.isfile(f'/usr/local/bin{i}'):
            print (f"[bold yellow]{i}[/] ->........[bold green][Ok][/]")
            time.sleep(0.2)
            tools.append(i)               
        else:
            print (f"[bold yellow]{i}[/] ->........[bold red][Not installed][/]")


    if len(tools) == 15:
        time.sleep(1)
        os.system("clear")
        

    else:
        print("")
        print ("[bold red][!][/][bold green] Sorry Please installed Tools And try  Again ![/]")
        sys.exit()



#################
def net():
    if os.getuid() == 0:
        pass
    else:
        logo()
        print ("")
        print ("[bold red][!][/][bold green] Please run as root [/]")
        sys.exit()
    red="\033[1;31m"
    green="\033[1;32m"
    blue="\033[1;33m"
    u="\033[1;34m"
    logo()
    print ("")
    tools()
    logo()
    print ("")
    print("[bold red][*] Cheack Internet...[/]")
    time.sleep(2)

    useragent =['Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.0.1.56','Mozilla/5.0 (Linux; Android 9; LAVA LE9830 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; N155DL Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.153 Mobile Safari/537.36 ','Mozilla/5.0 (Linux; Android 12; N155DL Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36','Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; WebView/2.0; rv:11.0; IEMobile/11.0','Mozilla/5.0 (Linux; Android 11; Nokia 6.1 Plus Build/RQ3A.210905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.153 Mobile Safari/537.36 ','Mozilla/5.0 (Linux; arm; Android 11; Nokia 1 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.4515.159 YaApp_Android/121.81.1 YaSearchBrowser/121.81.1 BroPP/1.0 SA/3 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.1.2; en-US; Nokia_Xplus Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.9.1155 Mobile Safari/537.36']
    headerss ={
                  "User-Agent":random.choice(useragent)
     
             }
    try:
        test=requests.get("https://google.com")
        #print ("")
        print ("[bold green][+] Found INTERNET[/] [bold red] +_+[/]")
        time.sleep(1)
        
        #print("")
        print ("[bold green][*][/] [bold red] Cheack Update...[/]")
        time.sleep(2)
    except:
        print("[bold red ][-] Please Connect in Internet ~_~[/]")
        sys.exit()
    br=mechanize.Browser()
    url= "http://websweeb.unaux.com/v1.txt"
    test =br.open(url)
    upp =test.read().decode()
    #print ("")
    s =open(__file__,"r").read()
    if upp == s:
        time.sleep(3)
        #print ("")
        print ("[bold red][+] NOT FOUND UPDATE[/]")
        time.sleep(3)
        os.system("clear")
        pentest()
    else:
        #print ("")     
        print ("[bold green][+] FOUND UPDATE ^_^[/]")
        time.sleep(2)
        print("")
        update()

        
    
os.system("clear")
net()
#pentest()
os.system("clear")

#c