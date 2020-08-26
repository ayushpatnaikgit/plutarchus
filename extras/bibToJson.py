#from pybtex.database.input import bibtex

from pybtex.database import parse_file
import re
import json

from pybtex.database.input import bibtex
parser = bibtex.Parser()
bib_data = parser.parse_file('~/Downloads/website.bib')
list(bib_data.entries["krishnan2020_health"].fields)

def clean(x):
    x = x.replace("{","")
    x = x.replace("}","")
    x = x.replace("//","")
    return x

def HTMLentry(x):
    return '<br><h4>' + x + '</h4>'

def title(entry): 
    if 'Url' in list(entry.fields):
        title = "<a href='" + entry.fields["Url"]+"'>" +  clean(entry.fields["title"]) + "</a>"
        return title
    elif 'url' in list(entry.fields):
        title = "<a href='" + entry.fields["url"]+"'>" +  clean(entry.fields["title"]) + "</a>"
        return title
    elif 'link' in list(entry.fields):
        title = "<a href='" + entry.fields["link"]+"'>" +  clean(entry.fields["title"]) + "</a>"
        return title
    else:
        return HTMLentry(entry.fields["title"])

def authorEntry(entry):
    names = []
    for author in entry.persons["Author"]:
        try:
            names.append(clean(author.first_names[0] + " " + author.last_names[0]))#(author.first_names, author.last_names)
        except:
            names.append(clean(str(author)))
    if len(names) == 1:
        return HTMLentry(str(names[0]))
    else:
        author_entry = "<br><h4>Authors<h4> "
        for author in names:
            author_entry = author_entry + author + ", "
        author_entry = author_entry[:author_entry.rfind(",")]
        try: 
            author_entry = author_entry[:author_entry.rfind(",")] + ' and' + author_entry[author_entry.rfind(",")+1:]
        except:
            pass
        return author_entry

def authorEntryAND(entry):
    names = []
    for author in entry.persons["Author"]:
        names.append(author.first_names[0] + " " + author.last_names[0])#(author.first_names, author.last_names)
    
    if len(names) == 1:
        return HTMLentry(str(names[0]))
    else:
        author_entry = "<br><h4>Authors<h4> "
        for author in names:
            author_entry = author_entry + author + " and "
        author_entry = author_entry[:author_entry.rfind(" and")]
        return author_entry

def OtherFields(entry):
    JSONFields= ""
    for field in list(entry.fields):
        if field == "title": continue
        if field == "Url": continue
        if field == "url": continue
        if field == "link": continue

        JSONFields = JSONFields + HTMLentry(field) + " " + clean(entry.fields[field])
    return JSONFields 

def EntryDate(entry):
    DayMonYear = ""
    try:
        DayMonYear = DayMonYear + entry.fields["Day"] + " "
    except:
        try:
            DayMonYear = DayMonYear + entry.fields["day"] + " "
        except:
            pass


    try:
        DayMonYear = DayMonYear + entry.fields["Month"] + " "
    except:
        try:
            DayMonYear = DayMonYear + entry.fields["month"] + " "
        except:
            pass

    try:
        DayMonYear = DayMonYear + entry.fields["year"] + " "
    except:
        try:
            DayMonYear = DayMonYear + entry.fields["Year"] + " "
        except:
            pass
    if len(DayMonYear)>1:
        return DayMonYear[:-1]
    else:
        return DayMonYear

"""
Examples
bib_data = parser.parse_file('~/Downloads/website.bib')

authorEntry(bib_data.entries["pandey2019_motivation"])
title(bib_data.entries["pandey2019_motivation"])
OtherFields(bib_data.entries["pandey2019_motivation"])
EntryDate(bib_data.entries["pandey2019_motivation"])


authorEntry(bib_data.entries["Patnaik2014_democracyGrowth"])
title(bib_data.entries["Patnaik2014_democracyGrowth"])
OtherFields(bib_data.entries["Patnaik2014_democracyGrowth"])
EntryDate(bib_data.entries["Patnaik2014_democracyGrowth"])


authorEntry(bib_data.entries["krishnan2020_health"])
title(bib_data.entries["krishnan2020_health"])
OtherFields(bib_data.entries["krishnan2020_health"])
EntryDate(bib_data.entries["krishnan2020_health"])



"""
## This function converts the above created entries into the json format required.
## json format is used from ila.json file.



def entryToJson(entry,typ="Papers"):
    try:
        typ = entry.fields["Type"] 
    except:
        pass


    entry = {
            "page":"Papers",
            "date":EntryDate(entry),
            "section":typ,
            "entry": title(entry) + authorEntry(entry) + OtherFields(entry)
        }
#    result = json.dumps(entry)
    return entry

## Example
"""
entryToJson(title[1], typ[1], authors[1], year[1], institute[1], url[1])
"""


## Function to generate json file.
def bibToJson(inputfile,outputfile):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(inputfile)
    json_object=[]
    for entry in bib_data.entries:
        print(entry)
        data = entryToJson(bib_data.entries[entry])
        json_object.append(json.dumps(data, indent =4))
    with open(outputfile, 'w') as outfile:
        for i in range(0, len(json_object)):
            outfile.write(json_object[i])
            outfile.write(",")

bibToJson('working.bib', 'patnaik.json')

##---------------------------------------------------------------------------
