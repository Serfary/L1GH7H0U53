ping -c 4 8.8.8.8 > /dev/null 2>&1

if [ $? != 0 ]
then
    sudo ip link set wlan0 down
    sleep 5
    sudo ip link set wlan0 up
    sleep 5
    sudo -u serfary git -C /home/serfary/L1GH7H0U53 fetch --all
    sudo -u serfary git -C /home/serfary/L1GH7H0U53 reset --hard origin/main
    sudo -u serfary git -C /home/serfary/L1GH7H0U53 pull
fi
