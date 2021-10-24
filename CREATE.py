import requests

bearer_token = 'BearereyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MzQ1NTE2OTksImp0aSI6ImhTZ2VQMTdMeW51aGg0RlNMb3NLY0dZWEZWZUZyM0ZlIiwiYXVkIjoiYXBpLnNrZW5hcmlvcy5jb20iLCJpc3MiOiJza2VuYXJpb3MuY29tIiwic3ViIjoiaWxqYSt0ZXN0LWVuZ2luZWVyQHNrZW5hcmlvbGFicy5jb20iLCJ1c2VyTmFtZSI6ImlsamErdGVzdC1lbmdpbmVlckBza2VuYXJpb2xhYnMuY29tIiwiZW1haWwiOiJpbGphK3Rlc3QtZW5naW5lZXJAc2tlbmFyaW9sYWJzLmNvbSIsInNrZW5hcmlvc1VzZXJJZCI6Mjg3NCwib3JnYW5pemF0aW9uSWQiOjE0NTd9.OrI_7MMx0q5tBGwKJPyCablDDi-B0u5P0dpdSO6w3aDdudmoqnWZCty5WTSqFsZd7mzH0un8zKSaoKC-JRcs0Q'
url = "https://api.skenarios.com/api/v1/portfolio/4116/building"

body = {
    "groupId": "test",
    "buildingId": "121213",
    "description": "My building's notes",
    "address": "Betonimiehenkuja 3",
    "postalCode": "02150",
    "city": "Espoo",
    "country": "FI",
    "buildingType": "office",
    "floors": 6,
    "floorArea": 60,
    "buildYear": 1964,
    "volume": 4000,
    "balconies": 0,
    "units": 50,
    "lifts": 0,
    "latitude": 60.1805653,
    "longitude": 24.832332299999997,
    "buildingName": "My building's name",
    "polygonUniqueId": "string",
    "propertyGroupId": 0,
    "propertyBuildingId": 0,
    "buildingPrototype": "string",
    "grossInternalArea": 58,
    "netInternalArea": 56,
    "attributes": [
        {
            "key": "NUMBER_OF_ROOMS",
            "value": 4
        }
    ]
}

response_code = requests.post(url, headers={'Authorization': bearer_token}, data=body)
print("the response for this POST request is")
print(response_code)
if response_code.ok:
    print("This request has no error")
else:
    print("This request has an error")


