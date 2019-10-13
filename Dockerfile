FROM python:3.6-slim
RUN pip install snmpsim
RUN adduser --system snmpsim
ADD ./data /usr/local/snmpsim/data
EXPOSE 1161/udp
USER snmpsim
CMD snmpsimd.py --agent-udpv4-endpoint=0.0.0.0:1161 --process-user=snmpsim --process-group=nogroup $EXTRA_FLAGS
