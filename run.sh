#!/bin/zsh
docker build -t snmpsim .
docker run -p 1161:1161/udp -e EXTRA_FLAGS="--v3-user=testing --v3-auth-key=testing123" --name snmpsim snmpsim
