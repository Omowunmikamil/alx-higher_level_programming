#!/bin/bash
#Sends a request to a URL passed as an argument, displays only the status code
curl -o /dev/null -sw "%{http_code}" "$1"
