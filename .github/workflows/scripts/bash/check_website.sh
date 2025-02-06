#!/bin/bash

# Ask the user for a website to check
read -p "Enter the website URL (e.g., google.com): " website

# Ping the website and check if it's reachable
ping -c 3 $website > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✅ $website is online!"
else
    echo "❌ $website is down!"
fi

