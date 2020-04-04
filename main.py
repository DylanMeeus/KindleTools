import sys
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
    web.click(book)
    elements = web.find_elements(id='highlight')
    highlights = []
    for e in elements:
        highlights.append(e.text)
    return highlights



if __name__ == '__main__':
    web = Browser(showWindow=True) # easier debugging
    login(web)
    books = extractBooks(web)
    qs = extractHighlights(web, books[2])
    for q in qs:
        print(q)
    

