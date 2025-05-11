#!/bin/bash

# Check if ngrok is installed
if ! command -v ngrok &> /dev/null; then
    echo "Installing ngrok..."
    curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
    echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
    sudo apt update && sudo apt install ngrok
fi

# Check if NGROK_AUTH_TOKEN is set
if [ -z "$NGROK_AUTH_TOKEN" ]; then
    echo "Error: NGROK_AUTH_TOKEN environment variable is not set"
    echo "Please set it with your ngrok authentication token"
    echo "You can get your token from https://dashboard.ngrok.com/get-started/your-authtoken"
    exit 1
fi

# Configure ngrok with auth token
ngrok config add-authtoken "$NGROK_AUTH_TOKEN"

# Start ngrok tunnel to SonarQube
echo "Starting ngrok tunnel to SonarQube..."
ngrok http 9000 --log=stdout > ngrok.log 2>&1 &

# Wait for ngrok to start
sleep 5

# Get the public URL
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')

if [ -z "$NGROK_URL" ] || [ "$NGROK_URL" == "null" ]; then
    echo "Error: Failed to get ngrok URL"
    cat ngrok.log
    exit 1
fi

echo "SonarQube is now accessible at: $NGROK_URL"
echo "Please update your GitHub repository secret SONAR_HOST_URL with this URL"
echo "Current ngrok tunnel status:"
curl -s http://localhost:4040/api/tunnels | jq '.'

# Keep the script running
echo "Press Ctrl+C to stop the tunnel"
tail -f ngrok.log 