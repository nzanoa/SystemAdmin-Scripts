#! /usr/bin/bash
# Create a tmp file of all ports
cat $1 |grep ^[0-9] |awk -F/ '{print $1}' |sort -u > ports.tmp
# Put all ports found in a list
for i in $(cat ports.tmp);
  do echo -n $i, > list.tmp;
  cat list.tmp
done
# Clean up
rm -rf ports.tmp
rm -rf list.tmp
