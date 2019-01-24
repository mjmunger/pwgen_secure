#!/usr/bin/env bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

PWGENPATH=/usr/bin/pwgen
SPWGENPATH=$(pwd)/spwgen.py

while getopts ":p:" opt; do
  case $opt in
    p)
      SPWGENPATH=${OPTARG}
      echo "Path to spwgen is being set to: " ${SPWGENPATH} >&2
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

if [ -f ${PWGENPATH} ]; then
    update-alternatives --install /usr/local/bin/pwgen pwgen ${PWGENPATH} 20
fi

update-alternatives --install /usr/local/bin/pwgen pwgen ${SPWGENPATH} 10
update-alternatives --set pwgen ${SPWGENPATH}