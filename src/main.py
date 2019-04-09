# Import pandas 
import pandas as pd 
import os
from insert import *
from activate import *
# reading csv file 
df = pd.read_csv("renuka.csv") 

#creating files using headinds
names = list(df.columns)
#generating the navigation bar and creating the files
elements = []
for x in names:
    os.system("cp template/left-sidebar.html template/" +x +'.html')
    elements.append('<li><a href="' + x + '.html"><span>' + x +  '<span class="border"></span></span></a></li>')
# file name, elements, label
os.system("cp template/index2.html template/index.html")
insert_elements("template/index.html",elements,'<!-- Make a generator for above list -->')
for x in names:
    activator(x)