#!/usr/bin/env python3


#import necessary modules
import requests, sys, json
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
    LISTINGS = "https://api.homegate.ch/search/listings"

    feedback1

    parameters = {"query":{"offerType":"RENT","categories":["APARTMENT","HOUSE"],"location":{"geoTags":["geo-country-switzerland"]}},"sortBy":"dateCreated","sortDirection":"desc","from":0,"size":20,"trackTotalHits":"true","fieldset":"srp-list"}
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
    response = requests.post(LISTINGS,headers=headers, json=parameters)
    # print(type(response.json()))
    data = response.json()
    print(data)

    # for each in data["results"]:
    #     print(each["listing"]["address"])
    #     print("then here is the price")
    #     print(each["listing"]["prices"])
    #     # print(each["listing"]["address"])
    #     print(each["listing"]["address"])

    # print(data["results"][0])

    # print(data[])
    # for each in data:
        # print(each[0])
    # soup = BeautifulSoup(page.content, "html.parser")

    # feedback2
# 
    # prices = soup.find_all(class_="ListItemPrice_price_1o0i3")
    # roomNumber = soup.find_all(class_="ListItemRoomNumber_value_Hpn8O")
    # roomSpace = soup.find_all(class_="ListItemLivingSpace_value_2zFir")     

    # propertyDetails = (list(zip(prices,roomNumber,roomSpace)))    
    # for p,r,rs in propertyDetails:
    #    print(p.text,r.text,rs.text)
    

# feedback3
# db = MySQLdb.connect("localhost","user", "pass","listingsdb")
# cursor = db.cursor()  


getPropertyListings()