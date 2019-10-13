#! /bin/bash

echo
echo "##############################################"
echo "################# PING SWEEP #################"
echo "##############################################"
echo
echo " The Script takes only a Subnet-IP as argument"
echo " CIDR and VLSM are not suported. By Nzanoa !!!"
echo " eg. bash ping_sweep 192.168.4.0"
echo

# Create temp file
echo $1 > .ping_sweep_ip
# Use IP in temp file to extract Network part
SUBNET=$(cat .ping_sweep_ip |cut -d "." -f 1,2,3)

echo " Analyzing the ${SUBNET}.0/24 subdomain..."

# Start pinging
for BIT in {1..254}
do
    ping -c 1 ${SUBNET}.${BIT} 2>&1 > /dev/null
    if [ $? == "0" ]
    then
        echo "[*] ${SUBNET}.${BIT} Is Reachable"
        sleep 0.3
    fi
done

# Remove temporary file
rm -rf .ping_sweep_ip

echo "[*] Done !!!"
