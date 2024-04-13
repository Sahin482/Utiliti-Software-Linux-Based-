import requests                         #HTTP Library For Python 
titles=[]                               #List to store news titles
description=[]                          #List to store news descriptions

#The JSON format is accessed using an News API URL in which the source and the apiKey will have to be specified. 
URL1="https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=73ba9519386543ea9c08351ddc2ec552"

r1 = requests.get(URL1)                             #GET request using python 'requests' library 
for i in r1.json()['articles']:                     #Running a for loop on r.json() to access contents of 'articles'
    titles.append(str(i['title']))                  #Storing all the news titles in 'titles' list
    description.append(str(i['description']))       #Storing all the news titles in 'description' list


dub_titles=[]
dub_description=[]
for i in range(0,3):
    dub_titles.append(str(titles[i]))
    dub_description.append(str(description[i]))

fo=open("info1.txt","w")
fo.write("\t\t\t\tWorld News\n\n")
fo.close()

fo=open("info1.txt","a")
for i in range(0,3):
    fo.write("Title: %s\n\n" % dub_titles[i])
    fo.write("Description: %s\n" % dub_description[i])
fo.close()

fo=open("info1.txt","a")
fo.write("\n\n")
fo.close()