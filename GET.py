import requests
import json

bearer_token = 'BearereyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MzQ1NTE2OTksImp0aSI6ImhTZ2VQMTdMeW51aGg0RlNMb3NLY0dZWEZWZUZyM0ZlIiwiYXVkIjoiYXBpLnNrZW5hcmlvcy5jb20iLCJpc3MiOiJza2VuYXJpb3MuY29tIiwic3ViIjoiaWxqYSt0ZXN0LWVuZ2luZWVyQHNrZW5hcmlvbGFicy5jb20iLCJ1c2VyTmFtZSI6ImlsamErdGVzdC1lbmdpbmVlckBza2VuYXJpb2xhYnMuY29tIiwiZW1haWwiOiJpbGphK3Rlc3QtZW5naW5lZXJAc2tlbmFyaW9sYWJzLmNvbSIsInNrZW5hcmlvc1VzZXJJZCI6Mjg3NCwib3JnYW5pemF0aW9uSWQiOjE0NTd9.OrI_7MMx0q5tBGwKJPyCablDDi-B0u5P0dpdSO6w3aDdudmoqnWZCty5WTSqFsZd7mzH0un8zKSaoKC-JRcs0Q'
url = 'https://api.skenarios.com/api/v1/portfolio/4116/building/121212'


def callMyApi():
    print("Calling API ...")
    response_text = requests.get(url, headers={'Authorization': bearer_token})
    print(response_text)
    response_result = (json.dumps(response_text.json(), indent=4))
    print(response_result)
callMyApi()

def check_status():
    response = requests.get(url, headers={'Authorization': bearer_token})
    assert response.status_code == 200
check_status()

def check_unexisting_id():
    url = 'https://api.skenarios.com/api/v1/portfolio/4116/building/000'
    response = requests.get(url, headers={'Authorization': bearer_token})
    if response.status_code == 200:
        print("This id exist")
    else:
        print("This id does not exist")
check_unexisting_id()










