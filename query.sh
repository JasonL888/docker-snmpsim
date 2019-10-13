#!/bin/zsh
snmpwalk -v3 -l authNoPriv -u testing -a MD5 -A testing123 -n demo  127.0.0.1:1161 
