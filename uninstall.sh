#!/usr/bin/env bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

update-alternatives --remove-all pwgen
update-alternatives --remove-all spwgen