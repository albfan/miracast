#!/bin/bash

dev=""

while [ "$dev" = "" ]
do
   sleep 0.01
   dev=$( iw dev | sed -n 's/Interface \(p2p-wlp4s0-.*\)/\1/p')
done

echo $dev
sleep 0.1
ip link set dev $dev up
tcpdump -c 10000 -w /tmp/dump -i $dev  &

./miracle-dhcp.py $dev
