###
#Goals better tags. Make code modular using the main file. 
###
import os
from insert import *
from activate import *
from pages import *
import json
import sys
# reading csv file 
# with open(sys.argv[1]) as json_file:  
#     data_file= json.load(json_file)


def build_website(data_file):
    os.system("cp -r assets/themes/Theme1 template")
    data = data_file

    names = list(data["settings"]["Pages"].keys())
#generating the navigation bar and creating the files
    elements = []
    for x in names:
        os.system("cp template/left-sidebar.html template/" +data["settings"]["Pages"][x] +'.html')
        elements.append('<li><a href="' + data["settings"]["Pages"][x] + '.html"><span>' + x +  '<span class="border"></span></span></a></li>')
        Title = ['<h1 class="intro-lead">'+x+'</h1>']
        insert_elements("template/"+data["settings"]["Pages"][x]+".html",Title,'<!-- Make Title Generator -->')

    #os.system("cp template/index2.html template/index.html")
    insert_elements("template/index.html",elements,'<!-- Make a generator for above list -->')
    Author_name = ['<a class="navbar-brand" href="index.html">'+data["settings"]["Name"]+'</a>']
    insert_elements("template/index.html",Author_name,'<!--Name of Author -->')
    Title_and_Authtor = ['<title>'+data["settings"]["Name"]+'&mdash; Resume</title>']
    Author_details = ordering("Home",data)
    Author_details_new = []
    for x in Author_details:
        x = x.replace("<h2>","<b>")
        x = x.replace("</h2>","</b>")
        #replace h1 with h2 and replace h2 with b
        x = x.replace("<h1>","<h2>")
        x = x.replace("</h1>","</h2>")
        Author_details_new.append(x)
    # print(Author_details_new)

    insert_elements("template/index.html",Author_details_new,'<!--About me -->')
    Author_email = ['<p><a href="mailto:'+data["settings"]["Email"]+'"'+'class="btn btn-primary">Email</a></p>']
    insert_elements("template/index.html",Author_email,'<!--Email -->')

    Author_image = ['<img src='+'"'+data["settings"]["Image"] +'"'+', width=270, hspace=50>']
    insert_elements("template/index.html",Author_image,'<!--Image -->')

    ## Footer

    #if data["settings"][""]

    for x in names:
        activator(x,data_file) #REACTIVE TITLE BAR 

        #ADDING CONTENT IN PAGES
        insert_elements("template/"+data["settings"]["Pages"][x]+'.html',ordering(data["settings"]["Pages"][x],data),'<!-- Content Generator -->')

    os.system('mv template website')







    