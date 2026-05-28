apt update
apt install git hashcat screen fcrackzip qtbase5-dev -y
if [ -d "L1GH7H0U53" ]; then
    git -C "L1GH7H0U53" pull
else
    git clone https://github.com/Serfary/L1GH7H0U53.git
fi

cp /home/serfary/L1GH7H0U53/L4B5/537UP/pm3 /usr/local/bin/
cp /home/serfary/L1GH7H0U53/L4B5/537UP/proxmark3 /usr/local/bin/
cp /home/serfary/L1GH7H0U53/L4B5/537UP/wifi-check.cron /etc/cron.d/

chmod +x /home/serfary/L1GH7H0U53/L4B5/537UP/wifi-check.sh

