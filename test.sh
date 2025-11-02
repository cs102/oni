#!/bin/bash
clear
echo 'Today is:'
cal
date

if [ ! -f ~/snarf ]; then
	echo "You have no snarf file"
	echo "Create one? [y/N]"
	read -n 1 -s choice
		if [ "$choice" == "y" ]; then
			touch ~/snarf
		fi
	else
		echo "Found file in use $USER home directory"
fi

echo "Good day!"

exit
