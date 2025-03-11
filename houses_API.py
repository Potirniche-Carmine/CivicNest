import requests

#Code from URL down to response were provided by RapidApi itself.
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
            listing_data = property_data.get("listing",{})
            
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
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
            listing_data = property_data.get("listing",{})
            
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
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
            listing_data = property_data.get("listing",{})
            
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
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
            listing_data = property_data.get("listing",{})
            
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
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
            listing_data = property_data.get("listing",{})
            
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
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
            listing_data = property_data.get("listing",{})
            
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring8 = {"polygon":"39.507446 -119.858525, 39.507330 -119.858121, 39.505990 -119.854425, 39.505472 -119.853019, 39.505392 -119.852748, 39.505319 -119.852451, 39.505276 -119.852168, 39.505237 -119.851915, 39.505203 -119.851360, 39.505220 -119.850869, 39.505291 -119.850333, 39.505548 -119.848798, 39.505650 -119.848395, 39.505846 -119.847852, 39.506058 -119.847437, 39.506505 -119.846710, 39.506766 -119.846148, 39.506845 -119.845877, 39.507052 -119.844867, 39.507168 -119.844464, 39.508731 -119.840509, 39.508804 -119.840259, 39.509522 -119.837919, 39.509642 -119.837326, 39.509835 -119.835869, 39.509873 -119.835693, 39.510405 -119.835042, 39.510525 -119.834897, 39.511941 -119.832805, 39.512394 -119.832285, 39.512599 -119.831977, 39.512844 -119.830623, 39.512904 -119.830369, 39.514030 -119.827962, 39.514158 -119.827746, 39.515369 -119.826118, 39.516056 -119.825450, 39.517180 -119.824638, 39.518133 -119.823965, 39.519021 -119.823208, 39.519840 -119.822046, 39.519926 -119.821807, 39.519969 -119.821540, 39.520071 -119.811376, 39.520321 -119.810455, 39.505875 -119.803397, 39.505451 -119.826479, 39.505051 -119.832718, 39.505029 -119.841608, 39.505087 -119.842127, 39.505014 -119.845251, 39.504956 -119.845619, 39.502866 -119.851565, 39.502458 -119.852301, 39.502422 -119.852622, 39.502431 -119.853767, 39.502338 -119.854044, 39.501760 -119.855227, 39.501305 -119.855901, 39.500777 -119.856968, 39.500723 -119.857245, 39.500777 -119.858065, 39.501150 -119.858010, 39.501527 -119.857985, 39.501888 -119.858005, 39.502260 -119.858075, 39.502548 -119.858176, 39.503169 -119.858398, 39.503682 -119.858488, 39.507446 -119.858525 ","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring9 = {"polygon":"39.507446 -119.858525, 39.507330 -119.858121, 39.505990 -119.854425, 39.505472 -119.853019, 39.505392 -119.852748, 39.505319 -119.852451, 39.505276 -119.852168, 39.505237 -119.851915, 39.505203 -119.851360, 39.505220 -119.850869, 39.505291 -119.850333, 39.505548 -119.848798, 39.505650 -119.848395, 39.505846 -119.847852, 39.506058 -119.847437, 39.506505 -119.846710, 39.506766 -119.846148, 39.506845 -119.845877, 39.507052 -119.844867, 39.507168 -119.844464, 39.508731 -119.840509, 39.508804 -119.840259, 39.509522 -119.837919, 39.509642 -119.837326, 39.509835 -119.835869, 39.509873 -119.835693, 39.510405 -119.835042, 39.510525 -119.834897, 39.511941 -119.832805, 39.512394 -119.832285, 39.512599 -119.831977, 39.512844 -119.830623, 39.512904 -119.830369, 39.514030 -119.827962, 39.514158 -119.827746, 39.515369 -119.826118, 39.516056 -119.825450, 39.517180 -119.824638, 39.518133 -119.823965, 39.519021 -119.823208, 39.519840 -119.822046, 39.519926 -119.821807, 39.519969 -119.821540, 39.520071 -119.811376, 39.520321 -119.810455, 39.505875 -119.803397, 39.505451 -119.826479, 39.505051 -119.832718, 39.505029 -119.841608, 39.505087 -119.842127, 39.505014 -119.845251, 39.504956 -119.845619, 39.502866 -119.851565, 39.502458 -119.852301, 39.502422 -119.852622, 39.502431 -119.853767, 39.502338 -119.854044, 39.501760 -119.855227, 39.501305 -119.855901, 39.500777 -119.856968, 39.500723 -119.857245, 39.500777 -119.858065, 39.501150 -119.858010, 39.501527 -119.857985, 39.501888 -119.858005, 39.502260 -119.858075, 39.502548 -119.858176, 39.503169 -119.858398, 39.503682 -119.858488, 39.507446 -119.858525 ","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
        
    querystring10 = {"polygon":"39.534471 -119.815553, 39.534997 -119.813268, 39.535996 -119.810082, 39.536233 -119.809180, 39.536382 -119.808365, 39.536475 -119.807590, 39.536568 -119.806588, 39.536803 -119.788459, 39.534096 -119.788102, 39.533536 -119.787932, 39.532833 -119.787624, 39.531630 -119.786759, 39.530105 -119.785245, 39.529128 -119.784565, 39.528628 -119.784365, 39.528104 -119.784226, 39.520096 -119.783851, 39.519354 -119.783679, 39.510600 -119.780828, 39.509359 -119.780574, 39.507791 -119.780433, 39.506506 -119.780630, 39.506005 -119.780743, 39.505831 -119.803222, 39.512832 -119.806604, 39.513058 -119.806622, 39.521933 -119.811007, 39.522033 -119.811325, 39.523296 -119.811811, 39.524879 -119.812418, 39.525645 -119.812865, 39.534471 -119.815553","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring11 = {"polygon":"39.534471 -119.815553, 39.534997 -119.813268, 39.535996 -119.810082, 39.536233 -119.809180, 39.536382 -119.808365, 39.536475 -119.807590, 39.536568 -119.806588, 39.536803 -119.788459, 39.534096 -119.788102, 39.533536 -119.787932, 39.532833 -119.787624, 39.531630 -119.786759, 39.530105 -119.785245, 39.529128 -119.784565, 39.528628 -119.784365, 39.528104 -119.784226, 39.520096 -119.783851, 39.519354 -119.783679, 39.510600 -119.780828, 39.509359 -119.780574, 39.507791 -119.780433, 39.506506 -119.780630, 39.506005 -119.780743, 39.505831 -119.803222, 39.512832 -119.806604, 39.513058 -119.806622, 39.521933 -119.811007, 39.522033 -119.811325, 39.523296 -119.811811, 39.524879 -119.812418, 39.525645 -119.812865, 39.534471 -119.815553","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })

    querystring12 = {"polygon":"39.556160 -119.787923, 39.556129 -119.786328, 39.556221 -119.784733, 39.556437 -119.782619, 39.556529 -119.781822, 39.556898 -119.779349, 39.557236 -119.776080, 39.557328 -119.774843, 39.557359 -119.774046, 39.557267 -119.773089, 39.557236 -119.772650, 39.556990 -119.771414, 39.556744 -119.769819, 39.556406 -119.768104, 39.556252 -119.766629, 39.556191 -119.765512, 39.556160 -119.764754, 39.556252 -119.763199, 39.556375 -119.762003, 39.556314 -119.757297, 39.556129 -119.755303, 39.556206 -119.752597, 39.554590 -119.752671, 39.554488 -119.752514, 39.552870 -119.752673, 39.552541 -119.752673, 39.552117 -119.752686, 39.551353 -119.752741, 39.543918 -119.752796, 39.543939 -119.754571, 39.544056 -119.755107, 39.544258 -119.755644, 39.544438 -119.755878, 39.544809 -119.756290, 39.545276 -119.757005, 39.545467 -119.757803, 39.545520 -119.758340, 39.545509 -119.760141, 39.545551 -119.760444, 39.545530 -119.762012, 39.545562 -119.762260, 39.545530 -119.763896, 39.545498 -119.764172, 39.545509 -119.769302, 39.545530 -119.769508, 39.545583 -119.775120, 39.545530 -119.776165, 39.545530 -119.782726, 39.545551 -119.783222, 39.545551 -119.787719, 39.554371 -119.787637, 39.555106 -119.787685, 39.555718 -119.787857, 39.556160 -119.787923","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })

    querystring13 = {"polygon":"39.556160 -119.787923, 39.556129 -119.786328, 39.556221 -119.784733, 39.556437 -119.782619, 39.556529 -119.781822, 39.556898 -119.779349, 39.557236 -119.776080, 39.557328 -119.774843, 39.557359 -119.774046, 39.557267 -119.773089, 39.557236 -119.772650, 39.556990 -119.771414, 39.556744 -119.769819, 39.556406 -119.768104, 39.556252 -119.766629, 39.556191 -119.765512, 39.556160 -119.764754, 39.556252 -119.763199, 39.556375 -119.762003, 39.556314 -119.757297, 39.556129 -119.755303, 39.556206 -119.752597, 39.554590 -119.752671, 39.554488 -119.752514, 39.552870 -119.752673, 39.552541 -119.752673, 39.552117 -119.752686, 39.551353 -119.752741, 39.543918 -119.752796, 39.543939 -119.754571, 39.544056 -119.755107, 39.544258 -119.755644, 39.544438 -119.755878, 39.544809 -119.756290, 39.545276 -119.757005, 39.545467 -119.757803, 39.545520 -119.758340, 39.545509 -119.760141, 39.545551 -119.760444, 39.545530 -119.762012, 39.545562 -119.762260, 39.545530 -119.763896, 39.545498 -119.764172, 39.545509 -119.769302, 39.545530 -119.769508, 39.545583 -119.775120, 39.545530 -119.776165, 39.545530 -119.782726, 39.545551 -119.783222, 39.545551 -119.787719, 39.554371 -119.787637, 39.555106 -119.787685, 39.555718 -119.787857, 39.556160 -119.787923","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring14 = {"polygon":"39.550746 -119.822957, 39.550746 -119.822917, 39.550741 -119.822883, 39.550733 -119.822852, 39.550720 -119.822827, 39.550710 -119.822813, 39.550492 -119.822657, 39.550486 -119.822652, 39.549974 -119.822247, 39.549938 -119.822230, 39.549896 -119.822221, 39.549846 -119.822215, 39.549768 -119.822208, 39.549618 -119.822184, 39.549178 -119.822180, 39.549152 -119.822175, 39.549111 -119.822160, 39.549028 -119.822120, 39.548992 -119.822107, 39.548962 -119.822102, 39.547270 -119.822032, 39.547170 -119.822022, 39.546988 -119.821999, 39.546872 -119.821983, 39.534809 -119.817297, 39.534785 -119.817429, 39.532528 -119.822763, 39.532249 -119.823481, 39.532133 -119.823839, 39.531930 -119.824565, 39.531135 -119.827308, 39.531011 -119.827723, 39.530811 -119.828244, 39.530636 -119.828631, 39.530391 -119.829100, 39.530343 -119.829172, 39.528982 -119.831335, 39.528784 -119.831686, 39.528525 -119.832170, 39.528315 -119.832639, 39.527993 -119.833501, 39.527834 -119.834023, 39.527630 -119.834891, 39.527452 -119.836282, 39.526867 -119.851567, 39.526865 -119.851911, 39.526870 -119.852278, 39.526878 -119.852803, 39.526861 -119.853908, 39.526830 -119.854535, 39.526759 -119.855350, 39.526696 -119.855858, 39.526619 -119.856382, 39.526351 -119.857565, 39.526262 -119.857924, 39.526059 -119.858656, 39.525853 -119.859302, 39.525561 -119.860086, 39.525327 -119.860646, 39.524944 -119.861450, 39.524475 -119.862339, 39.525736 -119.862509, 39.525966 -119.862545, 39.526608 -119.862697, 39.526877 -119.862776, 39.527715 -119.863074, 39.528387 -119.863336, 39.528957 -119.863567, 39.530372 -119.864119, 39.530726 -119.864221, 39.531014 -119.864298, 39.531585 -119.864382, 39.532631 -119.864405, 39.535950 -119.864461, 39.536280 -119.864422, 39.536584 -119.864348, 39.536932 -119.864259, 39.537237 -119.864149, 39.537738 -119.863916, 39.538269 -119.863565, 39.539078 -119.862873, 39.539601 -119.862230, 39.539961 -119.861682, 39.540195 -119.861243, 39.540423 -119.860735, 39.542651 -119.855295, 39.542921 -119.854709, 39.543201 -119.854163, 39.563878 -119.853015, 39.544352 -119.852346, 39.544634 -119.851975, 39.544998 -119.851547, 39.548375 -119.848000, 39.548691 -119.847586, 39.548977 -119.847115, 39.549224 -119.846588, 39.549417 -119.846024, 39.549555 -119.845434, 39.549615 -119.844952, 39.550749 -119.831337, 39.550761 -119.830946, 39.550739 -119.830253, 39.550538 -119.825694, 39.550528 -119.825250, 39.550548 -119.824741, 39.550595 -119.824176, 39.550743 -119.822982, 39.550746 -119.822957","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })

    querystring15 = {"polygon":"39.550746 -119.822957, 39.550746 -119.822917, 39.550741 -119.822883, 39.550733 -119.822852, 39.550720 -119.822827, 39.550710 -119.822813, 39.550492 -119.822657, 39.550486 -119.822652, 39.549974 -119.822247, 39.549938 -119.822230, 39.549896 -119.822221, 39.549846 -119.822215, 39.549768 -119.822208, 39.549618 -119.822184, 39.549178 -119.822180, 39.549152 -119.822175, 39.549111 -119.822160, 39.549028 -119.822120, 39.548992 -119.822107, 39.548962 -119.822102, 39.547270 -119.822032, 39.547170 -119.822022, 39.546988 -119.821999, 39.546872 -119.821983, 39.534809 -119.817297, 39.534785 -119.817429, 39.532528 -119.822763, 39.532249 -119.823481, 39.532133 -119.823839, 39.531930 -119.824565, 39.531135 -119.827308, 39.531011 -119.827723, 39.530811 -119.828244, 39.530636 -119.828631, 39.530391 -119.829100, 39.530343 -119.829172, 39.528982 -119.831335, 39.528784 -119.831686, 39.528525 -119.832170, 39.528315 -119.832639, 39.527993 -119.833501, 39.527834 -119.834023, 39.527630 -119.834891, 39.527452 -119.836282, 39.526867 -119.851567, 39.526865 -119.851911, 39.526870 -119.852278, 39.526878 -119.852803, 39.526861 -119.853908, 39.526830 -119.854535, 39.526759 -119.855350, 39.526696 -119.855858, 39.526619 -119.856382, 39.526351 -119.857565, 39.526262 -119.857924, 39.526059 -119.858656, 39.525853 -119.859302, 39.525561 -119.860086, 39.525327 -119.860646, 39.524944 -119.861450, 39.524475 -119.862339, 39.525736 -119.862509, 39.525966 -119.862545, 39.526608 -119.862697, 39.526877 -119.862776, 39.527715 -119.863074, 39.528387 -119.863336, 39.528957 -119.863567, 39.530372 -119.864119, 39.530726 -119.864221, 39.531014 -119.864298, 39.531585 -119.864382, 39.532631 -119.864405, 39.535950 -119.864461, 39.536280 -119.864422, 39.536584 -119.864348, 39.536932 -119.864259, 39.537237 -119.864149, 39.537738 -119.863916, 39.538269 -119.863565, 39.539078 -119.862873, 39.539601 -119.862230, 39.539961 -119.861682, 39.540195 -119.861243, 39.540423 -119.860735, 39.542651 -119.855295, 39.542921 -119.854709, 39.543201 -119.854163, 39.563878 -119.853015, 39.544352 -119.852346, 39.544634 -119.851975, 39.544998 -119.851547, 39.548375 -119.848000, 39.548691 -119.847586, 39.548977 -119.847115, 39.549224 -119.846588, 39.549417 -119.846024, 39.549555 -119.845434, 39.549615 -119.844952, 39.550749 -119.831337, 39.550761 -119.830946, 39.550739 -119.830253, 39.550538 -119.825694, 39.550528 -119.825250, 39.550548 -119.824741, 39.550595 -119.824176, 39.550743 -119.822982, 39.550746 -119.822957","page":"3","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })

    querystring16 = {"polygon":"39.550746 -119.822957, 39.550746 -119.822917, 39.550741 -119.822883, 39.550733 -119.822852, 39.550720 -119.822827, 39.550710 -119.822813, 39.550492 -119.822657, 39.550486 -119.822652, 39.549974 -119.822247, 39.549938 -119.822230, 39.549896 -119.822221, 39.549846 -119.822215, 39.549768 -119.822208, 39.549618 -119.822184, 39.549178 -119.822180, 39.549152 -119.822175, 39.549111 -119.822160, 39.549028 -119.822120, 39.548992 -119.822107, 39.548962 -119.822102, 39.547270 -119.822032, 39.547170 -119.822022, 39.546988 -119.821999, 39.546872 -119.821983, 39.534809 -119.817297, 39.534785 -119.817429, 39.532528 -119.822763, 39.532249 -119.823481, 39.532133 -119.823839, 39.531930 -119.824565, 39.531135 -119.827308, 39.531011 -119.827723, 39.530811 -119.828244, 39.530636 -119.828631, 39.530391 -119.829100, 39.530343 -119.829172, 39.528982 -119.831335, 39.528784 -119.831686, 39.528525 -119.832170, 39.528315 -119.832639, 39.527993 -119.833501, 39.527834 -119.834023, 39.527630 -119.834891, 39.527452 -119.836282, 39.526867 -119.851567, 39.526865 -119.851911, 39.526870 -119.852278, 39.526878 -119.852803, 39.526861 -119.853908, 39.526830 -119.854535, 39.526759 -119.855350, 39.526696 -119.855858, 39.526619 -119.856382, 39.526351 -119.857565, 39.526262 -119.857924, 39.526059 -119.858656, 39.525853 -119.859302, 39.525561 -119.860086, 39.525327 -119.860646, 39.524944 -119.861450, 39.524475 -119.862339, 39.525736 -119.862509, 39.525966 -119.862545, 39.526608 -119.862697, 39.526877 -119.862776, 39.527715 -119.863074, 39.528387 -119.863336, 39.528957 -119.863567, 39.530372 -119.864119, 39.530726 -119.864221, 39.531014 -119.864298, 39.531585 -119.864382, 39.532631 -119.864405, 39.535950 -119.864461, 39.536280 -119.864422, 39.536584 -119.864348, 39.536932 -119.864259, 39.537237 -119.864149, 39.537738 -119.863916, 39.538269 -119.863565, 39.539078 -119.862873, 39.539601 -119.862230, 39.539961 -119.861682, 39.540195 -119.861243, 39.540423 -119.860735, 39.542651 -119.855295, 39.542921 -119.854709, 39.543201 -119.854163, 39.563878 -119.853015, 39.544352 -119.852346, 39.544634 -119.851975, 39.544998 -119.851547, 39.548375 -119.848000, 39.548691 -119.847586, 39.548977 -119.847115, 39.549224 -119.846588, 39.549417 -119.846024, 39.549555 -119.845434, 39.549615 -119.844952, 39.550749 -119.831337, 39.550761 -119.830946, 39.550739 -119.830253, 39.550538 -119.825694, 39.550528 -119.825250, 39.550548 -119.824741, 39.550595 -119.824176, 39.550743 -119.822982, 39.550746 -119.822957","page":"4","sortOrder":"Homes_for_you","listingStatus":"Sold","listPriceRange":"min 50000","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}

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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring17 = {"polygon":"39.545313 -119.787734, 39.545374 -119.758222, 39.545330 -119.757821, 39.545253 -119.757377, 39.545054 -119.756920, 39.544790 -119.756490, 39.544481 -119.756147, 39.544205 -119.755761, 39.544028 -119.755389, 39.543874 -119.754931, 39.543808 -119.754473, 39.543808 -119.752785, 39.541513 -119.752842, 39.541314 -119.752913, 39.540310 -119.752971, 39.539990 -119.753028, 39.534179 -119.753084, 39.534157 -119.771783, 39.534212 -119.772726, 39.534608 -119.775755, 39.534917 -119.777240, 39.535159 -119.777855, 39.536459 -119.780569, 39.536834 -119.781526, 39.537131 -119.782454, 39.537318 -119.783383, 39.537462 -119.784426, 39.537528 -119.785483, 39.537506 -119.786454, 39.537462 -119.786416, 39.537346 -119.787854, 39.545313 -119.787734","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring18 = {"polygon":"39.545313 -119.787734, 39.545374 -119.758222, 39.545330 -119.757821, 39.545253 -119.757377, 39.545054 -119.756920, 39.544790 -119.756490, 39.544481 -119.756147, 39.544205 -119.755761, 39.544028 -119.755389, 39.543874 -119.754931, 39.543808 -119.754473, 39.543808 -119.752785, 39.541513 -119.752842, 39.541314 -119.752913, 39.540310 -119.752971, 39.539990 -119.753028, 39.534179 -119.753084, 39.534157 -119.771783, 39.534212 -119.772726, 39.534608 -119.775755, 39.534917 -119.777240, 39.535159 -119.777855, 39.536459 -119.780569, 39.536834 -119.781526, 39.537131 -119.782454, 39.537318 -119.783383, 39.537462 -119.784426, 39.537528 -119.785483, 39.537506 -119.786454, 39.537462 -119.786416, 39.537346 -119.787854, 39.545313 -119.787734","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })

    querystring19 = {"polygon":"39.556213 -119.752208, 39.556250 -119.748393, 39.552809 -119.748436, 39.552817 -119.752535, 39.556213 -119.752208","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    
    querystring20 = {"polygon":"39.556246 -119.748338, 39.556230 -119.740445, 39.555530 -119.740457, 39.553610 -119.739861, 39.553407 -119.739773, 39.552785 -119.739765, 39.552819 -119.748415, 39.556246 -119.748338","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })

    querystring21 = {"polygon":"39.552804 -119.739694, 39.553426 -119.739719, 39.553656 -119.739837, 39.555450 -119.740379, 39.556232 -119.740395, 39.556257 -119.738036, 39.556196 -119.737494, 39.556075 -119.736983, 39.555741 -119.736102, 39.555450 -119.735670, 39.554578 -119.734632, 39.554062 -119.734254, 39.553444 -119.734003, 39.552789 -119.733964, 39.552804 -119.739694","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring22 = {"polygon":"39.552765 -119.752486, 39.552737 -119.734072, 39.541943 -119.733903, 39.541994 -119.743872, 39.541977 -119.744173, 39.541865 -119.744982, 39.540388 -119.752658, 39.552765 -119.752486","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring23 = {"polygon":"39.552765 -119.752486, 39.552737 -119.734072, 39.541943 -119.733903, 39.541994 -119.743872, 39.541977 -119.744173, 39.541865 -119.744982, 39.540388 -119.752658, 39.552765 -119.752486","page":"2","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring24 = {"polygon":"39.545269 -119.761853, 39.545335 -119.758250, 39.545309 -119.757778, 39.545217 -119.757357, 39.545061 -119.756969, 39.544814 -119.756547, 39.544333 -119.756008, 39.544125 -119.755704, 39.543891 -119.755165, 39.543800 -119.754440, 39.543761 -119.752821, 39.540305 -119.753021, 39.538606 -119.761974, 39.545269 -119.761853","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring25 = {"polygon":"39.543926 -119.762190, 39.543757 -119.762000, 39.538570 -119.762047, 39.537953 -119.765344, 39.538876 -119.765351, 39.538990 -119.765428, 39.542129 -119.765386, 39.542349 -119.765301, 39.542502 -119.765178, 39.543483 -119.764073, 39.543537 -119.763933, 39.543717 -119.763702, 39.543792 -119.763493, 39.543825 -119.763316, 39.543841 -119.762650, 39.543858 -119.762463, 39.543924 -119.762253, 39.543926 -119.762190","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
                    "price": value,
                    "priceChange": price_change,
                    "pricePerSquareFoot": price_per_sqft,
                    "listingType": listingType
                })
    querystring25 = {"polygon":"39.545392 -119.771389, 39.545373 -119.769445, 39.545419 -119.769266, 39.545407 -119.764129, 39.545367 -119.763882, 39.545337 -119.762154, 39.544417 -119.762145, 39.544272 -119.762222, 39.544108 -119.762410, 39.544042 -119.762614, 39.544016 -119.763331, 39.543930 -119.763672, 39.543851 -119.763842, 39.543647 -119.764132, 39.543542 -119.764149, 39.542556 -119.765266, 39.542267 -119.765428, 39.542063 -119.765479, 39.539005 -119.765496, 39.538867 -119.765556, 39.537907 -119.765560, 39.536815 -119.771362, 39.536881 -119.771393, 39.545392 -119.771389","page":"1","sortOrder":"Homes_for_you","listingStatus":"Sold","bed_min":"No_Min","bed_max":"No_Max","bathrooms":"Any","homeType":"Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured","maxHOA":"Any","listingType":"By_Agent","listingTypeOptions":"Agent listed,New Construction,Fore-closures,Auctions","parkingSpots":"Any","mustHaveBasement":"No","soldInLast":"Any","daysOnZillow":"Any"}
    
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
