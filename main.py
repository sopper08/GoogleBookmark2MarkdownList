from bs4 import BeautifulSoup

def html2md(lines):
    preSpace = -1

    while len(lines):
        line = lines.pop(0)
        if "<DL><p>" in line:
            preSpace += 1
            continue
        if "</DL><p>" in line:
            preSpace -= 1
            continue
        if "<DT>" in line:
            soup = BeautifulSoup(line, "html.parser")
            title = soup.text[1:-1]
            try:
                content = soup.find('a')['href']
            except:
                content = ""
            
            if content != "":
                print("{0}* [{1}]({2})".format("    " * preSpace, title, content))
            else:
                print("{0}* {1}".format("    " * preSpace, title))

def main():
    with open("./GoogleBookmarks.html", 'r') as f:
        lines = f.readlines()
    
    html2md(lines)

if __name__ == "__main__":
    main()