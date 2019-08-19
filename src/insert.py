#####
#The functions here are used to insert a list of elements in a file after a label. 
#####
def insert_elements(file,elements,label): #inserts elements in a file after a label
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

def insert_file(file1,file2,label): #inserts elements of a file2 in file1 after a label. 
    fo = open(file2, "r")
    content = [x.strip() for x in fo] 
    final = []
    for x in content:
        final.append(x + "\n")
    insert_elements(file1,final,label)
    fo.close()

def insert_replace(file,url,label):
    content = open(file, "r+").read()
    content = content.replace(label,url,1)
    with open(file, 'w+') as fp:
        fp.write(content)
    fp.close()

def copy_between(file,label1,label2,n):
    fo = open(file, "r+")
    content = [x.strip() for x in fo] 
    elements = content[content.index(label1)+1:content.index(label2)-1] * n
    insert_elements(file,elements,label1)
    fo.close()