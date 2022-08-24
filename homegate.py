#!/usr/bin/env python3

#import modules
import requests #, mysql
from bs4 import BeautifulSoup

#def everyDay():
#    pass

def getPropertyListings():
   
    RENT = "https://www.homegate.ch/rent/real-estate/country-switzerland/matching-list"
    BUY = "https://www.homegate.ch/buy/apartment/country-switzerland/matching-list"
    
    page = requests.get(RENT)
    pageObject = BeautifulSoup(page.content, "html.parser")

    results = pageObject.select("#app > main > div > div.SeoEntryResultListPage_rootWrapper_1s-Ur > div > div.ResultListPage_stickyParent_2d4Bp > div:nth-child(2) > div:nth-child(1) > a > div > div.ListItemTopPremium_holder_27lq1 > div.ListItemTopPremium_data_3i7Ca > p:nth-child(1) > span.ListItemPrice_price_1o0i3")

    for each in results:
        print(each)


getPropertyListings()