# SNMP Simulator

This docker image starts up snmpsim.

# Prequisite
* Install Docker for local machine

# How to use
* To run
```
./run.sh  
```
  > docker build image snmpsim

  > docker run as a container snmpsim

  > by default loaded snmpwalk from `demo.snmplabs.com` under community name `demo`

* To snmp query
```
./query.sh
```

* To access bash shell inside docker container
```
docker exec -it snmpsim bash
```

* To stop container
```
./stop.sh
```

## Misc
* To add new simulation data
  * perform snmpwalk
  * use datafile.py to convert to .snmprec format
    * refer to [snmpsim Managing data](http://snmplabs.com/snmpsim/managing-simulation-data.html)
  * copy converted .snmprec file to /usr/local/snmpsim/data

* Fixing hex-STRING overflow issue
 * snmpsim converter, datafile.py, cannot handle hex-STRING that overflows (as shown below)

```
1.3.6.1.2.1.1.9.1.2.28 = OID: 1.3.6.1.6.3.15
1.3.6.1.2.1.1.9.1.3.1 = STRING: "The MIB module to describe network interfaces (regardless of their current state) present on this system"
1.3.6.1.4.1.4491.2.1.20.1.4.1.6.358.5000022 = Hex-STRING: 08 01 18 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00
```

 * use the utils script to concat all the Hex-STRING into single line (before using datafile.py)

 ```
 python fix_hexstring.py test_snmpwalk_input.txt test_snmpwalk_output.txt
 ```

 # License
 License under [MIT](LICENSE)

 # Acknowledgement
 * Thanks to original authors of https://github.com/tandrup/docker-snmpsim
 * Developers of [snmpsim](http://snmplabs.com/snmpsim/)
 * Authors of [IBM support page](https://www.ibm.com/support/pages/how-use-snmpsim-simulate-network-device-based-snmp-walk-file)
