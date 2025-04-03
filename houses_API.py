import requests
import time

#Code from URL down to response were provided by RapidApi itself. https://rapidapi.com/oneapiproject/api/zillow-working-api/playground/apiendpoint_68fbab94-16cf-4b5a-a643-a6f8fcee068d 
def Sold(properties):
    numData = 0
    url = "https://zillow-working-api.p.rapidapi.com/search/bypolygon"

    querystring1 = {"polygon":"39.550756 -119.821856,39.534907 -119.817108,39.537364 -119.788122,39.556199 -119.788684,39.556150 -119.800179,39.555091 -119.803115,39.552394 -119.806176,39.550756 -119.821856 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

    headers = {
	"x-rapidapi-key": "eb433fb3e6msh6f40dfa8c7810a1p1587fbjsn9ddafafaa1a5",
	"x-rapidapi-host": "zillow-working-api.p.rapidapi.com"
    }
    time.sleep(1)
    response1 = requests.get(url=url, headers=headers,params=querystring1)
    data1 = response1.json()
    if isinstance(data1.get("searchResults"), list) and len(data1["searchResults"]) > 0:
        for result in data1["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring3 = {"polygon":"39.523864 -119.862108, 39.525579 -119.858053, 39.526185 -119.853998, 39.526941 -119.836142, 39.528909 -119.830452, 39.530170 -119.828490, 39.531633 -119.823715, 39.533600 -119.819006, 39.534205 -119.815932, 39.529985 -119.814385, 39.527843 -119.825395, 39.526275 -119.827937, 39.524291 -119.835278, 39.519552 -119.847818, 39.518531 -119.849175, 39.517871 -119.849804, 39.515531 -119.851025, 39.514344 -119.852699, 39.513089 -119.857115, 39.512795 -119.859123, 39.523864 -119.862108","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response3 = requests.get(url=url, headers=headers,params=querystring3)
    data3 = response3.json()
    if isinstance(data3.get("searchResults"), list) and len(data3["searchResults"]) > 0:
        for result in data3["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring4 = {"polygon":"39.512475 -119.858883, 39.512631 -119.856763, 39.514111 -119.851716, 39.515931 -119.850298, 39.518351 -119.848867, 39.519976 -119.846009, 39.524137 -119.834961, 39.525441 -119.830844, 39.525975 -119.828201, 39.526761 -119.826750, 39.526426 -119.826447, 39.522065 -119.825039, 39.520377 -119.824540, 39.520043 -119.824540, 39.519207 -119.824952, 39.518088 -119.825104,  39.515917 -119.825702, 39.513025 -119.830327, 39.512687 -119.832080, 39.509908 -119.835828, 39.509670 -119.837760, 39.508793 -119.840632, 39.507191 -119.844673, 39.506790 -119.846409,  39.505923 -119.848032, 39.505312 -119.851010, 39.505617 -119.853218, 39.507529 -119.858445, 39.510695 -119.858487, 39.512475 -119.858883 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response4 = requests.get(url=url, headers=headers,params=querystring4)
    data4 = response4.json()
    if isinstance(data4.get("searchResults"), list) and len(data4["searchResults"]) > 0:
        for result in data4["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring5 = {"polygon":"39.512475 -119.858883, 39.512631 -119.856763, 39.514111 -119.851716, 39.515931 -119.850298, 39.518351 -119.848867, 39.519976 -119.846009, 39.524137 -119.834961, 39.525441 -119.830844, 39.525975 -119.828201, 39.526761 -119.826750, 39.526426 -119.826447, 39.522065 -119.825039, 39.520377 -119.824540, 39.520043 -119.824540, 39.519207 -119.824952, 39.518088 -119.825104,  39.515917 -119.825702, 39.513025 -119.830327, 39.512687 -119.832080, 39.509908 -119.835828, 39.509670 -119.837760, 39.508793 -119.840632, 39.507191 -119.844673, 39.506790 -119.846409,  39.505923 -119.848032, 39.505312 -119.851010, 39.505617 -119.853218, 39.507529 -119.858445, 39.510695 -119.858487, 39.512475 -119.858883 ","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response5 = requests.get(url=url, headers=headers,params=querystring5)
    data5 = response5.json()
    if isinstance(data5.get("searchResults"), list) and len(data5["searchResults"]) > 0:
        for result in data5["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring6 = {"polygon":"39.516378 -119.825528, 39.516557 -119.825405, 39.517311 -119.825108, 39.517577 -119.824946, 39.517889 -119.824851, 39.518388 -119.824824, 39.518940 -119.824811, 39.519120 -119.824760, 39.519549 -119.824561, 39.519843 -119.824426, 39.520113 -119.824359, 39.520381 -119.824342, 39.520616 -119.824356, 39.520675 -119.824372, 39.520990 -119.824463, 39.521375 -119.824588, 39.521969 -119.824800, 39.526509 -119.826328, 39.526676 -119.826338, 39.526928 -119.826560, 39.527617 -119.825575, 39.527690 -119.825424, 39.527727 -119.825332, 39.529821 -119.814318,  39.525224 -119.812772, 39.524781 -119.812521, 39.522240 -119.811568, 39.521923 -119.811325, 39.521743 -119.811118, 39.520419 -119.810494, 39.520168 -119.811361, 39.520057 -119.821529, 39.520041 -119.821713, 39.520001 -119.821885, 39.519905 -119.822117, 39.519153 -119.823229, 39.519034 -119.823366, 39.517325 -119.824659, 39.517186 -119.824869, 39.516404 -119.825406, 39.516378 -119.825528 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response6 = requests.get(url=url, headers=headers,params=querystring6)
    data6 = response6.json()
    if isinstance(data6.get("searchResults"), list) and len(data6["searchResults"]) > 0:
        for result in data6["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring7 = {"polygon":"39.516378 -119.825528, 39.516557 -119.825405, 39.517311 -119.825108, 39.517577 -119.824946, 39.517889 -119.824851, 39.518388 -119.824824, 39.518940 -119.824811, 39.519120 -119.824760, 39.519549 -119.824561, 39.519843 -119.824426, 39.520113 -119.824359, 39.520381 -119.824342, 39.520616 -119.824356, 39.520675 -119.824372, 39.520990 -119.824463, 39.521375 -119.824588, 39.521969 -119.824800, 39.526509 -119.826328, 39.526676 -119.826338, 39.526928 -119.826560, 39.527617 -119.825575, 39.527690 -119.825424, 39.527727 -119.825332, 39.529821 -119.814318,  39.525224 -119.812772, 39.524781 -119.812521, 39.522240 -119.811568, 39.521923 -119.811325, 39.521743 -119.811118, 39.520419 -119.810494, 39.520168 -119.811361, 39.520057 -119.821529, 39.520041 -119.821713, 39.520001 -119.821885, 39.519905 -119.822117, 39.519153 -119.823229, 39.519034 -119.823366, 39.517325 -119.824659, 39.517186 -119.824869, 39.516404 -119.825406, 39.516378 -119.825528 ","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response7 = requests.get(url=url, headers=headers,params=querystring7)
    data7 = response7.json()
    if isinstance(data7.get("searchResults"), list) and len(data7["searchResults"]) > 0:
        for result in data7["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring8 = {"polygon":"39.507446 -119.858525, 39.507330 -119.858121, 39.505990 -119.854425, 39.505472 -119.853019, 39.505392 -119.852748, 39.505319 -119.852451, 39.505276 -119.852168, 39.505237 -119.851915, 39.505203 -119.851360, 39.505220 -119.850869, 39.505291 -119.850333, 39.505548 -119.848798, 39.505650 -119.848395, 39.505846 -119.847852, 39.506058 -119.847437, 39.506505 -119.846710, 39.506766 -119.846148, 39.506845 -119.845877, 39.507052 -119.844867, 39.507168 -119.844464, 39.508731 -119.840509, 39.508804 -119.840259, 39.509522 -119.837919, 39.509642 -119.837326, 39.509835 -119.835869, 39.509873 -119.835693, 39.510405 -119.835042, 39.510525 -119.834897, 39.511941 -119.832805, 39.512394 -119.832285, 39.512599 -119.831977, 39.512844 -119.830623, 39.512904 -119.830369, 39.514030 -119.827962, 39.514158 -119.827746, 39.515369 -119.826118, 39.516056 -119.825450, 39.517180 -119.824638, 39.518133 -119.823965, 39.519021 -119.823208, 39.519840 -119.822046, 39.519926 -119.821807, 39.519969 -119.821540, 39.520071 -119.811376, 39.520321 -119.810455, 39.505875 -119.803397, 39.505451 -119.826479, 39.505051 -119.832718, 39.505029 -119.841608, 39.505087 -119.842127, 39.505014 -119.845251, 39.504956 -119.845619, 39.502866 -119.851565, 39.502458 -119.852301, 39.502422 -119.852622, 39.502431 -119.853767, 39.502338 -119.854044, 39.501760 -119.855227, 39.501305 -119.855901, 39.500777 -119.856968, 39.500723 -119.857245, 39.500777 -119.858065, 39.501150 -119.858010, 39.501527 -119.857985, 39.501888 -119.858005, 39.502260 -119.858075, 39.502548 -119.858176, 39.503169 -119.858398, 39.503682 -119.858488, 39.507446 -119.858525 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response8 = requests.get(url=url, headers=headers,params=querystring8)
    data8 = response8.json()
    if isinstance(data8.get("searchResults"), list) and len(data8["searchResults"]) > 0:
        for result in data8["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring9 = {"polygon":"39.507446 -119.858525, 39.507330 -119.858121, 39.505990 -119.854425, 39.505472 -119.853019, 39.505392 -119.852748, 39.505319 -119.852451, 39.505276 -119.852168, 39.505237 -119.851915, 39.505203 -119.851360, 39.505220 -119.850869, 39.505291 -119.850333, 39.505548 -119.848798, 39.505650 -119.848395, 39.505846 -119.847852, 39.506058 -119.847437, 39.506505 -119.846710, 39.506766 -119.846148, 39.506845 -119.845877, 39.507052 -119.844867, 39.507168 -119.844464, 39.508731 -119.840509, 39.508804 -119.840259, 39.509522 -119.837919, 39.509642 -119.837326, 39.509835 -119.835869, 39.509873 -119.835693, 39.510405 -119.835042, 39.510525 -119.834897, 39.511941 -119.832805, 39.512394 -119.832285, 39.512599 -119.831977, 39.512844 -119.830623, 39.512904 -119.830369, 39.514030 -119.827962, 39.514158 -119.827746, 39.515369 -119.826118, 39.516056 -119.825450, 39.517180 -119.824638, 39.518133 -119.823965, 39.519021 -119.823208, 39.519840 -119.822046, 39.519926 -119.821807, 39.519969 -119.821540, 39.520071 -119.811376, 39.520321 -119.810455, 39.505875 -119.803397, 39.505451 -119.826479, 39.505051 -119.832718, 39.505029 -119.841608, 39.505087 -119.842127, 39.505014 -119.845251, 39.504956 -119.845619, 39.502866 -119.851565, 39.502458 -119.852301, 39.502422 -119.852622, 39.502431 -119.853767, 39.502338 -119.854044, 39.501760 -119.855227, 39.501305 -119.855901, 39.500777 -119.856968, 39.500723 -119.857245, 39.500777 -119.858065, 39.501150 -119.858010, 39.501527 -119.857985, 39.501888 -119.858005, 39.502260 -119.858075, 39.502548 -119.858176, 39.503169 -119.858398, 39.503682 -119.858488, 39.507446 -119.858525 ","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response9 = requests.get(url=url, headers=headers,params=querystring9)
    data9 = response9.json()
    if isinstance(data9.get("searchResults"), list) and len(data9["searchResults"]) > 0:
        for result in data9["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring10 = {"polygon":"39.534471 -119.815553, 39.534997 -119.813268, 39.535996 -119.810082, 39.536233 -119.809180, 39.536382 -119.808365, 39.536475 -119.807590, 39.536568 -119.806588, 39.536803 -119.788459, 39.534096 -119.788102, 39.533536 -119.787932, 39.532833 -119.787624, 39.531630 -119.786759, 39.530105 -119.785245, 39.529128 -119.784565, 39.528628 -119.784365, 39.528104 -119.784226, 39.520096 -119.783851, 39.519354 -119.783679, 39.510600 -119.780828, 39.509359 -119.780574, 39.507791 -119.780433, 39.506506 -119.780630, 39.506005 -119.780743, 39.505831 -119.803222, 39.512832 -119.806604, 39.513058 -119.806622, 39.521933 -119.811007, 39.522033 -119.811325, 39.523296 -119.811811, 39.524879 -119.812418, 39.525645 -119.812865, 39.534471 -119.815553","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response10 = requests.get(url=url, headers=headers,params=querystring10)
    data10 = response10.json()
    if isinstance(data10.get("searchResults"), list) and len(data10["searchResults"]) > 0:
        for result in data10["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring11 = {"polygon":"39.534471 -119.815553, 39.534997 -119.813268, 39.535996 -119.810082, 39.536233 -119.809180, 39.536382 -119.808365, 39.536475 -119.807590, 39.536568 -119.806588, 39.536803 -119.788459, 39.534096 -119.788102, 39.533536 -119.787932, 39.532833 -119.787624, 39.531630 -119.786759, 39.530105 -119.785245, 39.529128 -119.784565, 39.528628 -119.784365, 39.528104 -119.784226, 39.520096 -119.783851, 39.519354 -119.783679, 39.510600 -119.780828, 39.509359 -119.780574, 39.507791 -119.780433, 39.506506 -119.780630, 39.506005 -119.780743, 39.505831 -119.803222, 39.512832 -119.806604, 39.513058 -119.806622, 39.521933 -119.811007, 39.522033 -119.811325, 39.523296 -119.811811, 39.524879 -119.812418, 39.525645 -119.812865, 39.534471 -119.815553","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response11 = requests.get(url=url, headers=headers,params=querystring11)
    data11 = response11.json()
    if isinstance(data11.get("searchResults"), list) and len(data11["searchResults"]) > 0:
        for result in data11["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring12 = {"polygon":"39.556160 -119.787923, 39.556129 -119.786328, 39.556221 -119.784733, 39.556437 -119.782619, 39.556529 -119.781822, 39.556898 -119.779349, 39.557236 -119.776080, 39.557328 -119.774843, 39.557359 -119.774046, 39.557267 -119.773089, 39.557236 -119.772650, 39.556990 -119.771414, 39.556744 -119.769819, 39.556406 -119.768104, 39.556252 -119.766629, 39.556191 -119.765512, 39.556160 -119.764754, 39.556252 -119.763199, 39.556375 -119.762003, 39.556314 -119.757297, 39.556129 -119.755303, 39.556206 -119.752597, 39.554590 -119.752671, 39.554488 -119.752514, 39.552870 -119.752673, 39.552541 -119.752673, 39.552117 -119.752686, 39.551353 -119.752741, 39.543918 -119.752796, 39.543939 -119.754571, 39.544056 -119.755107, 39.544258 -119.755644, 39.544438 -119.755878, 39.544809 -119.756290, 39.545276 -119.757005, 39.545467 -119.757803, 39.545520 -119.758340, 39.545509 -119.760141, 39.545551 -119.760444, 39.545530 -119.762012, 39.545562 -119.762260, 39.545530 -119.763896, 39.545498 -119.764172, 39.545509 -119.769302, 39.545530 -119.769508, 39.545583 -119.775120, 39.545530 -119.776165, 39.545530 -119.782726, 39.545551 -119.783222, 39.545551 -119.787719, 39.554371 -119.787637, 39.555106 -119.787685, 39.555718 -119.787857, 39.556160 -119.787923","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response12 = requests.get(url=url, headers=headers,params=querystring12)
    data12 = response12.json()
    if isinstance(data12.get("searchResults"), list) and len(data12["searchResults"]) > 0:
        for result in data12["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring13 = {"polygon":"39.556160 -119.787923, 39.556129 -119.786328, 39.556221 -119.784733, 39.556437 -119.782619, 39.556529 -119.781822, 39.556898 -119.779349, 39.557236 -119.776080, 39.557328 -119.774843, 39.557359 -119.774046, 39.557267 -119.773089, 39.557236 -119.772650, 39.556990 -119.771414, 39.556744 -119.769819, 39.556406 -119.768104, 39.556252 -119.766629, 39.556191 -119.765512, 39.556160 -119.764754, 39.556252 -119.763199, 39.556375 -119.762003, 39.556314 -119.757297, 39.556129 -119.755303, 39.556206 -119.752597, 39.554590 -119.752671, 39.554488 -119.752514, 39.552870 -119.752673, 39.552541 -119.752673, 39.552117 -119.752686, 39.551353 -119.752741, 39.543918 -119.752796, 39.543939 -119.754571, 39.544056 -119.755107, 39.544258 -119.755644, 39.544438 -119.755878, 39.544809 -119.756290, 39.545276 -119.757005, 39.545467 -119.757803, 39.545520 -119.758340, 39.545509 -119.760141, 39.545551 -119.760444, 39.545530 -119.762012, 39.545562 -119.762260, 39.545530 -119.763896, 39.545498 -119.764172, 39.545509 -119.769302, 39.545530 -119.769508, 39.545583 -119.775120, 39.545530 -119.776165, 39.545530 -119.782726, 39.545551 -119.783222, 39.545551 -119.787719, 39.554371 -119.787637, 39.555106 -119.787685, 39.555718 -119.787857, 39.556160 -119.787923","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response13 = requests.get(url=url, headers=headers,params=querystring13)
    data13 = response13.json()
    if isinstance(data13.get("searchResults"), list) and len(data13["searchResults"]) > 0:
        for result in data13["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring14 = {"polygon":"39.550746 -119.822957, 39.550746 -119.822917, 39.550741 -119.822883, 39.550733 -119.822852, 39.550720 -119.822827, 39.550710 -119.822813, 39.550492 -119.822657, 39.550486 -119.822652, 39.549974 -119.822247, 39.549938 -119.822230, 39.549896 -119.822221, 39.549846 -119.822215, 39.549768 -119.822208, 39.549618 -119.822184, 39.549178 -119.822180, 39.549152 -119.822175, 39.549111 -119.822160, 39.549028 -119.822120, 39.548992 -119.822107, 39.548962 -119.822102, 39.547270 -119.822032, 39.547170 -119.822022, 39.546988 -119.821999, 39.546872 -119.821983, 39.534809 -119.817297, 39.534785 -119.817429, 39.532528 -119.822763, 39.532249 -119.823481, 39.532133 -119.823839, 39.531930 -119.824565, 39.531135 -119.827308, 39.531011 -119.827723, 39.530811 -119.828244, 39.530636 -119.828631, 39.530391 -119.829100, 39.530343 -119.829172, 39.528982 -119.831335, 39.528784 -119.831686, 39.528525 -119.832170, 39.528315 -119.832639, 39.527993 -119.833501, 39.527834 -119.834023, 39.527630 -119.834891, 39.527452 -119.836282, 39.526867 -119.851567, 39.526865 -119.851911, 39.526870 -119.852278, 39.526878 -119.852803, 39.526861 -119.853908, 39.526830 -119.854535, 39.526759 -119.855350, 39.526696 -119.855858, 39.526619 -119.856382, 39.526351 -119.857565, 39.526262 -119.857924, 39.526059 -119.858656, 39.525853 -119.859302, 39.525561 -119.860086, 39.525327 -119.860646, 39.524944 -119.861450, 39.524475 -119.862339, 39.525736 -119.862509, 39.525966 -119.862545, 39.526608 -119.862697, 39.526877 -119.862776, 39.527715 -119.863074, 39.528387 -119.863336, 39.528957 -119.863567, 39.530372 -119.864119, 39.530726 -119.864221, 39.531014 -119.864298, 39.531585 -119.864382, 39.532631 -119.864405, 39.535950 -119.864461, 39.536280 -119.864422, 39.536584 -119.864348, 39.536932 -119.864259, 39.537237 -119.864149, 39.537738 -119.863916, 39.538269 -119.863565, 39.539078 -119.862873, 39.539601 -119.862230, 39.539961 -119.861682, 39.540195 -119.861243, 39.540423 -119.860735, 39.542651 -119.855295, 39.542921 -119.854709, 39.543201 -119.854163, 39.563878 -119.853015, 39.544352 -119.852346, 39.544634 -119.851975, 39.544998 -119.851547, 39.548375 -119.848000, 39.548691 -119.847586, 39.548977 -119.847115, 39.549224 -119.846588, 39.549417 -119.846024, 39.549555 -119.845434, 39.549615 -119.844952, 39.550749 -119.831337, 39.550761 -119.830946, 39.550739 -119.830253, 39.550538 -119.825694, 39.550528 -119.825250, 39.550548 -119.824741, 39.550595 -119.824176, 39.550743 -119.822982, 39.550746 -119.822957","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response14 = requests.get(url=url, headers=headers,params=querystring14)
    data14 = response14.json()
    if isinstance(data14.get("searchResults"), list) and len(data14["searchResults"]) > 0:
        for result in data14["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring15 = {"polygon":"39.550746 -119.822957, 39.550746 -119.822917, 39.550741 -119.822883, 39.550733 -119.822852, 39.550720 -119.822827, 39.550710 -119.822813, 39.550492 -119.822657, 39.550486 -119.822652, 39.549974 -119.822247, 39.549938 -119.822230, 39.549896 -119.822221, 39.549846 -119.822215, 39.549768 -119.822208, 39.549618 -119.822184, 39.549178 -119.822180, 39.549152 -119.822175, 39.549111 -119.822160, 39.549028 -119.822120, 39.548992 -119.822107, 39.548962 -119.822102, 39.547270 -119.822032, 39.547170 -119.822022, 39.546988 -119.821999, 39.546872 -119.821983, 39.534809 -119.817297, 39.534785 -119.817429, 39.532528 -119.822763, 39.532249 -119.823481, 39.532133 -119.823839, 39.531930 -119.824565, 39.531135 -119.827308, 39.531011 -119.827723, 39.530811 -119.828244, 39.530636 -119.828631, 39.530391 -119.829100, 39.530343 -119.829172, 39.528982 -119.831335, 39.528784 -119.831686, 39.528525 -119.832170, 39.528315 -119.832639, 39.527993 -119.833501, 39.527834 -119.834023, 39.527630 -119.834891, 39.527452 -119.836282, 39.526867 -119.851567, 39.526865 -119.851911, 39.526870 -119.852278, 39.526878 -119.852803, 39.526861 -119.853908, 39.526830 -119.854535, 39.526759 -119.855350, 39.526696 -119.855858, 39.526619 -119.856382, 39.526351 -119.857565, 39.526262 -119.857924, 39.526059 -119.858656, 39.525853 -119.859302, 39.525561 -119.860086, 39.525327 -119.860646, 39.524944 -119.861450, 39.524475 -119.862339, 39.525736 -119.862509, 39.525966 -119.862545, 39.526608 -119.862697, 39.526877 -119.862776, 39.527715 -119.863074, 39.528387 -119.863336, 39.528957 -119.863567, 39.530372 -119.864119, 39.530726 -119.864221, 39.531014 -119.864298, 39.531585 -119.864382, 39.532631 -119.864405, 39.535950 -119.864461, 39.536280 -119.864422, 39.536584 -119.864348, 39.536932 -119.864259, 39.537237 -119.864149, 39.537738 -119.863916, 39.538269 -119.863565, 39.539078 -119.862873, 39.539601 -119.862230, 39.539961 -119.861682, 39.540195 -119.861243, 39.540423 -119.860735, 39.542651 -119.855295, 39.542921 -119.854709, 39.543201 -119.854163, 39.563878 -119.853015, 39.544352 -119.852346, 39.544634 -119.851975, 39.544998 -119.851547, 39.548375 -119.848000, 39.548691 -119.847586, 39.548977 -119.847115, 39.549224 -119.846588, 39.549417 -119.846024, 39.549555 -119.845434, 39.549615 -119.844952, 39.550749 -119.831337, 39.550761 -119.830946, 39.550739 -119.830253, 39.550538 -119.825694, 39.550528 -119.825250, 39.550548 -119.824741, 39.550595 -119.824176, 39.550743 -119.822982, 39.550746 -119.822957","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response15 = requests.get(url=url, headers=headers,params=querystring15)
    data15 = response15.json()
    if isinstance(data15.get("searchResults"), list) and len(data15["searchResults"]) > 0:
        for result in data15["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring16 = {"polygon":"39.550746 -119.822957, 39.550746 -119.822917, 39.550741 -119.822883, 39.550733 -119.822852, 39.550720 -119.822827, 39.550710 -119.822813, 39.550492 -119.822657, 39.550486 -119.822652, 39.549974 -119.822247, 39.549938 -119.822230, 39.549896 -119.822221, 39.549846 -119.822215, 39.549768 -119.822208, 39.549618 -119.822184, 39.549178 -119.822180, 39.549152 -119.822175, 39.549111 -119.822160, 39.549028 -119.822120, 39.548992 -119.822107, 39.548962 -119.822102, 39.547270 -119.822032, 39.547170 -119.822022, 39.546988 -119.821999, 39.546872 -119.821983, 39.534809 -119.817297, 39.534785 -119.817429, 39.532528 -119.822763, 39.532249 -119.823481, 39.532133 -119.823839, 39.531930 -119.824565, 39.531135 -119.827308, 39.531011 -119.827723, 39.530811 -119.828244, 39.530636 -119.828631, 39.530391 -119.829100, 39.530343 -119.829172, 39.528982 -119.831335, 39.528784 -119.831686, 39.528525 -119.832170, 39.528315 -119.832639, 39.527993 -119.833501, 39.527834 -119.834023, 39.527630 -119.834891, 39.527452 -119.836282, 39.526867 -119.851567, 39.526865 -119.851911, 39.526870 -119.852278, 39.526878 -119.852803, 39.526861 -119.853908, 39.526830 -119.854535, 39.526759 -119.855350, 39.526696 -119.855858, 39.526619 -119.856382, 39.526351 -119.857565, 39.526262 -119.857924, 39.526059 -119.858656, 39.525853 -119.859302, 39.525561 -119.860086, 39.525327 -119.860646, 39.524944 -119.861450, 39.524475 -119.862339, 39.525736 -119.862509, 39.525966 -119.862545, 39.526608 -119.862697, 39.526877 -119.862776, 39.527715 -119.863074, 39.528387 -119.863336, 39.528957 -119.863567, 39.530372 -119.864119, 39.530726 -119.864221, 39.531014 -119.864298, 39.531585 -119.864382, 39.532631 -119.864405, 39.535950 -119.864461, 39.536280 -119.864422, 39.536584 -119.864348, 39.536932 -119.864259, 39.537237 -119.864149, 39.537738 -119.863916, 39.538269 -119.863565, 39.539078 -119.862873, 39.539601 -119.862230, 39.539961 -119.861682, 39.540195 -119.861243, 39.540423 -119.860735, 39.542651 -119.855295, 39.542921 -119.854709, 39.543201 -119.854163, 39.563878 -119.853015, 39.544352 -119.852346, 39.544634 -119.851975, 39.544998 -119.851547, 39.548375 -119.848000, 39.548691 -119.847586, 39.548977 -119.847115, 39.549224 -119.846588, 39.549417 -119.846024, 39.549555 -119.845434, 39.549615 -119.844952, 39.550749 -119.831337, 39.550761 -119.830946, 39.550739 -119.830253, 39.550538 -119.825694, 39.550528 -119.825250, 39.550548 -119.824741, 39.550595 -119.824176, 39.550743 -119.822982, 39.550746 -119.822957","page":"4","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response16 = requests.get(url=url, headers=headers,params=querystring16)
    data16 = response16.json()
    if isinstance(data16.get("searchResults"), list) and len(data16["searchResults"]) > 0:
        for result in data16["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring17 = {"polygon":"39.545313 -119.787734, 39.545374 -119.758222, 39.545330 -119.757821, 39.545253 -119.757377, 39.545054 -119.756920, 39.544790 -119.756490, 39.544481 -119.756147, 39.544205 -119.755761, 39.544028 -119.755389, 39.543874 -119.754931, 39.543808 -119.754473, 39.543808 -119.752785, 39.541513 -119.752842, 39.541314 -119.752913, 39.540310 -119.752971, 39.539990 -119.753028, 39.534179 -119.753084, 39.534157 -119.771783, 39.534212 -119.772726, 39.534608 -119.775755, 39.534917 -119.777240, 39.535159 -119.777855, 39.536459 -119.780569, 39.536834 -119.781526, 39.537131 -119.782454, 39.537318 -119.783383, 39.537462 -119.784426, 39.537528 -119.785483, 39.537506 -119.786454, 39.537462 -119.786416, 39.537346 -119.787854, 39.545313 -119.787734","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response17 = requests.get(url=url, headers=headers,params=querystring17)
    data17 = response17.json()
    if isinstance(data17.get("searchResults"), list) and len(data17["searchResults"]) > 0:
        for result in data17["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring18 = {"polygon":"39.545313 -119.787734, 39.545374 -119.758222, 39.545330 -119.757821, 39.545253 -119.757377, 39.545054 -119.756920, 39.544790 -119.756490, 39.544481 -119.756147, 39.544205 -119.755761, 39.544028 -119.755389, 39.543874 -119.754931, 39.543808 -119.754473, 39.543808 -119.752785, 39.541513 -119.752842, 39.541314 -119.752913, 39.540310 -119.752971, 39.539990 -119.753028, 39.534179 -119.753084, 39.534157 -119.771783, 39.534212 -119.772726, 39.534608 -119.775755, 39.534917 -119.777240, 39.535159 -119.777855, 39.536459 -119.780569, 39.536834 -119.781526, 39.537131 -119.782454, 39.537318 -119.783383, 39.537462 -119.784426, 39.537528 -119.785483, 39.537506 -119.786454, 39.537462 -119.786416, 39.537346 -119.787854, 39.545313 -119.787734","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response18 = requests.get(url=url, headers=headers,params=querystring18)
    data18 = response18.json()
    if isinstance(data18.get("searchResults"), list) and len(data18["searchResults"]) > 0:
        for result in data18["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })

    querystring19 = {"polygon":"39.556213 -119.752208, 39.556250 -119.748393, 39.552809 -119.748436, 39.552817 -119.752535, 39.556213 -119.752208","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response19 = requests.get(url=url, headers=headers,params=querystring19)
    data19 = response19.json()
    if isinstance(data19.get("searchResults"), list) and len(data19["searchResults"]) > 0:
        for result in data19["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })

    querystring20 = {"polygon":"39.556246 -119.748338, 39.556230 -119.740445, 39.555530 -119.740457, 39.553610 -119.739861, 39.553407 -119.739773, 39.552785 -119.739765, 39.552819 -119.748415, 39.556246 -119.748338","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response20 = requests.get(url=url, headers=headers,params=querystring20)
    data20 = response20.json()
    if isinstance(data20.get("searchResults"), list) and len(data20["searchResults"]) > 0:
        for result in data20["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })

    querystring21 = {"polygon":"39.552804 -119.739694, 39.553426 -119.739719, 39.553656 -119.739837, 39.555450 -119.740379, 39.556232 -119.740395, 39.556257 -119.738036, 39.556196 -119.737494, 39.556075 -119.736983, 39.555741 -119.736102, 39.555450 -119.735670, 39.554578 -119.734632, 39.554062 -119.734254, 39.553444 -119.734003, 39.552789 -119.733964, 39.552804 -119.739694","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response21 = requests.get(url=url, headers=headers,params=querystring21)
    data21 = response21.json()
    if isinstance(data21.get("searchResults"), list) and len(data21["searchResults"]) > 0:
        for result in data21["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring22 = {"polygon":"39.552765 -119.752486, 39.552737 -119.734072, 39.541943 -119.733903, 39.541994 -119.743872, 39.541977 -119.744173, 39.541865 -119.744982, 39.540388 -119.752658, 39.552765 -119.752486","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response22 = requests.get(url=url, headers=headers,params=querystring22)
    data22 = response22.json()
    if isinstance(data22.get("searchResults"), list) and len(data22["searchResults"]) > 0:
        for result in data22["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring23 = {"polygon":"39.552765 -119.752486, 39.552737 -119.734072, 39.541943 -119.733903, 39.541994 -119.743872, 39.541977 -119.744173, 39.541865 -119.744982, 39.540388 -119.752658, 39.552765 -119.752486","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response23 = requests.get(url=url, headers=headers,params=querystring23)
    data23 = response23.json()
    if isinstance(data23.get("searchResults"), list) and len(data23["searchResults"]) > 0:
        for result in data23["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring24 = {"polygon":"39.545269 -119.761853, 39.545335 -119.758250, 39.545309 -119.757778, 39.545217 -119.757357, 39.545061 -119.756969, 39.544814 -119.756547, 39.544333 -119.756008, 39.544125 -119.755704, 39.543891 -119.755165, 39.543800 -119.754440, 39.543761 -119.752821, 39.540305 -119.753021, 39.538606 -119.761974, 39.545269 -119.761853","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response24 = requests.get(url=url, headers=headers,params=querystring24)
    data24 = response24.json()
    if isinstance(data24.get("searchResults"), list) and len(data24["searchResults"]) > 0:
        for result in data24["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring25 = {"polygon":"39.543926 -119.762190, 39.543757 -119.762000, 39.538570 -119.762047, 39.537953 -119.765344, 39.538876 -119.765351, 39.538990 -119.765428, 39.542129 -119.765386, 39.542349 -119.765301, 39.542502 -119.765178, 39.543483 -119.764073, 39.543537 -119.763933, 39.543717 -119.763702, 39.543792 -119.763493, 39.543825 -119.763316, 39.543841 -119.762650, 39.543858 -119.762463, 39.543924 -119.762253, 39.543926 -119.762190","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response25 = requests.get(url=url, headers=headers,params=querystring25)
    data25 = response25.json()
    if isinstance(data25.get("searchResults"), list) and len(data25["searchResults"]) > 0:
        for result in data25["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring25 = {"polygon":"39.545392 -119.771389, 39.545373 -119.769445, 39.545419 -119.769266, 39.545407 -119.764129, 39.545367 -119.763882, 39.545337 -119.762154, 39.544417 -119.762145, 39.544272 -119.762222, 39.544108 -119.762410, 39.544042 -119.762614, 39.544016 -119.763331, 39.543930 -119.763672, 39.543851 -119.763842, 39.543647 -119.764132, 39.543542 -119.764149, 39.542556 -119.765266, 39.542267 -119.765428, 39.542063 -119.765479, 39.539005 -119.765496, 39.538867 -119.765556, 39.537907 -119.765560, 39.536815 -119.771362, 39.536881 -119.771393, 39.545392 -119.771389","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response25 = requests.get(url=url, headers=headers,params=querystring25)
    data25 = response25.json()
    if isinstance(data25.get("searchResults"), list) and len(data25["searchResults"]) > 0:
        for result in data25["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring26 = {"polygon":"39.535523 -119.777752, 39.535801 -119.776089, 39.535879 -119.775920, 39.540194 -119.753000, 39.534938 -119.753100, 39.534934 -119.753623, 39.534784 -119.754261, 39.534744 -119.755583, 39.534664 -119.756235, 39.534923 -119.758545, 39.534904 -119.759060, 39.534835 -119.759442, 39.534806 -119.760184, 39.534846 -119.761228, 39.534923 -119.761497, 39.535221 -119.762134, 39.535287 -119.762404, 39.535305 -119.763807, 39.535248 -119.763955, 39.535292 -119.773246, 39.535322 -119.773411, 39.535415 -119.774908, 39.535597 -119.775526, 39.535669 -119.776008, 39.535523 -119.777752","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response26 = requests.get(url=url, headers=headers,params=querystring26)
    data26 = response26.json()
    if isinstance(data26.get("searchResults"), list) and len(data26["searchResults"]) > 0:
        for result in data26["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring27 = {"polygon":"39.53471 -119.743365, 39.541902 -119.74319, 39.541822 -119.734695, 39.541768 -119.734596, 39.541759 -119.733896, 39.540692 -119.733964, 39.539594 -119.734304, 39.539251 -119.734502, 39.533548 -119.73873, 39.534103 -119.740041, 39.53432 -119.740906, 39.534531 -119.742144, 39.534596 -119.743367, 39.53471 -119.743365","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response27 = requests.get(url=url, headers=headers,params=querystring27)
    data27 = response27.json()
    if isinstance(data27.get("searchResults"), list) and len(data27["searchResults"]) > 0:
        for result in data27["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring28 = {"polygon":"39.541882 -119.743296, 39.541927 -119.744349, 39.540287 -119.752741, 39.534853 -119.752811, 39.534845 -119.743387, 39.541882 -119.743296","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response28 = requests.get(url=url, headers=headers,params=querystring28)
    data28 = response28.json()
    if isinstance(data28.get("searchResults"), list) and len(data28["searchResults"]) > 0:
        for result in data28["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring29 = {"polygon":"39.535144 -119.774683, 39.53027 -119.775124, 39.530275 -119.766419, 39.535168 -119.765562, 39.535144 -119.774683","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response29 = requests.get(url=url, headers=headers,params=querystring29)
    data29 = response29.json()
    if isinstance(data29.get("searchResults"), list) and len(data29["searchResults"]) > 0:
        for result in data29["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring30 = {"polygon":"39.530279 -119.775207, 39.53521 -119.774195, 39.540819 -119.787783, 39.530051 -119.786807, 39.530279 -119.775207","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response30 = requests.get(url=url, headers=headers,params=querystring30)
    data30 = response30.json()
    if isinstance(data30.get("searchResults"), list) and len(data30["searchResults"]) > 0:
        for result in data30["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring31 = {"polygon":"39.530093 -119.785178, 39.527459 -119.785230, 39.527579 -119.766774, 39.530729 -119.766209, 39.530093 -119.785178","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response31 = requests.get(url=url, headers=headers,params=querystring31)
    data31 = response31.json()
    if isinstance(data31.get("searchResults"), list) and len(data31["searchResults"]) > 0:
        for result in data31["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring32 = {"polygon":"39.527505 -119.783692, 39.519754 -119.783305, 39.517579 -119.777349, 39.521578 -119.771370, 39.527628 -119.777690, 39.527505 -119.783692","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response32 = requests.get(url=url, headers=headers,params=querystring32)
    data32 = response32.json()
    if isinstance(data32.get("searchResults"), list) and len(data32["searchResults"]) > 0:
        for result in data32["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring33 = {"polygon":"39.519662 -119.783213, 39.517536 -119.777389, 39.517241 -119.773434, 39.517359 -119.771367, 39.515902 -119.761747, 39.511572 -119.744633, 39.505405 -119.747963, 39.484143 -119.748144, 39.480914 -119.749918, 39.476843 -119.762694, 39.476913 -119.790838, 39.483816 -119.786508, 39.500103 -119.783449, 39.507335 -119.780129, 39.519662 -119.783213","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response33 = requests.get(url=url, headers=headers,params=querystring33)
    data33 = response33.json()
    if isinstance(data33.get("searchResults"), list) and len(data33["searchResults"]) > 0:
        for result in data33["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring34 = {"polygon":"39.519662 -119.783213, 39.517536 -119.777389, 39.517241 -119.773434, 39.517359 -119.771367, 39.515902 -119.761747, 39.511572 -119.744633, 39.505405 -119.747963, 39.484143 -119.748144, 39.480914 -119.749918, 39.476843 -119.762694, 39.476913 -119.790838, 39.483816 -119.786508, 39.500103 -119.783449, 39.507335 -119.780129, 39.519662 -119.783213","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response34 = requests.get(url=url, headers=headers,params=querystring34)
    data34 = response34.json()
    if isinstance(data34.get("searchResults"), list) and len(data34["searchResults"]) > 0:
        for result in data34["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring35 = {"polygon":"39.519662 -119.783213, 39.517536 -119.777389, 39.517241 -119.773434, 39.517359 -119.771367, 39.515902 -119.761747, 39.511572 -119.744633, 39.505405 -119.747963, 39.484143 -119.748144, 39.480914 -119.749918, 39.476843 -119.762694, 39.476913 -119.790838, 39.483816 -119.786508, 39.500103 -119.783449, 39.507335 -119.780129, 39.519662 -119.783213","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response35 = requests.get(url=url, headers=headers,params=querystring35)
    data35 = response35.json()
    if isinstance(data35.get("searchResults"), list) and len(data35["searchResults"]) > 0:
        for result in data35["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring36 = {"polygon":"39.521773 -119.771296, 39.527630 -119.778025, 39.527438 -119.752756, 39.534956 -119.752887, 39.534497 -119.737802, 39.531292 -119.739724, 39.521707 -119.740171, 39.517542 -119.740616, 39.511516 -119.744497, 39.515933 -119.761738, 39.517541 -119.777324, 39.521773 -119.771296","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response36 = requests.get(url=url, headers=headers,params=querystring36)
    data36 = response36.json()
    if isinstance(data36.get("searchResults"), list) and len(data36["searchResults"]) > 0:
        for result in data36["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring37 = {"polygon":"39.500708 -119.858177, 39.502384 -119.853858, 39.502425 -119.852313, 39.504967 -119.845489, 39.505066 -119.832014, 39.505397 -119.826478,  39.505650 -119.812600, 39.476534 -119.811816, 39.477875 -119.825304, 39.477659 -119.830003, 39.476036 -119.833007, 39.474446 -119.834788, 39.473949 -119.837148, 39.476152 -119.843028, 39.478173 -119.845495, 39.479895 -119.846740, 39.480922 -119.848950, 39.486851 -119.854744, 39.487282 -119.856503, 39.487050 -119.858370, 39.486238 -119.861825, 39.486785 -119.863413, 39.488490 -119.864722, 39.490130 -119.864400, 39.495975 -119.859400, 39.500708 -119.858177","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response37 = requests.get(url=url, headers=headers,params=querystring37)
    data37 = response37.json()
    if isinstance(data37.get("searchResults"), list) and len(data37["searchResults"]) > 0:
        for result in data37["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring38 = {"polygon":"39.500708 -119.858177, 39.502384 -119.853858, 39.502425 -119.852313, 39.504967 -119.845489, 39.505066 -119.832014, 39.505397 -119.826478,  39.505650 -119.812600, 39.476534 -119.811816, 39.477875 -119.825304, 39.477659 -119.830003, 39.476036 -119.833007, 39.474446 -119.834788, 39.473949 -119.837148, 39.476152 -119.843028, 39.478173 -119.845495, 39.479895 -119.846740, 39.480922 -119.848950, 39.486851 -119.854744, 39.487282 -119.856503, 39.487050 -119.858370, 39.486238 -119.861825, 39.486785 -119.863413, 39.488490 -119.864722, 39.490130 -119.864400, 39.495975 -119.859400, 39.500708 -119.858177","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response38 = requests.get(url=url, headers=headers,params=querystring38)
    data38 = response38.json()
    if isinstance(data38.get("searchResults"), list) and len(data38["searchResults"]) > 0:
        for result in data38["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring39 = {"polygon":"39.500708 -119.858177, 39.502384 -119.853858, 39.502425 -119.852313, 39.504967 -119.845489, 39.505066 -119.832014, 39.505397 -119.826478,  39.505650 -119.812600, 39.476534 -119.811816, 39.477875 -119.825304, 39.477659 -119.830003, 39.476036 -119.833007, 39.474446 -119.834788, 39.473949 -119.837148, 39.476152 -119.843028, 39.478173 -119.845495, 39.479895 -119.846740, 39.480922 -119.848950, 39.486851 -119.854744, 39.487282 -119.856503, 39.487050 -119.858370, 39.486238 -119.861825, 39.486785 -119.863413, 39.488490 -119.864722, 39.490130 -119.864400, 39.495975 -119.859400, 39.500708 -119.858177","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response39 = requests.get(url=url, headers=headers,params=querystring39)
    data39 = response39.json()
    if isinstance(data39.get("searchResults"), list) and len(data39["searchResults"]) > 0:
        for result in data39["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring40 = {"polygon":"39.505650 -119.812600, 39.505795 -119.780773, 39.500364 -119.783305, 39.496076 -119.784292, 39.484186 -119.786300, 39.481387 -119.787781, 39.476949 -119.790892, 39.476684 -119.807029, 39.476402 -119.809239, 39.476534 -119.811816, 39.505650 -119.812600","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response40 = requests.get(url=url, headers=headers,params=querystring40)
    data40 = response40.json()
    if isinstance(data40.get("searchResults"), list) and len(data40["searchResults"]) > 0:
        for result in data40["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring41 = {"polygon":"39.505650 -119.812600, 39.505795 -119.780773, 39.500364 -119.783305, 39.496076 -119.784292, 39.484186 -119.786300, 39.481387 -119.787781, 39.476949 -119.790892, 39.476684 -119.807029, 39.476402 -119.809239, 39.476534 -119.811816, 39.505650 -119.812600","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response41 = requests.get(url=url, headers=headers,params=querystring41)
    data41 = response41.json()
    if isinstance(data41.get("searchResults"), list) and len(data41["searchResults"]) > 0:
        for result in data41["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring42 = {"polygon":"39.550039 -119.843832, 39.550076 -119.898315, 39.514064 -119.900203, 39.518555 -119.873470, 39.524303 -119.862650, 39.536506 -119.864385, 39.539812 -119.862344, 39.543826 -119.853566, 39.550039 -119.843832","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response42 = requests.get(url=url, headers=headers,params=querystring42)
    data42 = response42.json()
    if isinstance(data42.get("searchResults"), list) and len(data42["searchResults"]) > 0:
        for result in data42["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring43 = {"polygon":"39.550039 -119.843832, 39.550076 -119.898315, 39.514064 -119.900203, 39.518555 -119.873470, 39.524303 -119.862650, 39.536506 -119.864385, 39.539812 -119.862344, 39.543826 -119.853566, 39.550039 -119.843832","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response43 = requests.get(url=url, headers=headers,params=querystring43)
    data43 = response43.json()
    if isinstance(data43.get("searchResults"), list) and len(data43["searchResults"]) > 0:
        for result in data43["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring44 = {"polygon":"39.550039 -119.843832, 39.550076 -119.898315, 39.514064 -119.900203, 39.518555 -119.873470, 39.524303 -119.862650, 39.536506 -119.864385, 39.539812 -119.862344, 39.543826 -119.853566, 39.550039 -119.843832","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response44 = requests.get(url=url, headers=headers,params=querystring44)
    data44 = response44.json()
    if isinstance(data44.get("searchResults"), list) and len(data44["searchResults"]) > 0:
        for result in data44["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring45 = {"polygon":"39.550039 -119.843832, 39.550076 -119.898315, 39.514064 -119.900203, 39.518555 -119.873470, 39.524303 -119.862650, 39.536506 -119.864385, 39.539812 -119.862344, 39.543826 -119.853566, 39.550039 -119.843832","page":"4","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response45 = requests.get(url=url, headers=headers,params=querystring45)
    data45 = response45.json()
    if isinstance(data45.get("searchResults"), list) and len(data45["searchResults"]) > 0:
        for result in data45["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring45 = {"polygon":"39.513669 -119.900602, 39.486581 -119.900774, 39.486722 -120.002408, 39.512614 -120.002404, 39.514549 -119.983228, 39.514019 -119.977821, 39.510377 -119.96117, 39.512133 -119.949564, 39.509848 -119.938253, 39.516271 -119.921945, 39.513357 -119.906667, 39.513669 -119.900602","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response45 = requests.get(url=url, headers=headers,params=querystring45)
    data45 = response45.json()
    if isinstance(data45.get("searchResults"), list) and len(data45["searchResults"]) > 0:
        for result in data45["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring46 = {"polygon":"39.509628 -119.938322, 39.556075 -119.939139, 39.555288 -120.001810, 39.512148 -120.002014, 39.514195 -119.984364, 39.510262 -119.961544, 39.512042 -119.948799, 39.509628 -119.938322","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response46 = requests.get(url=url, headers=headers,params=querystring46)
    data46 = response46.json()
    if isinstance(data46.get("searchResults"), list) and len(data46["searchResults"]) > 0:
        for result in data46["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring47 = {"polygon":"39.509628 -119.938322, 39.556075 -119.939139, 39.555288 -120.001810, 39.512148 -120.002014, 39.514195 -119.984364, 39.510262 -119.961544, 39.512042 -119.948799, 39.509628 -119.938322","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response47 = requests.get(url=url, headers=headers,params=querystring47)
    data47 = response47.json()
    if isinstance(data47.get("searchResults"), list) and len(data47["searchResults"]) > 0:
        for result in data47["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring48 = {"polygon":"39.509628 -119.938322, 39.556075 -119.939139, 39.555288 -120.001810, 39.512148 -120.002014, 39.514195 -119.984364, 39.510262 -119.961544, 39.512042 -119.948799, 39.509628 -119.938322","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response48 = requests.get(url=url, headers=headers,params=querystring48)
    data48 = response48.json()
    if isinstance(data48.get("searchResults"), list) and len(data48["searchResults"]) > 0:
        for result in data48["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring49 = {"polygon":"39.509628 -119.938322, 39.556075 -119.939139, 39.555288 -120.001810, 39.512148 -120.002014, 39.514195 -119.984364, 39.510262 -119.961544, 39.512042 -119.948799, 39.509628 -119.938322","page":"4","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response49 = requests.get(url=url, headers=headers,params=querystring49)
    data49 = response49.json()
    if isinstance(data49.get("searchResults"), list) and len(data49["searchResults"]) > 0:
        for result in data49["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring50 = {"polygon":"39.509661 -119.938383, 39.553425 -119.941186, 39.554369 -119.910131, 39.513592 -119.908350, 39.516254 -119.921484, 39.509661 -119.938383","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response50 = requests.get(url=url, headers=headers,params=querystring50)
    data50 = response50.json()
    if isinstance(data50.get("searchResults"), list) and len(data50["searchResults"]) > 0:
        for result in data50["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring51 = {"polygon":"39.509661 -119.938383, 39.553425 -119.941186, 39.554369 -119.910131, 39.513592 -119.908350, 39.516254 -119.921484, 39.509661 -119.938383","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response51 = requests.get(url=url, headers=headers,params=querystring51)
    data51 = response51.json()
    if isinstance(data51.get("searchResults"), list) and len(data51["searchResults"]) > 0:
        for result in data51["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring52 = {"polygon":"39.493645 -119.748073, 39.489683 -119.743561, 39.498071 -119.729526, 39.498240 -119.714448, 39.476262 -119.715060, 39.476631 -119.733670, 39.465855 -119.723775, 39.450409 -119.727858, 39.452143 -119.731737, 39.451827 -119.737759, 39.443709 -119.745516, 39.438676 -119.758564, 39.439004 -119.765240, 39.445847 -119.769731, 39.451865 -119.779357, 39.454094 -119.781522, 39.475546 -119.791266, 39.476995 -119.790688, 39.476939 -119.762540, 39.481395 -119.749477, 39.484181 -119.748033, 39.493645 -119.748073","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response52 = requests.get(url=url, headers=headers,params=querystring52)
    data52 = response52.json()
    if isinstance(data52.get("searchResults"), list) and len(data52["searchResults"]) > 0:
        for result in data52["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring53 = {"polygon":"39.493645 -119.748073, 39.489683 -119.743561, 39.498071 -119.729526, 39.498240 -119.714448, 39.476262 -119.715060, 39.476631 -119.733670, 39.465855 -119.723775, 39.450409 -119.727858, 39.452143 -119.731737, 39.451827 -119.737759, 39.443709 -119.745516, 39.438676 -119.758564, 39.439004 -119.765240, 39.445847 -119.769731, 39.451865 -119.779357, 39.454094 -119.781522, 39.475546 -119.791266, 39.476995 -119.790688, 39.476939 -119.762540, 39.481395 -119.749477, 39.484181 -119.748033, 39.493645 -119.748073","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response53 = requests.get(url=url, headers=headers,params=querystring53)
    data53 = response53.json()
    if isinstance(data53.get("searchResults"), list) and len(data53["searchResults"]) > 0:
        for result in data53["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring54 = {"polygon":"39.493645 -119.748073, 39.489683 -119.743561, 39.498071 -119.729526, 39.498240 -119.714448, 39.476262 -119.715060, 39.476631 -119.733670, 39.465855 -119.723775, 39.450409 -119.727858, 39.452143 -119.731737, 39.451827 -119.737759, 39.443709 -119.745516, 39.438676 -119.758564, 39.439004 -119.765240, 39.445847 -119.769731, 39.451865 -119.779357, 39.454094 -119.781522, 39.475546 -119.791266, 39.476995 -119.790688, 39.476939 -119.762540, 39.481395 -119.749477, 39.484181 -119.748033, 39.493645 -119.748073","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response54 = requests.get(url=url, headers=headers,params=querystring54)
    data54 = response54.json()
    if isinstance(data54.get("searchResults"), list) and len(data54["searchResults"]) > 0:
        for result in data54["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring55 = {"polygon":"39.493645 -119.748073, 39.489683 -119.743561, 39.498071 -119.729526, 39.498240 -119.714448, 39.476262 -119.715060, 39.476631 -119.733670, 39.465855 -119.723775, 39.450409 -119.727858, 39.452143 -119.731737, 39.451827 -119.737759, 39.443709 -119.745516, 39.438676 -119.758564, 39.439004 -119.765240, 39.445847 -119.769731, 39.451865 -119.779357, 39.454094 -119.781522, 39.475546 -119.791266, 39.476995 -119.790688, 39.476939 -119.762540, 39.481395 -119.749477, 39.484181 -119.748033, 39.493645 -119.748073","page":"4","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response55 = requests.get(url=url, headers=headers,params=querystring55)
    data55 = response55.json()
    if isinstance(data55.get("searchResults"), list) and len(data55["searchResults"]) > 0:
        for result in data55["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring56 = {"polygon":"39.438959 -119.765182, 39.424770 -119.754261, 39.421591 -119.749375, 39.416822 -119.746803, 39.412451 -119.747574, 39.409073 -119.750146, 39.402813 -119.746031, 39.403011 -119.739344, 39.406086 -119.734398, 39.407798 -119.733760, 39.416472 -119.733154, 39.423111 -119.733161, 39.450400 -119.727658, 39.452301 -119.733617, 39.452104 -119.737189, 39.442764 -119.746478, 39.438758 -119.758493, 39.438959 -119.765182","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response56 = requests.get(url=url, headers=headers,params=querystring56)
    data56 = response56.json()
    if isinstance(data56.get("searchResults"), list) and len(data56["searchResults"]) > 0:
        for result in data56["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring57 = {"polygon":"39.438959 -119.765182, 39.424770 -119.754261, 39.421591 -119.749375, 39.416822 -119.746803, 39.412451 -119.747574, 39.409073 -119.750146, 39.402813 -119.746031, 39.403011 -119.739344, 39.406086 -119.734398, 39.407798 -119.733760, 39.416472 -119.733154, 39.423111 -119.733161, 39.450400 -119.727658, 39.452301 -119.733617, 39.452104 -119.737189, 39.442764 -119.746478, 39.438758 -119.758493, 39.438959 -119.765182","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response57 = requests.get(url=url, headers=headers,params=querystring57)
    data57 = response57.json()
    if isinstance(data57.get("searchResults"), list) and len(data57["searchResults"]) > 0:
        for result in data57["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring58 = {"polygon":"39.438959 -119.765182, 39.424770 -119.754261, 39.421591 -119.749375, 39.416822 -119.746803, 39.412451 -119.747574, 39.409073 -119.750146, 39.402813 -119.746031, 39.403011 -119.739344, 39.406086 -119.734398, 39.407798 -119.733760, 39.416472 -119.733154, 39.423111 -119.733161, 39.450400 -119.727658, 39.452301 -119.733617, 39.452104 -119.737189, 39.442764 -119.746478, 39.438758 -119.758493, 39.438959 -119.765182","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response58 = requests.get(url=url, headers=headers,params=querystring58)
    data58 = response58.json()
    if isinstance(data58.get("searchResults"), list) and len(data58["searchResults"]) > 0:
        for result in data58["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring59 = {"polygon":"39.438959 -119.765182, 39.424770 -119.754261, 39.421591 -119.749375, 39.416822 -119.746803, 39.412451 -119.747574, 39.409073 -119.750146, 39.402813 -119.746031, 39.403011 -119.739344, 39.406086 -119.734398, 39.407798 -119.733760, 39.416472 -119.733154, 39.423111 -119.733161, 39.450400 -119.727658, 39.452301 -119.733617, 39.452104 -119.737189, 39.442764 -119.746478, 39.438758 -119.758493, 39.438959 -119.765182","page":"4","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response59 = requests.get(url=url, headers=headers,params=querystring59)
    data59 = response59.json()
    if isinstance(data59.get("searchResults"), list) and len(data59["searchResults"]) > 0:
        for result in data59["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring60 = {"polygon":"39.474099 -119.835259, 39.465033 -119.833338, 39.469751 -119.807876, 39.404492 -119.804708, 39.404580 -119.790845, 39.391831 -119.790616, 39.391771 -119.769230, 39.396866 -119.758133, 39.406058 -119.754431, 39.412388 -119.747634, 39.417405 -119.747027, 39.421109 -119.749030, 39.426970 -119.756373, 39.446813 -119.770899, 39.453434 -119.781004, 39.476948 -119.790684, 39.476667 -119.811076, 39.477698 -119.829647, 39.474099 -119.835259","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response60 = requests.get(url=url, headers=headers,params=querystring60)
    data60 = response60.json()
    if isinstance(data60.get("searchResults"), list) and len(data60["searchResults"]) > 0:
        for result in data60["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring61 = {"polygon":"39.474099 -119.835259, 39.465033 -119.833338, 39.469751 -119.807876, 39.404492 -119.804708, 39.404580 -119.790845, 39.391831 -119.790616, 39.391771 -119.769230, 39.396866 -119.758133, 39.406058 -119.754431, 39.412388 -119.747634, 39.417405 -119.747027, 39.421109 -119.749030, 39.426970 -119.756373, 39.446813 -119.770899, 39.453434 -119.781004, 39.476948 -119.790684, 39.476667 -119.811076, 39.477698 -119.829647, 39.474099 -119.835259","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response61 = requests.get(url=url, headers=headers,params=querystring61)
    data61 = response61.json()
    if isinstance(data61.get("searchResults"), list) and len(data61["searchResults"]) > 0:
        for result in data61["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring62 = {"polygon":"39.474099 -119.835259, 39.465033 -119.833338, 39.469751 -119.807876, 39.404492 -119.804708, 39.404580 -119.790845, 39.391831 -119.790616, 39.391771 -119.769230, 39.396866 -119.758133, 39.406058 -119.754431, 39.412388 -119.747634, 39.417405 -119.747027, 39.421109 -119.749030, 39.426970 -119.756373, 39.446813 -119.770899, 39.453434 -119.781004, 39.476948 -119.790684, 39.476667 -119.811076, 39.477698 -119.829647, 39.474099 -119.835259","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response62 = requests.get(url=url, headers=headers,params=querystring62)
    data62 = response62.json()
    if isinstance(data62.get("searchResults"), list) and len(data62["searchResults"]) > 0:
        for result in data62["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring63 = {"polygon":"39.474099 -119.835259, 39.465033 -119.833338, 39.469751 -119.807876, 39.404492 -119.804708, 39.404580 -119.790845, 39.391831 -119.790616, 39.391771 -119.769230, 39.396866 -119.758133, 39.406058 -119.754431, 39.412388 -119.747634, 39.417405 -119.747027, 39.421109 -119.749030, 39.426970 -119.756373, 39.446813 -119.770899, 39.453434 -119.781004, 39.476948 -119.790684, 39.476667 -119.811076, 39.477698 -119.829647, 39.474099 -119.835259","page":"4","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response63 = requests.get(url=url, headers=headers,params=querystring63)
    data63 = response63.json()
    if isinstance(data63.get("searchResults"), list) and len(data63["searchResults"]) > 0:
        for result in data63["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring64 = {"polygon":"39.474099 -119.835259, 39.465033 -119.833338, 39.469751 -119.807876, 39.404492 -119.804708, 39.404580 -119.790845, 39.391831 -119.790616, 39.391771 -119.769230, 39.396866 -119.758133, 39.406058 -119.754431, 39.412388 -119.747634, 39.417405 -119.747027, 39.421109 -119.749030, 39.426970 -119.756373, 39.446813 -119.770899, 39.453434 -119.781004, 39.476948 -119.790684, 39.476667 -119.811076, 39.477698 -119.829647, 39.474099 -119.835259","page":"5","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response64 = requests.get(url=url, headers=headers,params=querystring64)
    data64 = response64.json()
    if isinstance(data64.get("searchResults"), list) and len(data64["searchResults"]) > 0:
        for result in data64["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring65 = {"polygon":"39.557664 -119.773789, 39.565010 -119.773971, 39.566554 -119.775549, 39.570296 -119.780829, 39.570406 -119.785615, 39.602400 -119.808737, 39.605653 -119.809891, 39.607710 -119.813500, 39.607515 -119.832518, 39.602900 -119.836993, 39.597506 -119.839158, 39.573140 -119.848973, 39.549214 -119.847529, 39.552775 -119.806101, 39.556281 -119.800832, 39.557664 -119.773789","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response65 = requests.get(url=url, headers=headers,params=querystring65)
    data65 = response65.json()
    if isinstance(data65.get("searchResults"), list) and len(data65["searchResults"]) > 0:
        for result in data65["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring66 = {"polygon":"39.557664 -119.773789, 39.565010 -119.773971, 39.566554 -119.775549, 39.570296 -119.780829, 39.570406 -119.785615, 39.602400 -119.808737, 39.605653 -119.809891, 39.607710 -119.813500, 39.607515 -119.832518, 39.602900 -119.836993, 39.597506 -119.839158, 39.573140 -119.848973, 39.549214 -119.847529, 39.552775 -119.806101, 39.556281 -119.800832, 39.557664 -119.773789","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response66 = requests.get(url=url, headers=headers,params=querystring66)
    data66 = response66.json()
    if isinstance(data66.get("searchResults"), list) and len(data66["searchResults"]) > 0:
        for result in data66["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring67 = {"polygon":"39.557664 -119.773789, 39.565010 -119.773971, 39.566554 -119.775549, 39.570296 -119.780829, 39.570406 -119.785615, 39.602400 -119.808737, 39.605653 -119.809891, 39.607710 -119.813500, 39.607515 -119.832518, 39.602900 -119.836993, 39.597506 -119.839158, 39.573140 -119.848973, 39.549214 -119.847529, 39.552775 -119.806101, 39.556281 -119.800832, 39.557664 -119.773789","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response67 = requests.get(url=url, headers=headers,params=querystring67)
    data67 = response67.json()
    if isinstance(data67.get("searchResults"), list) and len(data67["searchResults"]) > 0:
        for result in data67["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring68 = {"polygon":"39.557664 -119.773789, 39.565010 -119.773971, 39.566554 -119.775549, 39.570296 -119.780829, 39.570406 -119.785615, 39.602400 -119.808737, 39.605653 -119.809891, 39.607710 -119.813500, 39.607515 -119.832518, 39.602900 -119.836993, 39.597506 -119.839158, 39.573140 -119.848973, 39.549214 -119.847529, 39.552775 -119.806101, 39.556281 -119.800832, 39.557664 -119.773789","page":"4","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response68 = requests.get(url=url, headers=headers,params=querystring68)
    data68 = response68.json()
    if isinstance(data68.get("searchResults"), list) and len(data68["searchResults"]) > 0:
        for result in data68["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring69 = {"polygon":"39.557664 -119.773789, 39.565010 -119.773971, 39.566554 -119.775549, 39.570296 -119.780829, 39.570406 -119.785615, 39.602400 -119.808737, 39.605653 -119.809891, 39.607710 -119.813500, 39.607515 -119.832518, 39.602900 -119.836993, 39.597506 -119.839158, 39.573140 -119.848973, 39.549214 -119.847529, 39.552775 -119.806101, 39.556281 -119.800832, 39.557664 -119.773789","page":"5","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response69 = requests.get(url=url, headers=headers,params=querystring69)
    data69 = response69.json()
    if isinstance(data69.get("searchResults"), list) and len(data69["searchResults"]) > 0:
        for result in data69["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring70 = {"polygon":"39.599940 -119.837478, 39.588260 -119.855136, 39.620965 -119.857470, 39.623396 -119.848184, 39.623116 -119.808856, 39.602169 -119.808431, 39.605302 -119.809524, 39.607594 -119.813408, 39.607500 -119.832465, 39.599940 -119.837478","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response70 = requests.get(url=url, headers=headers,params=querystring70)
    data70 = response70.json()
    if isinstance(data70.get("searchResults"), list) and len(data70["searchResults"]) > 0:
        for result in data70["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring71 = {"polygon":"39.599940 -119.837478, 39.588260 -119.855136, 39.620965 -119.857470, 39.623396 -119.848184, 39.623116 -119.808856, 39.602169 -119.808431, 39.605302 -119.809524, 39.607594 -119.813408, 39.607500 -119.832465, 39.599940 -119.837478","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response71 = requests.get(url=url, headers=headers,params=querystring71)
    data71 = response71.json()
    if isinstance(data71.get("searchResults"), list) and len(data71["searchResults"]) > 0:
        for result in data71["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring72 = {"polygon":"39.623413 -119.848119, 39.624570 -119.849828, 39.631834 -119.853648, 39.643919 -119.864135, 39.642640 -119.867333, 39.642636 -119.870135, 39.641606 -119.874969, 39.642407 -119.878861, 39.642402 -119.881709, 39.619153 -119.882209, 39.611059 -119.851022, 39.616198 -119.848021, 39.621144 -119.848771, 39.623413 -119.848119","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response72 = requests.get(url=url, headers=headers,params=querystring72)
    data72 = response72.json()
    if isinstance(data72.get("searchResults"), list) and len(data72["searchResults"]) > 0:
        for result in data72["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring73 = {"polygon":"39.623413 -119.848119, 39.624570 -119.849828, 39.631834 -119.853648, 39.643919 -119.864135, 39.642640 -119.867333, 39.642636 -119.870135, 39.641606 -119.874969, 39.642407 -119.878861, 39.642402 -119.881709, 39.619153 -119.882209, 39.611059 -119.851022, 39.616198 -119.848021, 39.621144 -119.848771, 39.623413 -119.848119","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response73 = requests.get(url=url, headers=headers,params=querystring73)
    data73 = response73.json()
    if isinstance(data73.get("searchResults"), list) and len(data73["searchResults"]) > 0:
        for result in data73["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring74 = {"polygon":"39.623413 -119.848119, 39.624570 -119.849828, 39.631834 -119.853648, 39.643919 -119.864135, 39.642640 -119.867333, 39.642636 -119.870135, 39.641606 -119.874969, 39.642407 -119.878861, 39.642402 -119.881709, 39.619153 -119.882209, 39.611059 -119.851022, 39.616198 -119.848021, 39.621144 -119.848771, 39.623413 -119.848119","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response74 = requests.get(url=url, headers=headers,params=querystring74)
    data74 = response74.json()
    if isinstance(data74.get("searchResults"), list) and len(data74["searchResults"]) > 0:
        for result in data74["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring75 = {"polygon":"39.623413 -119.848119, 39.624570 -119.849828, 39.631834 -119.853648, 39.643919 -119.864135, 39.642640 -119.867333, 39.642636 -119.870135, 39.641606 -119.874969, 39.642407 -119.878861, 39.642402 -119.881709, 39.619153 -119.882209, 39.611059 -119.851022, 39.616198 -119.848021, 39.621144 -119.848771, 39.623413 -119.848119","page":"4","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response75 = requests.get(url=url, headers=headers,params=querystring75)
    data75 = response75.json()
    if isinstance(data75.get("searchResults"), list) and len(data75["searchResults"]) > 0:
        for result in data75["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring76 = {"polygon":"39.626842 -119.915850, 39.653481 -119.922710, 39.681523 -119.922089, 39.714318 -119.900071, 39.753807 -119.780735, 39.952641 -119.765161, 39.951015 -119.999100, 39.673745 -120.001092, 39.651239 -119.980602, 39.626842 -119.915850","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response76 = requests.get(url=url, headers=headers,params=querystring76)
    data76 = response76.json()
    if isinstance(data76.get("searchResults"), list) and len(data76["searchResults"]) > 0:
        for result in data76["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring77 = {"polygon":"39.626842 -119.915850, 39.653481 -119.922710, 39.681523 -119.922089, 39.714318 -119.900071, 39.753807 -119.780735, 39.952641 -119.765161, 39.951015 -119.999100, 39.673745 -120.001092, 39.651239 -119.980602, 39.626842 -119.915850","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response77 = requests.get(url=url, headers=headers,params=querystring77)
    data77 = response77.json()
    if isinstance(data77.get("searchResults"), list) and len(data77["searchResults"]) > 0:
        for result in data77["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring78 = {"polygon":"39.626842 -119.915850, 39.653481 -119.922710, 39.681523 -119.922089, 39.714318 -119.900071, 39.753807 -119.780735, 39.952641 -119.765161, 39.951015 -119.999100, 39.673745 -120.001092, 39.651239 -119.980602, 39.626842 -119.915850","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response78 = requests.get(url=url, headers=headers,params=querystring78)
    data78 = response78.json()
    if isinstance(data78.get("searchResults"), list) and len(data78["searchResults"]) > 0:
        for result in data78["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring79 = {"polygon":"39.626842 -119.915850, 39.653481 -119.922710, 39.681523 -119.922089, 39.714318 -119.900071, 39.753807 -119.780735, 39.952641 -119.765161, 39.951015 -119.999100, 39.673745 -120.001092, 39.651239 -119.980602, 39.626842 -119.915850","page":"4","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response79 = requests.get(url=url, headers=headers,params=querystring79)
    data79 = response79.json()
    if isinstance(data79.get("searchResults"), list) and len(data79["searchResults"]) > 0:
        for result in data79["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring80 = {"polygon":"39.626842 -119.915850, 39.653481 -119.922710, 39.681523 -119.922089, 39.714318 -119.900071, 39.753807 -119.780735, 39.952641 -119.765161, 39.951015 -119.999100, 39.673745 -120.001092, 39.651239 -119.980602, 39.626842 -119.915850","page":"5","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response80 = requests.get(url=url, headers=headers,params=querystring80)
    data80 = response80.json()
    if isinstance(data80.get("searchResults"), list) and len(data80["searchResults"]) > 0:
        for result in data80["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring81 = {"polygon":"39.715273 -119.896488, 39.722929 -119.881072, 39.747852 -119.830091, 39.741460 -119.825957, 39.673160 -119.829796, 39.671157 -119.833684, 39.678516 -119.864783, 39.693958 -119.874658, 39.711301 -119.875385, 39.715273 -119.896488","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response81 = requests.get(url=url, headers=headers,params=querystring81)
    data81 = response81.json()
    if isinstance(data81.get("searchResults"), list) and len(data81["searchResults"]) > 0:
        for result in data81["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring82 = {"polygon":"39.675388 -119.849454, 39.666600 -119.853971, 39.666577 -119.857400, 39.657137 -119.866867, 39.657043 -119.869174, 39.653399 -119.869659, 39.654146 -119.881069, 39.642557 -119.881797, 39.642335 -119.878898, 39.641575 -119.874857, 39.642632 -119.869864, 39.642632 -119.867075, 39.643954 -119.864200, 39.624114 -119.849464, 39.623503 -119.848118, 39.638345 -119.842417, 39.648682 -119.828559, 39.657685 -119.815659, 39.672154 -119.815745, 39.670965 -119.833683, 39.675388 -119.849454","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response82 = requests.get(url=url, headers=headers,params=querystring82)
    data82 = response82.json()
    if isinstance(data82.get("searchResults"), list) and len(data82["searchResults"]) > 0:
        for result in data82["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring83 = {"polygon":"39.675388 -119.849454, 39.666600 -119.853971, 39.666577 -119.857400, 39.657137 -119.866867, 39.657043 -119.869174, 39.653399 -119.869659, 39.654146 -119.881069, 39.642557 -119.881797, 39.642335 -119.878898, 39.641575 -119.874857, 39.642632 -119.869864, 39.642632 -119.867075, 39.643954 -119.864200, 39.624114 -119.849464, 39.623503 -119.848118, 39.638345 -119.842417, 39.648682 -119.828559, 39.657685 -119.815659, 39.672154 -119.815745, 39.670965 -119.833683, 39.675388 -119.849454","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response83 = requests.get(url=url, headers=headers,params=querystring83)
    data83 = response83.json()
    if isinstance(data83.get("searchResults"), list) and len(data83["searchResults"]) > 0:
        for result in data83["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring84 = {"polygon":"39.675388 -119.849454, 39.666600 -119.853971, 39.666577 -119.857400, 39.657137 -119.866867, 39.657043 -119.869174, 39.653399 -119.869659, 39.654146 -119.881069, 39.642557 -119.881797, 39.642335 -119.878898, 39.641575 -119.874857, 39.642632 -119.869864, 39.642632 -119.867075, 39.643954 -119.864200, 39.624114 -119.849464, 39.623503 -119.848118, 39.638345 -119.842417, 39.648682 -119.828559, 39.657685 -119.815659, 39.672154 -119.815745, 39.670965 -119.833683, 39.675388 -119.849454","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response84 = requests.get(url=url, headers=headers,params=querystring84)
    data84 = response84.json()
    if isinstance(data84.get("searchResults"), list) and len(data84["searchResults"]) > 0:
        for result in data84["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring85 = {"polygon":"39.675388 -119.849454, 39.666600 -119.853971, 39.666577 -119.857400, 39.657137 -119.866867, 39.657043 -119.869174, 39.653399 -119.869659, 39.654146 -119.881069, 39.642557 -119.881797, 39.642335 -119.878898, 39.641575 -119.874857, 39.642632 -119.869864, 39.642632 -119.867075, 39.643954 -119.864200, 39.624114 -119.849464, 39.623503 -119.848118, 39.638345 -119.842417, 39.648682 -119.828559, 39.657685 -119.815659, 39.672154 -119.815745, 39.670965 -119.833683, 39.675388 -119.849454","page":"4","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response85 = requests.get(url=url, headers=headers,params=querystring85)
    data85 = response85.json()
    if isinstance(data85.get("searchResults"), list) and len(data85["searchResults"]) > 0:
        for result in data85["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring86 = {"polygon":"39.626920 -119.915871, 39.653879 -119.922509, 39.681458 -119.922145, 39.714483 -119.899866, 39.715182 -119.896320, 39.711335 -119.875223, 39.693704 -119.874495, 39.677889 -119.862856, 39.675509 -119.849398, 39.666620 -119.853853, 39.656890 -119.867312, 39.657100 -119.869221, 39.653529 -119.869767, 39.654229 -119.881043, 39.619215 -119.882225, 39.626920 -119.915871","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response86 = requests.get(url=url, headers=headers,params=querystring86)
    data86 = response86.json()
    if isinstance(data86.get("searchResults"), list) and len(data86["searchResults"]) > 0:
        for result in data86["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring87 = {"polygon":"39.626920 -119.915871, 39.653879 -119.922509, 39.681458 -119.922145, 39.714483 -119.899866, 39.715182 -119.896320, 39.711335 -119.875223, 39.693704 -119.874495, 39.677889 -119.862856, 39.675509 -119.849398, 39.666620 -119.853853, 39.656890 -119.867312, 39.657100 -119.869221, 39.653529 -119.869767, 39.654229 -119.881043, 39.619215 -119.882225, 39.626920 -119.915871","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response87 = requests.get(url=url, headers=headers,params=querystring87)
    data87 = response87.json()
    if isinstance(data87.get("searchResults"), list) and len(data87["searchResults"]) > 0:
        for result in data87["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring88 = {"polygon":"39.626920 -119.915871, 39.653879 -119.922509, 39.681458 -119.922145, 39.714483 -119.899866, 39.715182 -119.896320, 39.711335 -119.875223, 39.693704 -119.874495, 39.677889 -119.862856, 39.675509 -119.849398, 39.666620 -119.853853, 39.656890 -119.867312, 39.657100 -119.869221, 39.653529 -119.869767, 39.654229 -119.881043, 39.619215 -119.882225, 39.626920 -119.915871","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    time.sleep(1)
    response88 = requests.get(url=url, headers=headers,params=querystring88)
    data88 = response88.json()
    if isinstance(data88.get("searchResults"), list) and len(data88["searchResults"]) > 0:
        for result in data88["searchResults"]:
            # Extract property data
            property_data = result.get("property", {})
            address = property_data.get("address", {})
            price = property_data.get("price", {})
            listing_data = property_data.get("listing",{})
            
            zpid = property_data.get("zpid", None)
            street_address = address.get("streetAddress", None)
            city = address.get("city", None)
            state = address.get("state", None)
            zipcode = address.get("zipcode", None)
            latitude = property_data.get("location", {}).get("latitude", None)
            longitude = property_data.get("location", {}).get("longitude", None)
            bathrooms = property_data.get("bathrooms",None)
            bedrooms = property_data.get("bedrooms",None)
            value = price.get("value", None)
            price_change = price.get("priceChange", None)
            price_per_sqft = price.get("pricePerSquareFoot", None)
            listingType = listing_data.get("listingStatus", None)
            
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
                    "bathrooms": bathrooms,
                    "bedrooms": bedrooms,
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    print(numData)
    return properties

def DataCollection():
    properties = []
    Sold(properties)
    return properties

if __name__ == '__main__':
   DataCollection()
