import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import pandas as pd
import json


## This function returns the total number of pages assigned to a particular author on The Indian Express webpage.
## For example - Bhanu Pratap Singh has 23 pages. 
def totalPages(url):
    html      = urlopen(url)
    soup      = BeautifulSoup(html, "lxml")
    totalPage = []
    for number in soup.find_all('a', { "class" : "page-numbers"}):
        totalPage.append(number.get_text())
    if not totalPage:
        pages = 1
    else:
        pages     = int(totalPage[-2])
    return pages

## Generates the url for different pages of a columnist. For example - Bhanu Pratap Singh has 23 pages on The Indian Express.
## This function generates the url for each page.
def currentUrl(url, pageNo):
    link    = url
    newLink = url + '/' + str(pageNo) + '/'
    return newLink

## Generates a dataframe containing title and link of each article published of a given columnist.
def scrapeArticleTitles(url):
    print(url)
    originalLink = url
    pages        = totalPages(url)
    ref          = []
    title        = []
    date         = []
    for i in range(1,(pages +1)):
        url = currentUrl(originalLink, i) ##Generating current url
        print(url)
        print(i)
        html = urlopen(url)
        soup = BeautifulSoup(html, "lxml")
        for link in soup.find_all('div', { "class" : "col-stories"}):
            ref.append(link.find('a').get('href'))
            title.append(link.find('a').get_text('href'))
            date.append(link.find('div', {"class": "date"}).get_text())
    df = pd.DataFrame(list(zip(title, ref, date)), columns=['title', 'url', 'date'])
    return df
    #    df.to_csv("titleScraper.csv")



## Generates the list of columnists (with their respective Indian express url) in The Indian Express.
def listAuthorsAndLink(url):
    authorLink = []
    authorname = []
    url        = url
    html       = urlopen(url)
    soup       = BeautifulSoup(html, "lxml")
    for div in soup.find_all('div', { "id" : ['A', 'E', 'I', 'M', 'Q', 'U']}):
        for link in div.find_all('a', { "class" : ""}):
            authorLink.append(link.get('href'))
            authorname.append(link.get_text())
    df = pd.DataFrame(list(zip(authorname, authorLink)), columns=['authorName', 'url'])
    return df
        

#cRajaMohan       = scrapeArticleTitles("http://indianexpress.com/profile/columnist/c-raja-mohan")
#pratapBhanuMehta = scrapeArticleTitles("https://indianexpress.com/profile/columnist/pratap-bhanu-mehta")
#pratapBhanuMehta.to_csv("bhanuPratap.csv")

## This function converts the above created entries into the json format required.
## json format is used from ila.json file.
def entryToJson(title, author, url, date):
    entry = {
            "page":"Articles",
            "date":date,
            #"section":typ,
            "entry":"<br><h4> Title </h4><a href="+ url + ">"+ title+" </a> <br><h4>Authors</h4>" + author +"<br><h4>Year</h4>" + date #+ " <br><h4> Institution </h4>" + institute
        }
    return entry

authors = listAuthorsAndLink("http://indianexpress.com/columnists")
    

def authorArticlesToJson(authorNo = 0, outputFileName = 'sample.json'):
    authors = listAuthorsAndLink("http://indianexpress.com/columnists")
    authorNo = authorNo ## Author at 0th position in "authors"
    author = scrapeArticleTitles(str(authors.iloc[authorNo][1])) 
    ## Write the json entry into sample.json
    json_object=[]
    print(author)
    for i in range(0,len(author)):
        print(i)
        data = entryToJson(author.iloc[i][0], authors.iloc[authorNo][0], author.iloc[i][1], author.iloc[i][2])
        print(data)
        json_object.append(json.dumps(data, indent =3))
        print(json_object)
    with open(outputFileName, 'w') as outfile:
        for i in range(0, len(json_object)):
            outfile.write(json_object[i])


authorArticlesToJson(2, "test.json")