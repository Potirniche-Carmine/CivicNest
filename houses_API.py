import requests
import time

#Code from URL down to response were provided by RapidApi itself.
def ForSale(properties):
    numData = 0
    url = "https://zillow-working-api.p.rapidapi.com/search/bypolygon"

    querystring1 = {"polygon":"39.550756 -119.821856,39.534907 -119.817108,39.537364 -119.788122,39.556199 -119.788684,39.556150 -119.800179,39.555091 -119.803115,39.552394 -119.806176,39.550756 -119.821856 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"For_Sale","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    headers = {
	"x-rapidapi-key": "eb433fb3e6msh6f40dfa8c7810a1p1587fbjsn9ddafafaa1a5",
	"x-rapidapi-host": "zillow-working-api.p.rapidapi.com"
    }
    response1 = requests.get(url=url, headers=headers,params=querystring1)
    data1 = response1.json()
    if isinstance(data1.get("searchResults"), list) and len(data1["searchResults"]) > 0:
        for result in data1["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })
    
    querystring2 = {"polygon":"39.550756 -119.821856,39.534907 -119.817108,39.537364 -119.788122,39.556199 -119.788684,39.556150 -119.800179,39.555091 -119.803115,39.552394 -119.806176,39.550756 -119.821856","page":"1","sortOrder":"Homes_for_you","listingStatus":"For_Sale","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    response2 = requests.get(url=url, headers=headers,params=querystring2)
    data2 = response2.json()
    if isinstance(data2.get("searchResults"), list) and len(data2["searchResults"]) > 0:
        for result in data2["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })
    querystring3 = {"polygon":"39.523864 -119.862108, 39.525579 -119.858053, 39.526185 -119.853998, 39.526941 -119.836142, 39.528909 -119.830452, 39.530170 -119.828490, 39.531633 -119.823715, 39.533600 -119.819006, 39.534205 -119.815932, 39.529985 -119.814385, 39.527843 -119.825395, 39.526275 -119.827937, 39.524291 -119.835278, 39.519552 -119.847818, 39.518531 -119.849175, 39.517871 -119.849804, 39.515531 -119.851025, 39.514344 -119.852699, 39.513089 -119.857115, 39.512795 -119.859123, 39.523864 -119.862108","page":"1","sortOrder":"Homes_for_you","listingStatus":"For_Sale","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    response3 = requests.get(url=url, headers=headers,params=querystring3)
    data3 = response3.json()
    if isinstance(data3.get("searchResults"), list) and len(data3["searchResults"]) > 0:
        for result in data3["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })
    
    querystring4 = {"polygon":"39.512475 -119.858883, 39.512631 -119.856763, 39.514111 -119.851716, 39.515931 -119.850298, 39.518351 -119.848867, 39.519976 -119.846009, 39.524137 -119.834961, 39.525441 -119.830844, 39.525975 -119.828201, 39.526761 -119.826750, 39.526426 -119.826447, 39.522065 -119.825039, 39.520377 -119.824540, 39.520043 -119.824540, 39.519207 -119.824952, 39.518088 -119.825104,  39.515917 -119.825702, 39.513025 -119.830327, 39.512687 -119.832080, 39.509908 -119.835828, 39.509670 -119.837760, 39.508793 -119.840632, 39.507191 -119.844673, 39.506790 -119.846409,  39.505923 -119.848032, 39.505312 -119.851010, 39.505617 -119.853218, 39.507529 -119.858445, 39.510695 -119.858487, 39.512475 -119.858883 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"For_Sale","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    response4 = requests.get(url=url, headers=headers,params=querystring4)
    data4 = response4.json()
    if isinstance(data4.get("searchResults"), list) and len(data4["searchResults"]) > 0:
        for result in data4["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })
    
    querystring5 = {"polygon":"39.516378 -119.825528, 39.516557 -119.825405, 39.517311 -119.825108, 39.517577 -119.824946, 39.517889 -119.824851, 39.518388 -119.824824, 39.518940 -119.824811, 39.519120 -119.824760, 39.519549 -119.824561, 39.519843 -119.824426, 39.520113 -119.824359, 39.520381 -119.824342, 39.520616 -119.824356, 39.520675 -119.824372, 39.520990 -119.824463, 39.521375 -119.824588, 39.521969 -119.824800, 39.526509 -119.826328, 39.526676 -119.826338, 39.526928 -119.826560, 39.527617 -119.825575, 39.527690 -119.825424, 39.527727 -119.825332, 39.529821 -119.814318,  39.525224 -119.812772, 39.524781 -119.812521, 39.522240 -119.811568, 39.521923 -119.811325, 39.521743 -119.811118, 39.520419 -119.810494, 39.520168 -119.811361, 39.520057 -119.821529, 39.520041 -119.821713, 39.520001 -119.821885, 39.519905 -119.822117, 39.519153 -119.823229, 39.519034 -119.823366, 39.517325 -119.824659, 39.517186 -119.824869, 39.516404 -119.825406, 39.516378 -119.825528 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"For_Sale","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
    response5 = requests.get(url=url, headers=headers,params=querystring5)
    data5 = response5.json()
    if isinstance(data5.get("searchResults"), list) and len(data5["searchResults"]) > 0:
        for result in data5["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })
    print(numData)
    return properties

def Sold(properties):
    numData = 0
    url = "https://zillow-working-api.p.rapidapi.com/search/bypolygon"

    querystring1 = {"polygon":"39.550756 -119.821856,39.534907 -119.817108,39.537364 -119.788122,39.556199 -119.788684,39.556150 -119.800179,39.555091 -119.803115,39.552394 -119.806176,39.550756 -119.821856 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    headers = {
	"x-rapidapi-key": "eb433fb3e6msh6f40dfa8c7810a1p1587fbjsn9ddafafaa1a5",
	"x-rapidapi-host": "zillow-working-api.p.rapidapi.com"
    }
    response1 = requests.get(url=url, headers=headers,params=querystring1)
    data1 = response1.json()
    if isinstance(data1.get("searchResults"), list) and len(data1["searchResults"]) > 0:
        for result in data1["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })
    
    querystring2 = {"polygon":"39.550756 -119.821856,39.534907 -119.817108,39.537364 -119.788122,39.556199 -119.788684,39.556150 -119.800179,39.555091 -119.803115,39.552394 -119.806176,39.550756 -119.821856","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    response2 = requests.get(url=url, headers=headers,params=querystring2)
    data2 = response2.json()
    if isinstance(data2.get("searchResults"), list) and len(data2["searchResults"]) > 0:
        for result in data2["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })

    querystring3 = {"polygon":"39.523864 -119.862108, 39.525579 -119.858053, 39.526185 -119.853998, 39.526941 -119.836142, 39.528909 -119.830452, 39.530170 -119.828490, 39.531633 -119.823715, 39.533600 -119.819006, 39.534205 -119.815932, 39.529985 -119.814385, 39.527843 -119.825395, 39.526275 -119.827937, 39.524291 -119.835278, 39.519552 -119.847818, 39.518531 -119.849175, 39.517871 -119.849804, 39.515531 -119.851025, 39.514344 -119.852699, 39.513089 -119.857115, 39.512795 -119.859123, 39.523864 -119.862108","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    response3 = requests.get(url=url, headers=headers,params=querystring3)
    data3 = response3.json()
    if isinstance(data3.get("searchResults"), list) and len(data3["searchResults"]) > 0:
        for result in data3["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })

    querystring4 = {"polygon":"39.512475 -119.858883, 39.512631 -119.856763, 39.514111 -119.851716, 39.515931 -119.850298, 39.518351 -119.848867, 39.519976 -119.846009, 39.524137 -119.834961, 39.525441 -119.830844, 39.525975 -119.828201, 39.526761 -119.826750, 39.526426 -119.826447, 39.522065 -119.825039, 39.520377 -119.824540, 39.520043 -119.824540, 39.519207 -119.824952, 39.518088 -119.825104,  39.515917 -119.825702, 39.513025 -119.830327, 39.512687 -119.832080, 39.509908 -119.835828, 39.509670 -119.837760, 39.508793 -119.840632, 39.507191 -119.844673, 39.506790 -119.846409,  39.505923 -119.848032, 39.505312 -119.851010, 39.505617 -119.853218, 39.507529 -119.858445, 39.510695 -119.858487, 39.512475 -119.858883 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    response4 = requests.get(url=url, headers=headers,params=querystring4)
    data4 = response4.json()
    if isinstance(data4.get("searchResults"), list) and len(data4["searchResults"]) > 0:
        for result in data4["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })

    querystring5 = {"polygon":"39.512475 -119.858883, 39.512631 -119.856763, 39.514111 -119.851716, 39.515931 -119.850298, 39.518351 -119.848867, 39.519976 -119.846009, 39.524137 -119.834961, 39.525441 -119.830844, 39.525975 -119.828201, 39.526761 -119.826750, 39.526426 -119.826447, 39.522065 -119.825039, 39.520377 -119.824540, 39.520043 -119.824540, 39.519207 -119.824952, 39.518088 -119.825104,  39.515917 -119.825702, 39.513025 -119.830327, 39.512687 -119.832080, 39.509908 -119.835828, 39.509670 -119.837760, 39.508793 -119.840632, 39.507191 -119.844673, 39.506790 -119.846409,  39.505923 -119.848032, 39.505312 -119.851010, 39.505617 -119.853218, 39.507529 -119.858445, 39.510695 -119.858487, 39.512475 -119.858883 ","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    response5 = requests.get(url=url, headers=headers,params=querystring5)
    data5 = response5.json()
    if isinstance(data5.get("searchResults"), list) and len(data5["searchResults"]) > 0:
        for result in data5["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })

    querystring6 = {"polygon":"39.516378 -119.825528, 39.516557 -119.825405, 39.517311 -119.825108, 39.517577 -119.824946, 39.517889 -119.824851, 39.518388 -119.824824, 39.518940 -119.824811, 39.519120 -119.824760, 39.519549 -119.824561, 39.519843 -119.824426, 39.520113 -119.824359, 39.520381 -119.824342, 39.520616 -119.824356, 39.520675 -119.824372, 39.520990 -119.824463, 39.521375 -119.824588, 39.521969 -119.824800, 39.526509 -119.826328, 39.526676 -119.826338, 39.526928 -119.826560, 39.527617 -119.825575, 39.527690 -119.825424, 39.527727 -119.825332, 39.529821 -119.814318,  39.525224 -119.812772, 39.524781 -119.812521, 39.522240 -119.811568, 39.521923 -119.811325, 39.521743 -119.811118, 39.520419 -119.810494, 39.520168 -119.811361, 39.520057 -119.821529, 39.520041 -119.821713, 39.520001 -119.821885, 39.519905 -119.822117, 39.519153 -119.823229, 39.519034 -119.823366, 39.517325 -119.824659, 39.517186 -119.824869, 39.516404 -119.825406, 39.516378 -119.825528 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
    response6 = requests.get(url=url, headers=headers,params=querystring6)
    data6 = response6.json()
    if isinstance(data6.get("searchResults"), list) and len(data6["searchResults"]) > 0:
        for result in data6["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })
    
    querystring7 = {"polygon":"39.516378 -119.825528, 39.516557 -119.825405, 39.517311 -119.825108, 39.517577 -119.824946, 39.517889 -119.824851, 39.518388 -119.824824, 39.518940 -119.824811, 39.519120 -119.824760, 39.519549 -119.824561, 39.519843 -119.824426, 39.520113 -119.824359, 39.520381 -119.824342, 39.520616 -119.824356, 39.520675 -119.824372, 39.520990 -119.824463, 39.521375 -119.824588, 39.521969 -119.824800, 39.526509 -119.826328, 39.526676 -119.826338, 39.526928 -119.826560, 39.527617 -119.825575, 39.527690 -119.825424, 39.527727 -119.825332, 39.529821 -119.814318,  39.525224 -119.812772, 39.524781 -119.812521, 39.522240 -119.811568, 39.521923 -119.811325, 39.521743 -119.811118, 39.520419 -119.810494, 39.520168 -119.811361, 39.520057 -119.821529, 39.520041 -119.821713, 39.520001 -119.821885, 39.519905 -119.822117, 39.519153 -119.823229, 39.519034 -119.823366, 39.517325 -119.824659, 39.517186 -119.824869, 39.516404 -119.825406, 39.516378 -119.825528 ","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
    response7 = requests.get(url=url, headers=headers,params=querystring7)
    data7 = response7.json()
    if isinstance(data7.get("searchResults"), list) and len(data7["searchResults"]) > 0:
        for result in data7["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })
    print(numData)
    return properties


def ForRent(properties):
    numData = 0
    url = "https://zillow-working-api.p.rapidapi.com/search/bypolygon"

    querystring1 = {"polygon":"39.550756 -119.821856,39.534907 -119.817108,39.537364 -119.788122,39.556199 -119.788684,39.556150 -119.800179,39.555091 -119.803115,39.552394 -119.806176,39.550756 -119.821856 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"For_Rent","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    headers = {
	"x-rapidapi-key": "eb433fb3e6msh6f40dfa8c7810a1p1587fbjsn9ddafafaa1a5",
	"x-rapidapi-host": "zillow-working-api.p.rapidapi.com"
    }
    response1 = requests.get(url=url, headers=headers,params=querystring1)
    data1 = response1.json()
    if isinstance(data1.get("searchResults"), list) and len(data1["searchResults"]) > 0:
        for result in data1["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })
    
    querystring2 = {"polygon":"39.550756 -119.821856,39.534907 -119.817108,39.537364 -119.788122,39.556199 -119.788684,39.556150 -119.800179,39.555091 -119.803115,39.552394 -119.806176,39.550756 -119.821856","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    response2 = requests.get(url=url, headers=headers,params=querystring2)
    data2 = response2.json()
    if isinstance(data2.get("searchResults"), list) and len(data2["searchResults"]) > 0:
        for result in data2["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })

    querystring3 = {"polygon":"39.523864 -119.862108, 39.525579 -119.858053, 39.526185 -119.853998, 39.526941 -119.836142, 39.528909 -119.830452, 39.530170 -119.828490, 39.531633 -119.823715, 39.533600 -119.819006, 39.534205 -119.815932, 39.529985 -119.814385, 39.527843 -119.825395, 39.526275 -119.827937, 39.524291 -119.835278, 39.519552 -119.847818, 39.518531 -119.849175, 39.517871 -119.849804, 39.515531 -119.851025, 39.514344 -119.852699, 39.513089 -119.857115, 39.512795 -119.859123, 39.523864 -119.862108","page":"1","sortOrder":"Homes_for_you","listingStatus":"For_Rent","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    response3 = requests.get(url=url, headers=headers,params=querystring3)
    data3 = response3.json()
    if isinstance(data3.get("searchResults"), list) and len(data3["searchResults"]) > 0:
        for result in data3["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })

    querystring4 = {"polygon":"39.512475 -119.858883, 39.512631 -119.856763, 39.514111 -119.851716, 39.515931 -119.850298, 39.518351 -119.848867, 39.519976 -119.846009, 39.524137 -119.834961, 39.525441 -119.830844, 39.525975 -119.828201, 39.526761 -119.826750, 39.526426 -119.826447, 39.522065 -119.825039, 39.520377 -119.824540, 39.520043 -119.824540, 39.519207 -119.824952, 39.518088 -119.825104,  39.515917 -119.825702, 39.513025 -119.830327, 39.512687 -119.832080, 39.509908 -119.835828, 39.509670 -119.837760, 39.508793 -119.840632, 39.507191 -119.844673, 39.506790 -119.846409,  39.505923 -119.848032, 39.505312 -119.851010, 39.505617 -119.853218, 39.507529 -119.858445, 39.510695 -119.858487, 39.512475 -119.858883 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"For_Rent","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    response4 = requests.get(url=url, headers=headers,params=querystring4)
    data4 = response4.json()
    if isinstance(data4.get("searchResults"), list) and len(data4["searchResults"]) > 0:
        for result in data4["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })

    querystring5 = {"polygon":"39.516378 -119.825528, 39.516557 -119.825405, 39.517311 -119.825108, 39.517577 -119.824946, 39.517889 -119.824851, 39.518388 -119.824824, 39.518940 -119.824811, 39.519120 -119.824760, 39.519549 -119.824561, 39.519843 -119.824426, 39.520113 -119.824359, 39.520381 -119.824342, 39.520616 -119.824356, 39.520675 -119.824372, 39.520990 -119.824463, 39.521375 -119.824588, 39.521969 -119.824800, 39.526509 -119.826328, 39.526676 -119.826338, 39.526928 -119.826560, 39.527617 -119.825575, 39.527690 -119.825424, 39.527727 -119.825332, 39.529821 -119.814318,  39.525224 -119.812772, 39.524781 -119.812521, 39.522240 -119.811568, 39.521923 -119.811325, 39.521743 -119.811118, 39.520419 -119.810494, 39.520168 -119.811361, 39.520057 -119.821529, 39.520041 -119.821713, 39.520001 -119.821885, 39.519905 -119.822117, 39.519153 -119.823229, 39.519034 -119.823366, 39.517325 -119.824659, 39.517186 -119.824869, 39.516404 -119.825406, 39.516378 -119.825528 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"For_Rent","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
    response5 = requests.get(url=url, headers=headers,params=querystring5)
    data5 = response5.json()
    if isinstance(data5.get("searchResults"), list) and len(data5["searchResults"]) > 0:
        for result in data5["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            
            # Check if all necessary fields are present
            if zpid and street_address and value is not None and latitude and longitude:
                numData += 1
                # Add the property data to the list
                properties.append({
                    "zpid": zpid,
                    "address": street_address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "latitude": latitude,
                    "longitude": longitude,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft
                })
    print(numData)
    return properties
    
def DataCollection():
    properties = []
    ForSale(properties)
    ForRent(properties)
    Sold(properties)

if __name__ == '__main__':
   DataCollection()
