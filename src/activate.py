from insert import *

def get_pages(file):
    fo = open(file, "r+")
    content = [x.strip() for x in fo] 
    content = content[content.index('<!-- Page list start-->')+1:content.index('<!-- Page list end-->')]
    fo.close()
    print(content)
    return content[:-1] #returns the list of pages 


def activator(file, data):
    label = '<!-- Page list start-->'
    for x in get_pages("template/index.html"):
        if file in x: 
            insert_elements("template/"+data["settings"]["Pages"][file] +'.html',[x],label)
            insert_replace("template/"+data["settings"]["Pages"][file] +'.html',"active",'"notactive"')
            continue
        insert_elements("template/"+data["settings"]["Pages"][file] +'.html',[x],label)
