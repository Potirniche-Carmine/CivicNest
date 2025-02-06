import requests
import time

#Code from URL down to response were provided by RapidApi itself.
def houses():
    properties = []
    i = 0
    url = "https://zillow56.p.rapidapi.com/search"

    querystring = {"polygon":"39.550756 -119.821856,39.534907 -119.817108,39.537364 -119.788122,39.556199 -119.788684,39.556150 -119.800179,39.555091 -119.803115,39.552394 -119.806176,39.550756 -119.821856 ","output":"json","status":"forSale","sortSelection":"priorityscore","listing_type":"by_agent","doz":"any"}

    headers = {
	    "x-rapidapi-key": "eb433fb3e6msh6f40dfa8c7810a1p1587fbjsn9ddafafaa1a5",
	    "x-rapidapi-host": "zillow56.p.rapidapi.com"
    }
    response = requests.get(url=url, headers=headers,params=querystring)
    data = response.json()
    if isinstance(data.get("results"), list) and len(data["results"]) > 0:
        for i in data["results"]:
            zpid = i.get("zpid", None) 
            address = i.get("streetAddress", None)
            price = i.get("price",None)
            latitude = i.get("latitude",None)
            longitude = i.get("longitude",None)
            if zpid and address and price and latitude and longitude:  
                properties.append({"zpid": zpid, "address": address, "price": price, "latitude": latitude, "longitude": longitude})
    #print(properties)      
    return properties
