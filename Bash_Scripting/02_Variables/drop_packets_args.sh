#!/bin/bash

echo "Blocking connections from $1"
sleep 1

iptables -I INPUT -s $1 -j DROP

echo "$1 is now blocked..."

iptables -L INPUT -v -n 
echo

sleep 5

iptables -D INPUT -s $1 -j DROP

echo "$1 is now unblocked..."

iptables -L INPUT -v -n 
echo

echo "Done."