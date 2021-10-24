import requests


bearer_token = 'BearereyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MzQ1NTE2OTksImp0aSI6ImhTZ2VQMTdMeW51aGg0RlNMb3NLY0dZWEZWZUZyM0ZlIiwiYXVkIjoiYXBpLnNrZW5hcmlvcy5jb20iLCJpc3MiOiJza2VuYXJpb3MuY29tIiwic3ViIjoiaWxqYSt0ZXN0LWVuZ2luZWVyQHNrZW5hcmlvbGFicy5jb20iLCJ1c2VyTmFtZSI6ImlsamErdGVzdC1lbmdpbmVlckBza2VuYXJpb2xhYnMuY29tIiwiZW1haWwiOiJpbGphK3Rlc3QtZW5naW5lZXJAc2tlbmFyaW9sYWJzLmNvbSIsInNrZW5hcmlvc1VzZXJJZCI6Mjg3NCwib3JnYW5pemF0aW9uSWQiOjE0NTd9.OrI_7MMx0q5tBGwKJPyCablDDi-B0u5P0dpdSO6w3aDdudmoqnWZCty5WTSqFsZd7mzH0un8zKSaoKC-JRcs0Q'
url = "https://api.skenarios.com/api/v1/portfolio/4116/building/12341234"

response_code = requests.delete(url)
print("the response for this GET request is")
print(response_code)

if response_code.ok:
    print("No Error")
else:
    print("This request has an error")
