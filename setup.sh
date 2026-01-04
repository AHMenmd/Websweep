
sudo apt install searchsploit -y
sudo apt remove fuff -y
sudo apt install python3 
sudo apt install wpscan -y
sudo apt install subfinder -y
sudo apt install httpx -y 
sleep 2

echo "[*] Done install"
sleep 2
echo "[*] Please Waite ..."

sleep 3
sudo mv tools/ffuf /usr/sbin 
sudo mv Tools/mantra /usr/sbin 
sudo mv Tools/kxss /usr/sbin 
sudo mv tools/waybackurls /usr/sbin
sudo mv Toolls/gospider /usr/sbin
sudo mv Tools/subzy /usr/sbin

sudo mv Toolls/openredirex /usr/sbin


sleep 2
sudo pip  install -r requirements.txt 
wpscan --update
echo "[*] Done +_+ "
