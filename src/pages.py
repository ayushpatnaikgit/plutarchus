import datetime

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

def ordering(page,data): #This is the most important part of the code. Iterating through sections and subsecitons to add entries in proper order in HTML format
    pagedictionary = pageDict(page,data)
    #print(pagedictionary)
    html_page = []
    section_list = []
    for x in pagedictionary: 
        subsection_list = []
        if x["section"] not in section_list: 
            section_list.append(x["section"])
            html_page.append(section(x["section"]))
            for y in pagedictionary:
                if y["section"] == x["section"]:
                    if y["subsection"] not in subsection_list:
                        subsection_list.append(y["subsection"])
                        html_page.append(subsection(y["subsection"]))
                        entries = []
                        for z in pagedictionary: 
                            if z["section"] == x["section"] and z["subsection"] == y["subsection"]:
                                entries.append(entry(z["Entry"])) 
                        try: #try sorting if dates are there
                            entries = sorted(entries, key = lambda i:  datetime.datetime.strptime(i['Date'], '%d/%m/%Y'))[::-1]
                        except: 
                            pass
                        html_page = html_page + list(map(entry,entries))

    return html_page