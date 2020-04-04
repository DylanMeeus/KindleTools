import os
import sys
import json
from webbot import Browser

url = "https://read.amazon.com/kp/notebook"

def extractUserPass():
    return (sys.argv[1], sys.argv[2])

def login(web):
    web.go_to(url)
    up = extractUserPass()
    web.type(up[0], id='ap_mail')
    web.type(up[1], id='ap_password')
    web.press(web.Key.ENTER)

def extractBooks(web):
    h2s = web.find_elements(tag='h2')
    books = []
    for h in h2s:
        books.append(h.text)
    return books

def extractHighlights(web, book):
    try:
        web.click(book)
        elements = web.find_elements(id='highlight')
    except:
        print("could not read " + book)
        return
    highlights = []
    for e in elements:
        highlights.append(e.text)
    return highlights



if __name__ == '__main__':
    web = Browser(showWindow=True) # easier debugging
    login(web)
    books = extractBooks(web)
    book_highlights = {}
    for book in books:
        print("extracting highlights for " + book)
        hs = extractHighlights(web, book)
        book_highlights[book] = hs
    print("writing to json file")
    js = json.dumps(book_highlights)
    f = open("highlights.json", 'w')
    f.write(js)
    f.close()
    print("done")


    

