import os
from insert import *
from activate import *
from pages import *
import json

def build_website(data):
    os.system("cp -r assets/themes/"+ data["settings"]["theme"]+" template")
    settings = data["settings"]
    page_names = settings["pages"]
    page_dict = {}
    for x in page_names:page_dict[x] = x.replace(' ','_')
    home = "template/index.html"
    Author_image='"'+settings["image"] +'"'
    insert_replace(home,Author_image,'"fakelink"')
    copy_between(home,'<!-- Page list start-->','<!-- Page list end-->',len(page_names)-1) 
    for x in page_names:
        page_link = "template/"+page_dict[x]+".html"
        os.system("cp template/left-sidebar.html "+page_link)
        insert_replace(home,page_link[9:],'"sameplepage.html"')
        insert_replace(home,x,'"samplepage"')
        insert_replace(page_link,x,'"sampletitle"')
        insert_replace(page_link,x,'"nameofauthor"')
        insert_elements(page_link,ordering(page_dict[x],data),'<!-- Content Generator -->')
        insert_replace(page_link,Author_image,'"fakelink"')

    insert_replace(home,settings["name"],'"nameofauthor"')
    Author_details = ordering("Home",data)
    insert_elements(home,Author_details,'<!--About me -->')
    insert_replace(home,settings["email"],'"example@gmail.com"')
    if settings["support_us"]=="YES":
        insert_file(home,"template/ad.html","<!--Footer -->")
    for x in page_names:
        activator(page_dict[x],data) #REACTIVE TITLE BAR 





    