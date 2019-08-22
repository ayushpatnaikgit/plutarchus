import os
from insert import *
from activate import *
from pages import *
import json

def build_website(data):
    os.system("cp -r assets/themes/"+ data["settings"]["Theme"]+" template")
    names = data["settings"]["Pages"]
    home = "template/index.html"
    Author_image='"'+data["settings"]["Image"] +'"'
    insert_replace(home,Author_image,'"fakelink"')
    copy_between(home,'<!-- Page list start-->','<!-- Page list end-->',len(names)-1) 
    for x in names:
        page_link = "template/"+list(x.values())[0]+".html"
        os.system("cp template/left-sidebar.html "+page_link)
        insert_replace(home,page_link[9:],'"sameplepage.html"')
        insert_replace(home,list(x.keys())[0],'"samplepage"')
        insert_replace(page_link,list(x.keys())[0],'"sampletitle"')
        insert_replace(page_link,list(x.keys())[0],'"nameofauthor"')
        insert_elements(page_link,ordering(list(x.values())[0],data),'<!-- Content Generator -->')
        insert_replace(page_link,Author_image,'"fakelink"')

    insert_replace(home,data["settings"]["Name"],'"nameofauthor"')
    Author_details = ordering("Home",data)
    insert_elements(home,Author_details,'<!--About me -->')
    insert_replace(home,data["settings"]["Email"],'"example@gmail.com"')
    if data["settings"]["Support us"]=="YES":
        insert_file(home,"template/ad.html","<!--Footer -->")
    for x in names:
        activator(list(x.values())[0],data) #REACTIVE TITLE BAR 





    