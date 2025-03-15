#!/bin/bash

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Installing Node.js dependencies..."
cd Zero-Tool/nuke-bot || exit
npm install

cd ../..

echo "Installation complete. Run ./start.sh to start the tool."
