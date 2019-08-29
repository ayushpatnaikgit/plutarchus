from plutarchus.html_file import Home,SidePage
def build_website(data):
    
    basics = data["basics"]
    pages= ['Home']+basics["pages"]
    home = Home()

    home.make_navigator(pages)
    home.author_image(basics["image"]) 
    home.author_name(basics["name"])
    home.email(basics["email"])

    home.select_and_add_content(data) 
    home.write_html()
    for x in pages:
        
        page = SidePage(x)

        page.make_navigator(pages)
        page.author_name(basics["name"])
        page.author_image(basics["image"])
        page.select_and_add_content(data)
        page.write_html()
    # if basics["support_us"]=="YES": 
    #    insert_file(home,"template/ad.html","<!--Footer -->")
