#!/bin/bash

# Exit script on any error
set -e

echo "🚀 Starting MongoDB and setting up the project..."



# Set up Python virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/Scripts/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the Flask app
echo "🚀 Starting Flask application..."
python run.py
