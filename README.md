# Websweep
This tool is designed to detect website vulnerabilities, such as XSS vulnerabilities, SQL injection vulnerabilities, OpenDirect vulnerabilities, and others. It scans for vulnerabilities and extracts the target website's subdomain for analysis, along with its URLs. It also scans for open ports and reveals hidden files within the website. The tool also supports WordPress site scanning and utilizes powerful tools such as nmap, HTTPx, WhatWeb, sqlmap, Dalfox, GoSpider, and WPScan.
# 1 Setup
bash setup.sh
# 2 install
sudo cp /usr/local/bin/httpx /usr/sbin && git clone https://github.com/hahwul/dalfox.git && cd dalfox && go build dalfox.go && cp dalfox /usr/sbin

# Run
python3 websweep.py
# Image 
![Tool](https://github.com/AHMenmd/Websweep/blob/main/websweep.png?raw=true)
