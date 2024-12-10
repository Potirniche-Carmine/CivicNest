import requests
import time

def houses():
    url = "https://zillow56.p.rapidapi.com/search"

    querystring = {"polygon":"39.723844 -120.001231,39.747606, -119.704257,39.396162 -119.700127,39.399877 -120.006381,39.723844 -120.001231","output":"json","sortSelection":"priorityscore","listing_type":"by_agent","doz":"any"}
    
    headers = {
        "x-rapidapi-key": "eb433fb3e6msh6f40dfa8c7810a1p1587fbjsn9ddafafaa1a5",
        "x-rapidapi-host": "zillow56.p.rapidapi.com"
    }

    response = requests.get(url=url, headers=headers,params=querystring)
    data = response.json()
    if isinstance(data.get("results"), list) and len(data["results"]) > 0:
            properties = []
            i = 0
            for i in data["results"]:
                zpid = i.get("zpid", None) 
                address = i.get("streetAddress", None)
                price = i.get("price",None)
                latitude = i.get("latitude",None)
                longitude = i.get("longitude",None)
                if zpid and address and price and latitude and longitude:  
                    properties.append({"zpid": zpid, "address": address, "price": price, "latitude":latitude, "longitude":longitude})

    #print(properties)      
    return properties
