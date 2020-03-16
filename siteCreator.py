import sys
import os
from llib import install
prefx = ""
def openFile(filename):
    with open(filename,"r",encoding="UTF-8") as f:
        return f.read()

def saveToFile(filename,data,mode="w"):
    with open(filename,mode,encoding="UTF-8") as f:
        f.write(data)
        return True

def createTree(root,dirlist=["templates","static","src"],staticdirlist=["images","scripts"]):
    os.mkdir(prefx+root)
    for i in dirlist:
        os.mkdir(prefx+root+"/"+i)
        if i == "static":
            for j in staticdirlist:
                os.mkdir(prefx+root+"/"+i+"/"+j)
    return True

def createIndexs(root, pathToCSS="{{ url_for('static', filename='style.css') }}", pathToJS="{{ url_for('static', filename='scripts/main.js') }}"):
    indexPage = openFile("pattern.html")
    indexPage = indexPage.replace("[title]",root)
    indexPage = indexPage.replace("[pathToCSS]",pathToCSS)
    indexPage = indexPage.replace("[pathToJS]",pathToJS)
    saveToFile(prefx+root+"/templates/index.html", indexPage)
    css = "/*place style here*/"
    js = "//place javascript here"
    app = openFile("pattern.py")
    saveToFile(prefx+root+"/static/style.css", css)
    saveToFile(prefx+root+"/static/scripts/main.js", js)
    saveToFile(prefx+root+"/app.py", app)
    return True

def main():
    try:
        if sys.argv[2] == "-f":
            print("====|Flask install enable|====")
            install("flask")
    except IndexError:
        print("====|Flask install disable|====")
    try:
        root=str(sys.argv[1])
    except IndexError:
        print("====|Use \"python siteCreate.py [Name] [-f]\"|====")
            
    try:
        createTree(root)
        createIndexs(root)
        print("====|Project created!|====")
    except FileExistsError:
        print("====|Project \""+root+"\" is exists!|====")
    except UnboundLocalError:
        pass

if __name__ == "__main__":
    sys.exit(main())
