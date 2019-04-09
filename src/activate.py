from insert import *
def get_pages():
    fo = open("template/index.html", "r+")
    content = [x.strip() for x in fo] 
    content = content[content.index('<!-- Make a generator for above list -->')+1:content.index('<!-- End of generator -->')]
    fo.close()
    return content[:-1]

def activator(file):
    label = '<!-- Make a generator for above list -->'
    fo = open("template/"+file+".html", "r+")

    elements = []
    pages = get_pages()
    for x in pages: 
        if file in x: 
            elements.append('<li class="active"><a href="'+file+'.html"><span>' +file+ '<span class="border"></span></span></a></li>')
            continue
        elements.append(x)
    fo.close()
    insert_elements("template/"+file +'.html',elements,label)