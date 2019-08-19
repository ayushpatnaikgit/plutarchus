from insert import *

def get_pages(file):
    fo = open(file, "r+")
    content = [x.strip() for x in fo] 
    content = content[content.index('<!-- Page list start-->')+1:content.index('<!-- Page list end-->')]
    fo.close()
    return content[:-1] #returns the list of pages 


def activator(file, data):
    file_url = file+'.html'
    label = '<!-- Page list start-->'
    for x in get_pages("template/index.html")[::-1]: ##The insertion needs to be reversed since elements are put below label, hence reversing the order. We want to keep current item on top. 
        if file in x:             
            insert_elements("template/"+file_url,[x],label)
            insert_replace("template/"+file_url,"active",'"notactive"') ##current one is always on top. 
            continue
        insert_elements("template/"+file_url,[x],label)

