apt update
apt install git hashcat screen build-essential pkg-config libreadline-dev gcc-arm-none-eabi libnewlib-dev qtbase5-dev -y
git clone https://github.com/Serfary/L1GH7H0U53.git
git clone https://github.com/RfidResearchGroup/proxmark3.git
cd proxmark3
make clean && make all
make install
