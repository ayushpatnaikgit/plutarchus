import os
from insert import *
from activate import *
from pages import *
import json
import sys
from build_funcs import *
# reading csv file 
with open(sys.argv[1]) as json_file:  
    data_file = json.load(json_file)
#creating files using headinds
os.system("rm -rf template")
build_website(data_file)
#os.system("unzip resume.zip")
#os.system("rm -rf resume.zip")
