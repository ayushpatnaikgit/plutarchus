import json
with open('saner.json') as json_file:  
    data = json.load(json_file) 

def pageDict(page,data):
    data2 = []
    for x in data["Entries"]:
        if x["PageTag"] == page:
            data2.append(x)
    return data2

def section(H1):
    return "<h1>" + H1+ "</h1>"

def subsection(H2):
    return "<h2>" + H2+ "</h2>"

def entry(ENTRY):
    return "<p>" + ENTRY + "</p>" 

def ordering(page,data):
    pagedictionary = pageDict(page,data)
    sections = []
    for x in pagedictionary: 
        if "section" in list(x.keys()):
            sections.append(x["section"])
    sections = list(set(sections))
    subsections = {}
    if len(sections) != 0:
        for y in sections:
            subsections[y] = []
        for x in pagedictionary:
            if "section" and "subsection" in list(x.keys()):
                subsections[x["section"]].append(x["subsection"])
        subsections_list  = []
        for x in pagedictionary: 
            if "subsection" in list(x.keys()):
                subsections_list.append(x["subsection"])

        if subsections_list != 0:
            html_page = subsections
        else: 
            home_page = {}
            for y in sections:
                home_page[y] = []
    
            for x in pagedictionary:
                if "section" in pagedictionary:
                    home_page[x["section"]].append(x["Entry"])
    
    else: 
        subsections_list  = []
        for x in pagedictionary: 
            if "subsection" in list(x.keys()):
                subsections_list.append(x["subsection"])
            subsections_list = list(set(subsections_list))
        if len(subsections_list) != 0:
            for y in subsections_list:
                subsections[y] = []
            for x in pagedictionary: 
                if "subsection" in list(x.keys()):
                    subsections[x["subsection"]].append(x["Entry"])
            html_page = subsections
        else:
            html_page["Entries"] = []
            for x in pagedictionary:
                html_page["Entries"].append(x["Entries"])
    return html_page
             
