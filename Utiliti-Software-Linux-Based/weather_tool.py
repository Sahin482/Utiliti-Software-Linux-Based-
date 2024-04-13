import requests             #HTTP Library For Python 
import sys                  #Library that enables command line input
CITY_NAME=sys.argv[1]       #Variable 'CITY_NAME' for storing the command line input

#The JSON format is accessed using an openweather URL in which the city name and the app id will have to be specified.            
URL="http://api.openweathermap.org/data/2.5/weather?q="+CITY_NAME+"&mode=json&units=metric&cnt=7&appid=85d97b3a5c555f0d8f3a9b3a21f36059"
#In the above URL,'CITY_NAME' is the name of the city and 'appid' is the registered key which is available when you have a OpenWeatherMap registered account.
r = requests.get(URL)                                                   #GET request using python 'requests' library 
# print("Print details:",r.json())

temp_min = r.json()['main']['temp_min']
fo=open("info.txt","w")                                                 #Writing down all the values in a file 'info.txt' which were stored in the respective lists
fo.write("%s today temperature" % CITY_NAME )
fo.close()                #Closing the file
fo=open("info.txt","a")                                                 #Writing down all the values in a file 'info.txt' which were stored in the respective lists
fo.write("\n\nMinimum Temperature: %s\n" % temp_min)
fo.close()                #Closing the file
temp_max = r.json()['main']['temp_max']
fo=open("info.txt","a")                                                 #Writing down all the values in a file 'info.txt' which were stored in the respective lists
fo.write("\nMaximum Temperature: %s\n" % temp_max)
fo.close()                                                              #Closing the file

description = r.json()['weather'][0]['description']
fo=open("info.txt","a")                                                 #Writing down all the values in a file 'info.txt' which were stored in the respective lists
fo.write("\nTemperature description: %s\n" % description)
fo.close()                                                              #Closing the file