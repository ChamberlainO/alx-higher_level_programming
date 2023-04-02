#!/bin/bash
# a script to check the size of the body of the response
curl -sI "$1" | grep Content-Length | tail -c 4
