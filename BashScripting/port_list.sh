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

# Header
echo -e ${YELLOW}
echo " #############################################"
echo " ############## OPEN PORTS LIST ##############"
echo " #############################################"
echo
echo -e " The Script takes only a IP as argument"
echo -e " List of all open ports. By Nzanoa !!!" ${NC}
echo -e " eg. ${LPURPLE}bash port_list.sh 192.168.4.2"
echo -e  ${NC}

# If No argument
if [ ! $1 ]
then
	echo -e " ${RED}You forgot the argument buddy"
	echo -e " There is an example in the header" ${NC}
	set -e
else
	# Nmap port
	echo -e " [+] ${BLUE} Using Nmap to discover open ports" ${NC}
	nmap -T5 -p- $1 > result.tmp

	# Create a tmp file of all ports
	cat result.tmp |grep ^[0-9] |awk -F/ '{print $1}' |sort -u > ports.tmp

	# Put all ports found in a list
	echo -n -e " [+] ${BLUE} Open port on $1:${GREEN}"
	for i in $(cat ports.tmp);
	  do echo -n " $i," > list.tmp;
	  cat list.tmp
	done

	# Clean up
	rm -rf ports.tmp
	rm -rf list.tmp
	rm -rf result.tmp
fi

# End of script
echo
echo -e " ${YELLOW}Done !!!" ${NC}
echo

