# Plutarchus

Read full documentation: https://github.com/ayushpatnaikgit/plutarchus/blob/master/docs/USER_DOC.pdf

   Plutarchus is an open source personal website building tool. It takes a JSON file and generates a website using the data in the JSON file. The JSON file is the dataset of the user's work. The websites that Plutarchus generates are static HTMLs, however Javascript and CSS are integrated to make then at par with modern web designs. Plutarchus v0.1 is designed to build resume websites.
    The examples and test cases are websites of academics and hence same are the target audience for v 0.1.

# How to use

1. Construct the dataset of your work in a JSON file by editing assets/basic_format.json
2. Either use the commandline interface or the web app to construct the website by supplying the JSON file. 

## Making JSON File

There should be a settings section and an entries section in the JSON. The format is provided in assets/basic_format.json 

The settings section contains basic information such as name of the user, theme, email address of the user, page names, etc. 

The entries section contains all the dataset of the users work and the home page. 

## Command Line Interface

$ git clone https://github.com/ayushpatnaikgit/plutarchus.git
If you JSON file is name example.JSON and it is in the plutarchus folder, 
run 
$ python src/plutarchus.py example.JSON. 
If your JSON file is elsewhere, write the path instead of just 'example.json'
this will generate a folder names 'template'. This is your website. Open index.html to view it. 

## Graphical User Interface (web app)

Go to plutarchus.com to view the web app. 
upload the JSON file. 
Download and unzip the file shown in the prompt. 
You will see a folder 'template'. This is your website. Open index.html to view it.




