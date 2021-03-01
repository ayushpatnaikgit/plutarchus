import pandas as pd
import json

database = pd.read_csv("data/logdata.csv")

## Let's see the columns
database.columns

## Let's filter unique authors
authors  = database.persons.unique()

## Let's filter unique categories
categories = database.category.unique()

## How many are there?
len(authors)

## Let's filter Ajay Shah's content
ajayShah = database.loc[database["persons"]=="Ajay Shah"]


## This function generates a json entry from the given inputs.
def entryToJson(pageTitle, date, url, title):
    entry = {
        "page":pageTitle,
        "date": date,
        "entry":"<br><h4> Title </h4><a href="+ url + ">"+ title+" </a>"
    }
    return entry

## Let's test this function

entryToJson(ajayShah.category.iloc[1], ajayShah.date.iloc[1], 
            ajayShah.url.iloc[1], ajayShah.description.iloc[1])



## This function generates the json file for the given author name.

def authorCsvToJson(authorName):
    ## Write the json entry into sample.json
    author = database.loc[database["persons"] == authorName]
    #author = author.sort_values(by=["date"])
    json_object=[]
    print(author)
    for i in range(0,len(author)):
        print(i)
        data = entryToJson(author.category.iloc[i], author.date.iloc[i], str(author.url.iloc[i]), author.description.iloc[i])
        json_object.append(json.dumps(data, indent =3))
        print(data)
        print("done")
    with open((authorName + ".json"), 'w') as outfile:
        print(authorName)
        for i in range(0, len(json_object)):
            outfile.write(json_object[i])
    

authorCsvToJson("Ajay Shah")

authorCsvToJson("Radhika Pandey")

## Generating everyone's json file.
for i in range(0, len(authors)):
    print(i)
    authorCsvToJson(authors[i])

## Another thought for fixing .json file with multiple names.
## Make a list of authors and then filter and so every entry gets in. 

# def authorCsvToJson2(authorName, outputFileName = 'sample.json'):
#     ## Write the json entry into sample.json
#     authorData = database.loc[database["persons"] == authorName]
#     categories = authorData.category.unique()
#     json_object=[]
#     for k in range(0, len(categories)):
#         author = authorData.loc[authorData["category"] == categories[k]]    
#         for i in range(0,len(author)):
#             print(i)
#             data = entryToJson(author.category.iloc[i], author.date.iloc[i], str(author.url.iloc[i]), author.description.iloc[i])
#             json_object.append(json.dumps(data, indent =3))
#             print(data)
#             print("done")
#         with open(outputFileName, 'w') as outfile:
#             for i in range(0, len(json_object)):
#                 outfile.write(json_object[i])




