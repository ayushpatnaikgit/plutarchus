#####
#The functions here are used to insert a list of elements in a file after a label. 
#####

def insert_elements(file,elements,label): #inserts elements in a file after a label
    fo = open(file, "r+")
    content = [line.strip() for line in fo] 
    new_content = content[0:content.index(label)+1]
    new_content = new_content + elements + content[content.index(label)+1:]
    new_content = [line + "\n" for line in new_content]
    fo.truncate(0)
    fo.writelines(new_content)
    fo.close()

def insert_file(file1,file2,label): #inserts elements of a file2 in file1 after a label. 
    fo = open(file2, "r")
    content = fo.readlines()
    insert_elements(file1,content,label)
    fo.close()

def insert_replace(file,url,label):
    fo = open(file, "r+")
    content = fo.read()
    content = content.replace(label,url,1)
    fo.truncate(0)
    fo.write(content)
    fo.close()
    
def copy_between(file,label1,label2,n):
    fo = open(file, "r+")
    content = [x.strip() for x in fo] 
    elements = content[content.index(label1)+1:content.index(label2)-1] * n
    insert_elements(file,elements,label1)
    fo.close()