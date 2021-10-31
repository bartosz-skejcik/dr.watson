#!/bin/bash
# Script for update Fsociety tools

git clone --depth=1 https://github.com/bartosz-skejcik/dr.watson.git
sudo chmod +x dr.watson/install.sh
bash dr.watson/install.sh