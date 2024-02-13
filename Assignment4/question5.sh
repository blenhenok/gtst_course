#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Usage: $0 <IP address> <NSE script name>"
    exit 1
fi

ip_address="$1"
nse_script="$2"

nmap -sV --script "$nse_script" "$ip_address"
