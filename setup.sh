sudo apt install exploitdb -y
sudo apt remove fuff -y
sudo apt install python3 
sudo apt install wpscan -y
sudo apt install subfinder -y
sudo apt remove httpx -y && rm /usr/bin/httpx
sudo apt install golang-go -y
sudo git clone https://github.com/hahwul/dalfox.git && cd dalfox && go build dalfox.go && cp dalfox /usr/sbin && git clone https://github.com/devanshbatham/ParamSpider.git && cd ParamSpider && python3 setup.py install
sleep 2
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
echo "[*] Done install"
sudo cp /usr/bin/httpx /usr/sbin
sleep 2
echo "[*] Please Waite ..."
cd Toolls && chmod +x * && cd .. && cd tools && chmod +x * && cd .. && cd Tools && chmod +x * && cd ..


sleep 3
sudo cp tools/ffuf /usr/sbin 
sudo cp Tools/mantra /usr/sbin 
sudo cp Tools/kxss /usr/sbin 
sudo cp tools/waybackurls /usr/sbin
sudo cp Toolls/gospider /usr/sbin
sudo cp Tools/subzy /usr/sbin

sudo cp Toolls/openredirex /usr/sbin


sleep 2
sudo pip  install -r requirements.txt 
wpscan --update
echo "[*] Done +_+ "
