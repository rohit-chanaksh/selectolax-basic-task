from utils.dataScraper import getDatafromUrl
from utils.dataScraper import Num_Converter
from utils.dataScraper import get_num_price


from selectolax.parser import HTMLParser

bUrl = 'https://books.toscrape.com/'


def getBookName(book):
    return ''


if __name__ == "__main__":
    htmlPage = getDatafromUrl(bUrl)
    # print(htmlPage)
    tree = HTMLParser(htmlPage)

    arTitle =  tree.css_first("h3 a").attributes['title']

    price = get_num_price(tree.css_first('p.price_color').text())

    rating = Num_Converter(tree.css_first('p.star-rating').attributes['class'])

    print('-----')
    print('-----')
    print('-----',arTitle)
    print('-----')
    print('-----')
    print('-----',price)
    print('-----')
    print('-----')
    print('-----',rating)
    print('-----')
    print('-----')


    