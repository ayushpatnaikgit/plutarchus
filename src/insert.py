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

def insert_file(file1,file2,label): 
    fo = open(file2, "r")
    content = [x.strip() for x in fo] #no need to strip back slash from the end
    final = []
    for x in content:
        final.append(x + "\n")
    insert_elements(file1,final,label)
