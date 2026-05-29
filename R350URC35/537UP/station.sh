apt update
apt install git hashcat screen fcrackzip python3-bcrypt qtbase5-dev -y
if [ -d "L1GH7H0U53" ]; then
    sudo -u serfary git -C /home/serfary/L1GH7H0U53 reset --hard origin/main
    sudo -u serfary git -C /home/serfary/L1GH7H0U53 clean -fd
    sudo -u serfary git -C /home/serfary/L1GH7H0U53 pull
else
    sudo -u serfary git clone https://github.com/Serfary/L1GH7H0U53.git
fi

cp /home/serfary/L1GH7H0U53/L4B5/537UP/pm3 /usr/local/bin/
cp /home/serfary/L1GH7H0U53/L4B5/537UP/proxmark3 /usr/local/bin/

