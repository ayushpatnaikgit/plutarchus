"""
These functions are highly specific to this module.
"""
from insert import *

def get_pages(file,top,bottom):
    """
    Returns the content of a file between two labels i.e. top and bottom.
    """
    fo = open(file, "r")
    content = [x.strip() for x in fo] 
    content = content[content.index(top)+1:content.index(bottom)]
    fo.close()
    return content[:-1] #returns the list of pages 


def activator(file, data):
    """
    Gets the list of pages from index.html using get pages. Puts it 'file'.
    However, it changes the class from nonactive to active
    """
    file_url = file+'.html'
    label = '<!-- Page list start-->'
    for x in get_pages("template/index.html",label,'<!-- Page list end-->')[::-1]: ##The insertion needs to be reversed since elements are put below label, hence reversing the order. We want to keep current item on top. 
        if file in x:             
            insert_elements("template/"+file_url,[x],label)
            insert_replace("template/"+file_url,"active",'"notactive"') ##current one is always on top. 
            continue
        insert_elements("template/"+file_url,[x],label)

