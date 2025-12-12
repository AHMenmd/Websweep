sudo apt update && sudo apt upgrade
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
