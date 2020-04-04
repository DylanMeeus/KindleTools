import sys
from webbot import Browser


url = "https://www.amazon.com/ap/signin?openid.return_to=https%3A%2F%2Fread.amazon.com%2Fkp%2Fnotebook%3FamazonDeviceType%3DA2CLFWBIMVSE9N&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_kp_us&openid.mode=checkid_setup&marketPlaceId=ATVPDKIKX0DER&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_kp_notebook_us&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=1209600&siteState=clientContext%3D138-0567063-7383049%2CsourceUrl%3Dhttps%253A%252F%252Fread.amazon.com%252Fkp%252Fnotebook%253FamazonDeviceType%253DA2CLFWBIMVSE9N%2Csignature%3DmI9EO9Jj2FMnsvPjvrubJpSQKHg8kj3D&language=en_US&auth=Customer+is+not+authenticated"

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


if __name__ == '__main__':
    web = Browser(showWindow=False)
    login(web)
    books = extractBooks(web)
    print(books[2])
