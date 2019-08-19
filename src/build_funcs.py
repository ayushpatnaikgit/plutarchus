import os
from insert import *
from activate import *
from pages import *
import json
import sys

def build_website(data_file):
    os.system("cp -r assets/themes/"+ data_file["settings"]["Theme"]+" template")
    data = data_file
    names = list(data["settings"]["Pages"].keys())
    home = "template/index.html"
#generating the navigation bar and creating the files
    elements = []
    copy_between(home,'<!-- Page list start-->','<!-- Page list end-->',len(names)-1) 
    for x in names:
        page_link = "template/"+data["settings"]["Pages"][x]+".html"
        page_name = data["settings"]["Pages"][x]+".html"
        os.system("cp template/left-sidebar.html "+page_link)
        insert_replace(home,page_name,'"sameplepage.html"')
        insert_replace(home,x,'"samplepage"')
        print(x)
        insert_replace(page_link,x,'"sampletitle"')
        insert_replace(page_link,data["settings"]["Name"],'"nameofauthor"')
        insert_elements(page_link,ordering(data["settings"]["Pages"][x],data),'<!-- Content Generator -->')

    insert_elements(home,elements,'<!-- Page list start-->')
    insert_replace(home,data["settings"]["Name"],'"nameofauthor"')

    Author_details = ordering("Home",data)
    Author_details_new = []
    for x in Author_details:
        x = x.replace("h2","b")
        x = x.replace("h1","h2")
        Author_details_new.append(x)

    insert_elements(home,Author_details_new,'<!--About me -->')
    insert_replace(home,data["settings"]["Email"],'"example@gmail.com"')

    Author_image='"'+data["settings"]["Image"] +'"'
    insert_replace(home,Author_image,'"fakelink"')
    ## Footer

    #if data["settings"][""]

    for x in names:
        activator(x,data_file) #REACTIVE TITLE BAR 

    os.system("zip -r resume.zip template")
    os.system("rm -rf template")






    