#!/bin/bash

# Set env variables for URL and CONNECTOR_PATH, e.g.
# export URL=http://localhost:8083
# export CONNECTOR_PATH=./configs/cdc

CYAN="\033[1;36m"
RESET="\033[0m"
NOTICE_FLAG="${CYAN}❯"

# Get list of all connectors in kafka connect
echo -e "${NOTICE_FLAG} List connectors ${RESET}"
echo $(curl -s -X GET $URL/connectors)

# Iterating through all connectors config file from local to kafka connect
echo -e "${NOTICE_FLAG} Begin upserting connectors ${RESET}"
for FILENAME in "$CONNECTOR_PATH"/*.json; do
    CONNECTOR=${FILENAME##*/}
    echo -e "${CYAN}$CONNECTOR${RESET}"
    curl -i -X PUT -H "Accept:application/json" -H "Content-Type:application/json" "$URL/connectors/${CONNECTOR%.*}/config" -d "@$FILENAME"
    echo
done

echo -e "${NOTICE_FLAG} Finished.${RESET}"
