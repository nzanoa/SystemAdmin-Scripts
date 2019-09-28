#! /bin/bash
clear
echo
echo "##############################################"
echo "################# PING SWEEP #################"
echo "##############################################"
echo
echo " The Script accept only a Network-IP as argument"
echo " eg. ping_sweep 192.168.4.0"
echo

echo $1 > .ping_sweep_ip
SUBNET=$(cat .ping_sweep_ip |cut -d "." -f 1,2,3)

for BIT in {1..254}
do
    ping -c 1 ${SUBNET}.${BIT}
    if [ $? == "0" ]
    then
        echo "[*] ${SUBNET}.${BIT} Is Reachable"
        sleep 0.3
    else
        echo "[!] ${SUBNET}.${BIT} Is Unreachable"
    fi
    echo
done

rm -rf .ping_sweep_ip

echo "[*] Done !!!"
