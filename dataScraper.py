from playwright.sync_api import sync_playwright

import re  # for regex

def getDatafromUrl(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)

        page = browser.new_page()

        page.goto(url)
        page.wait_for_load_state('networkidle')
        htmlpage = page.inner_html('body')

        return htmlpage
    
def Num_Converter(num_text ) :
    if num_text == 'star-rating One' :
        return 1 
    elif num_text == 'star-rating Two' :
        return 2
    elif num_text == 'star-rating Three' :
        return 3 
    elif num_text == 'star-rating Four' :
        return 4
    elif num_text == 'star-rating Five' :
        return 5
    else :
        return 0
    
def get_num_price(pricetext):
     pricematch = re.search(r'\d+\.\d+', pricetext)
     priceValue = float(pricematch.group())
     return priceValue
    
