#!/bin/bash
# Colors
NC='\033[0m'
RED='\033[1;31m'
GREEN='\033[0;32m'
BLUE="\033[0;34m"
YELLOW="\033[1;33m"
LPURPLE='\033[1;35m'

# Catch C^
trap ctrl_c INT
function ctrl_c() {
        echo -e " ${RED}:( Ending this Script..." ${NC}
	kill -n 9 $BASHPID 2>&1 > /dev/null
}

echo -e ${YELLOW}
echo " #############################################"
echo " ################# PING SWEEP ################"
echo " #############################################"
echo
echo -e " The Script takes only a Subnet-IP as argument"
echo -e " CIDR and VLSM are not suported. By Nzanoa !!!" ${NC}
echo -e " eg. ${LPURPLE}bash ping_sweep.sh 192.168.4.0"
echo -e  ${NC}


if [ ! $1 ]
then
	# If No argument
	echo -e " ${RED}You forgot the argument buddy"
	echo -e " There is an example in the header" ${NC}
	set -e
else
	# Create temp file
	echo $1 > .ping_sweep_ip
	# Use IP in temp file to extract Network part
	SUBNET=$(cat .ping_sweep_ip |cut -d "." -f 1,2,3)

	echo -e " ${BLUE}Looking for available hosts in ${SUBNET}.0/24..." ${NC}

	# Start pinging
	for BIT in {1..254}
	do
	    ping -c 1 ${SUBNET}.${BIT} 2>&1 > /dev/null
	    if [ $? == "0" ]
	    then
		echo -e " [*]  ${GREEN}Host ${SUBNET}.${BIT} Is Alive " ${NC}
		# sleep 0.3
	    fi
	done

	# Clean up
	rm -rf .ping_sweep_ip
fi

# End of script
echo
echo -e " ${YELLOW}Done !!!" ${NC}
echo
