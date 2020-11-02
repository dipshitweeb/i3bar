#!/bin/sh

echo '{ "version" : 1 }'
echo "["
while :;
do
	TEMP=$(cat ~/.config/i3/temp_file)
	echo "[{\"name\":\"time\",\"full_text\":\"$(date) | $TEMP\"}],"
	sleep 1
done
