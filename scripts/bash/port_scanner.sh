# This is a port scanner.

#!/bin/bash

# Ask the user for a target IP or domain
read -p "Enter target IP or domain: " target

# Define ports to scan
ports=(22 80 443 3389 445)

echo "Scanning $target for open ports..."

# Loop through each port and check if it's open
for port in "${ports[@]}"; do
    timeout 1 bash -c "echo > /dev/tcp/$target/$port" 2>/dev/null && \
    echo "✅ Port $port is open" || \
    echo "❌ Port $port is closed"
done

echo "Scan completed."

