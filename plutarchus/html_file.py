"""
These are general functions, not limited to the scope of this program. These are general file manipulation functions. 
"""
from plutarchus.pages import ordering

class File:
    def __init__(self,name,file_link):
        self.name = name
        self.tag = name.replace(' ','_')
        with open(file_link,'r') as fo: 
            self.content = fo.read().splitlines()
 
    def insert(self,elements,label): #inserts elements in a file after a label
        #Take a list of strings and puts it below a label in a file. 
        if type(elements)!=list: 
            elements = [elements]
        index = self.content.index(label)
        self.content = self.content[:index+1] + elements +  self.content[index+1:]

    def label_replace(self,old,new):
        #Replaces a label with another (generally a URL). The label must be in quotes.
        content_join = ''.join([line + "\n" for line in self.content])
        content_join = content_join.replace(old,new,1)
        self.content = content_join.splitlines()

    def copy_between(self,top,bottom,n):
        #Looks between 2 labels of a file and copies the content n times below the top label.   
        elements = self.content[self.content.index(top)+1:self.content.index(bottom)-1] * n
        self.insert(top,elements)
    
    def get_elements(self,top,bottom):
        return self.content[self.content.index(top)+1:self.content.index(bottom)]

    def render(self,file_link):
        with open(file_link,'w+') as fo: 
            fo.writelines([line + "\n" for line in self.content])


class html_file(File):
    def __init__(self,name,link):
        File.__init__(self,name,link)

    def make_navigator(self,pages):
    
        self.insert([self.get_elements('<!-- Page list start-->','<!-- Page list end-->')[0]] * (len(pages)-1),'<!-- Page list start-->')
        iterator = self.content.index('<!-- Page list start-->') + 1
        for page in pages:
            if page ==  self.name:
                self.content[iterator] = self.content[iterator].replace("notactive","active",1)
            self.content[iterator] = self.content[iterator].replace('"samplepage"',page,1)
            if page == "Home":
                self.content[iterator]= self.content[iterator].replace('"sameplepage.html"','index.html',1)
            else:
                self.content[iterator]= self.content[iterator].replace('"sameplepage.html"',page.replace(' ','_')+'.html',1) #needs to be looked into
            iterator += 1

    def author_image(self,image):
        self.label_replace('author_image',image)

    def author_name(self,name):
        self.label_replace('"nameofauthor"',name)

    def select_and_add_content(self,data,label="<!--Content-->"):
        self.insert(ordering(self.name,data),label)



class Home(html_file):
    def __init__(self):
        self.link = 'website/index.html'
        html_file.__init__(self,'Home',self.link)
        self.tag = 'index'

    def email(self,email): 
        self.label_replace('"example@gmail.com"',email)

    def write_html(self):
        self.render('website/index.html') #unix doesn't like spaces 

class SidePage(html_file):
    def __init__(self,name):
        self.link = 'website/left-sidebar.html'
        html_file.__init__(self,name,self.link)
        self.label_replace('"sampletitle"',self.name)
        
    
    def write_html(self):
        self.render('website/'+self.name.replace(' ','_')+".html") #unix doesn't like spaces 


