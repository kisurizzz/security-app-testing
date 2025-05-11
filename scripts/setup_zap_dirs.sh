#!/bin/bash

# Create necessary directories
echo "Creating ZAP directories..."

# Create .zap directory if it doesn't exist
mkdir -p .zap
chmod 755 .zap

# Create zap-reports directory if it doesn't exist
mkdir -p zap-reports
chmod 777 zap-reports

# Create a default rules file if it doesn't exist
if [ ! -f .zap/rules.tsv ]; then
    echo "Creating default rules.tsv file..."
    echo "# Rule ID	Level	URL" > .zap/rules.tsv
    echo "10016	IGNORE	.*" >> .zap/rules.tsv
    echo "10020	IGNORE	.*" >> .zap/rules.tsv
    chmod 644 .zap/rules.tsv
fi

# Verify directories exist and have correct permissions
echo "Verifying directory structure..."
echo "Directory structure:"
tree -a -L 2 .

echo -e "\nDirectory permissions:"
ls -la .zap/
ls -la zap-reports/

echo -e "\nChecking if rules file exists and is readable:"
if [ -f .zap/rules.tsv ]; then
    echo "rules.tsv exists and is readable"
    cat .zap/rules.tsv
else
    echo "ERROR: rules.tsv does not exist!"
    exit 1
fi 