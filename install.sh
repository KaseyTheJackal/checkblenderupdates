#!/bin/bash
pip3 install requests beautifulsoup4
[[ $USER != "root" ]]; then echo "This part of the script must be run as root." else
cp checkblenderupdates.plist ~/Library/LaunchDaemons/checkblenderupdates.plist
launchctl enable checkblenderupdates.plist
