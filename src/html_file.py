"""
These are general functions, not limited to the scope of this program. These are general file manipulation functions. 
"""
from pages import ordering

class File:
    def __init__(self,name,file_link):
        self.name = name
        self.tag = name.replace(' ','_')#unix doesn't like spaces 
        with open(file_link,'r') as fo: 
            self.content = fo.read().splitlines()
 
    def insert(self,elements,label): #inserts elements in a file after a label
        #Take a list of strings and puts it below a label in a file.  
        self.content.insert(self.content.index(label),elements)

    def replace(self,url,label):
        #Replaces a label with another (generally a URL). The label must be in quotes.
        self.content_join = ''.join([line + "\n" for line in self.content])
        self.content_join = line.replace(label,url,1)
        self.content = self.content_join.splitlines()

    def copy_between(self,top,bottom,n):
        #Looks between 2 labels of a file and copies the content n times below the top label.   
        elements = self.content[self.content.index(top)+1:self.content.index(bottom)-1] * n
        self.insert(top,elements)
    
    def get_elements(self,top,bottom):
        return self.content[self.content.index(top)+1:self.content.index(bottom)]

    def render(self,file_link):
        self.new_content = [line + "\n" for line in self.content]
        with open(file_link,'w+') as fo: 
            self.content = fo.writelines(self.new_content)


class html_file(File):
    def __init__(self):
        file_plus_plus.__init__(self)

    def make_navigator(self,pages):
        for page in page_names:
            page_link = page.replace(' ','_') + '.html'
            sample_item_on_navbar = get_elements('<!-- Page list start-->','<!-- Page list end-->') 
            if page ==  self.name: 
                sample_item_on_navbar.replace("active",'"notactive"')
            item_on_navbar= sample_item_on_navbar.replace(page_link,'"sameplepage.html"') #needs to be looked into
            item_on_navbar.replace(page,'"samplepage"')
            self.insert(item_on_navbar)

    def author_image(self,image)
        self.replace(image,'author_image')

    def author_name(self,name):
        self.replace('"nameofauthor"')

    def add_content(self,data,label):
        self.insert(ordering(self.name,data))

    def write_html(self):
        render(self,'template/'+self.tag)

class Home(html_file):
    def __init__(self,theme):
        self.link = 'template/index.html'
        html_file.__init__(self,'Home',self.link)
    def email(self,email): 
        self.replace(email,'"example@gmail.com"')

class SidePage(html_file):
    def __init__(self,theme,name):
        self.link = 'template/left_sidebar.html'
        html_file.__init__(self,name,self.link)
        self.replace(self.name,'"sampletitle"')
    





