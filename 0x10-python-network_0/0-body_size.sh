#!/bin/bash
response=$(curl -sI "$1")
content_length=$(echo "Content-Length: ${content_length} bytes" | grep -i "Content-Length" | awk '{print $2}')
