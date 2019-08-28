import html_file

def build_website(data):
    
    basics = data["basics"]
    pages= ['Home']+basics["pages"]
    theme = basics["theme"]
    
    home = html_file.Home()

    home.make_navigator(pages)
    home.author_image(basics["image"]) 
    home.author_name(basics["name"])
    home.email(basics["email"])

    home.add_content(data,'<!--About me -->') 
    home.write_html()
    for x in pages:
        
        page = html_file.SidePage(x)

        page.make_navigator(pages)
        page.author_name(basics["name"])
        page.author_image(basics["image"])
        page.add_content(data,'<!-- Content Generator -->')
        page.write_html()
    # if basics["support_us"]=="YES": 
    #    insert_file(home,"template/ad.html","<!--Footer -->")
