#!/usr/bin/env python3


#import necessary modules
from email import feedparser
import requests, sys, csv#, MySQLdb
from bs4 import BeautifulSoup


#visual feedback 
feedback1 = print("Getting webpage....")
feedback2 = print("Webpage Saved....")
feedback3 = print("Connecting DB....")


#def everyDay():
#    pass

# get rent and buy listings 
def getPropertyListings():
   
    RENT = "https://www.homegate.ch/rent/real-estate/country-switzerland/matching-list?o=dateCreated-desc"
    BUY = "https://www.homegate.ch/buy/apartment/country-switzerland/matching-list?o=dateCreated-desc"
    
    feedback1

    page = requests.get(RENT)
    soup = BeautifulSoup(page.content, "html.parser")

    feedback2

    prices = soup.find_all(class_="ListItemPrice_price_1o0i3")
    roomNumber = soup.find_all(class_="ListItemRoomNumber_value_Hpn8O")
    roomSpace = soup.find_all(class_="ListItemLivingSpace_value_2zFir")     

    propertyDetails = (list(zip(prices,roomNumber,roomSpace)))    
    for p,r,rs in propertyDetails:
       print(p.text,r.text,rs.text)
    

feedback3
db = MySQLdb.connect("localhost","user", "pass","listingsdb")
cursor = db.cursor()  


getPropertyListings()