import datetime

def pageDict(page,data):
    data2 = []
    for x in data["entries"]:
        if x["page"] == page:
            data2.append(x)
    return data2

def section(H2):
    return "<h2>" + H2+ "</h2>"

def subsection(B):
    return "<b>" + B+ "</b>"

def entry(ENTRY):
    return "<p>" + ENTRY + "</p>" 

def check_empty(dict,key):
    try:
        value = dict[key]
    except:
        value = ""
    return value 

def ordering(page,data): #This is the most important part of the code. Iterating through sections and subsecitons to add entries in proper order in HTML format
    pagedictionary = pageDict(page,data)
    html_page = []
    section_list = []
    for x in pagedictionary: 
        subsection_list = []
        if check_empty(x,"section") not in section_list: 
            section_list.append(check_empty(x,"section"))
            html_page.append(section(check_empty(x,"section")))
            for y in pagedictionary:
                if check_empty(y,"section") == check_empty(x,"section"):
                    if check_empty(y,"subsection") not in subsection_list:
                        subsection_list.append(check_empty(y,"subsection"))
                        html_page.append(subsection(check_empty(y,"subsection")))
                        entries = []
                        for z in pagedictionary: 
                            if check_empty(z,"section") == check_empty(x,"section") and check_empty(z,"subsection") == check_empty(y,"subsection"):
                                entries.append(entry(z["entry"])) 
                        try: #try sorting if dates are there
                            entries = sorted(entries, key = lambda i:  datetime.datetime.strptime(i['date'], '%d/%m/%Y'))[::-1]
                        except: 
                            pass
                        html_page = html_page + list(map(entry,entries))

    return html_page