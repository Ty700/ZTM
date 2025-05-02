#!/bin/bash
read -p "Enter IP, Network, or Domain to drop: " drop

echo "Blocking connections from $drop"
sleep 1

iptables -I INPUT -s $drop -j DROP

echo "$drop is now blocked..."

iptables -L INPUT -v -n 
echo

sleep 5

iptables -D INPUT -s $drop -j DROP

echo "$drop is now unblocked..."

iptables -L INPUT -v -n 
echo

echo "Done."