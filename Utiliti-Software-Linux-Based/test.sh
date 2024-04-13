#!/bin/sh

# You must place file "COPYING" in same folder of this script.
FILE=`dirname $0`/info1.txt

zenity --text-info \
       --title="News" \
       --filename=$FILE \

case $? in
    0)
        echo "Start installation!"
	# next step
	;;
    1)
        echo "Stop installation!"
	;;
    -1)
        echo "An unexpected error has occurred."
	;;
esac