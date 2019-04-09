def insert_elements(file,elements,label):
    fo = open(file, "r+")
    content = [x.strip() for x in fo] 
    new_content = content[0:content.index(label)+1]
    new_content = new_content + elements + content[content.index(label)+1:]
    final = []
    for x in new_content:
        final.append(x + "\n")
    fo.close()
    with open(file, 'w+') as fp:
        fp.writelines(final)