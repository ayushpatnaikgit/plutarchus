"""
These are general functions, not limited to the scope of this program. These are general file manipulation functions. 
"""

def insert_elements(file,elements,label): #inserts elements in a file after a label
    """
    Take a list of strings and puts it below a label in a file.  
    """
    fo = open(file, "r+")
    content = [line.strip() for line in fo] 
    new_content = content[0:content.index(label)+1]
    new_content = new_content + elements + content[content.index(label)+1:]
    new_content = [line + "\n" for line in new_content]
    fo.truncate(0)
    fo.writelines(new_content)
    fo.close()

def insert_file(parent_file,child_file,label): #inserts elements of a file2 in file1 after a label. 
    """
    Takes the contents of a file (child_file) and puts it below a label which is inside the parent file. 
    """
    fo = open(child_file, "r")
    content = fo.readlines()
    insert_elements(parent_file,content,label)
    fo.close()

def insert_replace(file,url,label):
    """
    Replaces a label with another (generally a URL). The label must be in quotes.
    """
    fo = open(file, "r+")
    content = fo.read()
    content = content.replace(label,url,1)
    fo.truncate(0)
    fo.write(content)
    fo.close()

def copy_between(file,top,bottom,n):
    """
    Looks between 2 labels of a file and copies the content n times below the top label.   
    """
    fo = open(file, "r+")
    content = [x.strip() for x in fo] 
    elements = content[content.index(top)+1:content.index(bottom)-1] * n
    insert_elements(file,elements,top)
    fo.close()