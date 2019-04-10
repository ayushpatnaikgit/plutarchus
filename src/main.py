import os
from insert import *
from activate import *
import json
# reading csv file 
with open('saner.json') as json_file:  
    data = json.load(json_file)
#creating files using headinds
names = list(data["settings"]["Pages"].keys())
#generating the navigation bar and creating the files
elements = []
for x in names:
    os.system("cp template/left-sidebar.html template/" +data["settings"]["Pages"][x] +'.html')
    elements.append('<li><a href="' + data["settings"]["Pages"][x] + '.html"><span>' + x +  '<span class="border"></span></span></a></li>')
    Title = ['<h1 class="intro-lead">'+x+'</h1>']
    insert_elements("template/"+data["settings"]["Pages"][x]+".html",Title,'<!-- Make Title Generator -->')
# file name, elements, label
os.system("cp template/index2.html template/index.html")
insert_elements("template/index.html",elements,'<!-- Make a generator for above list -->')

for x in names:
    activator(x)
    insert_file("template/"+data["settings"]["Pages"][x]+'.html','template/sample_temp.html','<!-- Content Generator -->')
