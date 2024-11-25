from API import houses
import requests

def schools():
    properties = houses()
    i = 0
    for i in properties:
        zpid = i.get("zpid")
        url = "https://zillow56.p.rapidapi.com/schools"

        querystring = {"zpid": zpid}

        headers = {
            "x-rapidapi-key": "eb433fb3e6msh6f40dfa8c7810a1p1587fbjsn9ddafafaa1a5",
            "x-rapidapi-host": "zillow56.p.rapidapi.com"
        }

        response = requests.get(url=url, headers=headers,params=querystring)
        data = response.json()
        if isinstance(data.get("schools"), list) and len(data["schools"]) > 0:
                schools = []
                j = 0
                for j in data["schools"]:
                    grades = j.get("grades", None) 
                    name = j.get("name", None)
                    rating = j.get("rating",None) 
                    if grades and name and rating:  
                        schools.append({"grades": grades, "name": name, "rating": rating})

    return schools

if __name__ == "__main__":
    schools()