#!/bin/bash

FILE=`dirname $0`/info.txt

zenity --text-info \
       --title="Today Weather" \
       --filename=$FILE \                                                                        #