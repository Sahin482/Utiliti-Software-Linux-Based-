#!/bin/bash
python news_tool.py 					#Runs news_tool.py
python news_tool1.py         			#Runs news_tool1.py
python news_tool2.py 					#Runs news_tool2.py

FILE=`dirname $0`/info1.txt

zenity --text-info \
       --title="Today News" \
       --filename=$FILE \
       --width=600 --height=400

echo "World News"
for (( i=0; i<3; i++ ))					#Running the for loop to extract the data of World new for array 'arr'
do
    echo "${arr[i]}"
    echo "${arr[i+3]}"
    echo
done
echo
echo

echo "Technology"						#Running the for loop to extract the data of Technology news for array 'arr'
for (( i=6; i<9; i++ ))
do
    echo "${arr[i]}"
    echo "${arr[i+3]}"
    echo
done
echo
echo

echo "Sports"							#Running the for loop to extract the data of Sports news for array 'arr'
for (( i=12; i<15; i++ ))
do
    echo "${arr[i]}"
    echo "${arr[i+3]}"
    echo
done


