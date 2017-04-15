#!/bin/sh

USAGE="Usage: $0 function [args]"

function parseFile() {
    if [ "$1" = "" ] ; then
        echo "ERROR: /parseFile requires a URI parameter for source file"
        exit 1
    fi
    curl -X POST http://${serverip}:${serverport}/parseFile -d"{\"uri\": \"${1}\"}" | python3 -m json.tool
}

if [ "${serverip}" = "" ] ; then
    echo "Server IP is empty. Is the server running?"
    echo "If the server is running but you're seeing this error, run:"
    echo "export serverip=<ip>"
    exit 1
fi
if [ "${serverport}" = "" ] ; then
    echo "Server port is empty. Is the server running?"
    echo "If the server is running but you're seeing this error, run:"
    echo "export serverport=<port>"
    exit 1
fi

if [ "$1" = "" ] ; then
    echo "${USAGE}"
    exit 1
fi

case "$1" in
    "parseFile")
        parseFile $2
        ;;
    "help")
        echo "${USAGE}"
        exit 1
        ;;
    *)
        echo "Unrecognized function. Type '$0 help' for help. "
        exit 1
        ;;
esac


