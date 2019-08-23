import os
from insert import *
from activate import *
from pages import *
import json

def build_website(data):
    """
    This function will copy a theme, which mostly contains CSS, some javascript and html. Then it will insert data from the given JSON file into the HTML files.   
    """
    os.system("cp -r assets/themes/"+ data["basics"]["theme"]+" template")
    """
    Copying the theme mentioned in basics of the JSON file. Template will initially have empty HTML files into which data will be inserted. 
    """
    basics = data["basics"] #importing basics from the JSON file. 
    """
    For each page, we want a separate HTML file. We can't make 'page name'.html since it might contain spaces. There might be other problems too. Hence a dictionary is created with page suitable page names. in v0.1, the spaces are replaced with underscore'.
    """
    page_names,page_dict = basics["pages"], {}
    for x in page_names:page_dict[x] = x.replace(' ','_')
    
    home = "template/index.html" #defining home page. Since it's repeatedly used. 
    Author_image='"'+basics["image"] +'"' #link to author's image. 
    insert_replace(home,Author_image,'"author_image"')
    """
    There is a string "author_image", insert_replace will replace that string with link pointing at the author's image. 
    """
    copy_between(home,'<!-- Page list start-->','<!-- Page list end-->',len(page_names)-1) 
    """
    There standard way of making a list in the top bar in each of the themes. One element is made as sample. This element's name is samplepage and link is samplepage.html. For each page a duplicate of this item is made and then samplepage and samplepage.html are replaced with the pages actual name and link.   
    """
    for x in page_names:
        """
        For each page a separate HTML file is created. 
        """
        page_link = "template/"+page_dict[x]+".html" #this the html file name will look like. 
        os.system("cp template/left-sidebar.html "+page_link) 
        """
        There standard way of making a list in the top bar in each of the themes. One element is made as sample. This element's name is samplepage and link is samplepage.html. For each page a duplicate of this item is made and then samplepage and samplepage.html are replaced with the pages actual name and link. This is where the replacement is done.   
        """
        insert_replace(home,page_link[9:],'"sameplepage.html"')
        insert_replace(home,x,'"samplepage"')

        """
        page title, name of the authod and the author's image are inserted in the page. 
        """
        insert_replace(page_link,x,'"sampletitle"')
        insert_replace(page_link,x,'"nameofauthor"')
        insert_replace(page_link,Author_image,'"author_image"')
        """
        ordering() generates the content in the page by reading the entries. This is where all the content is put in the HTML file of the page. 
        """
        insert_elements(page_link,ordering(page_dict[x],data),'<!-- Content Generator -->')
        
    insert_replace(home,basics["name"],'"nameofauthor"')
    Author_details = ordering("Home",data)
    insert_elements(home,Author_details,'<!--About me -->')
    insert_replace(home,basics["email"],'"example@gmail.com"')
    if basics["support_us"]=="YES":
        insert_file(home,"template/ad.html","<!--Footer -->")
    for x in page_names:
        activator(page_dict[x],data) #REACTIVE TITLE BAR 





    