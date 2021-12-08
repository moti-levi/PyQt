import requests
import json


# url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3&limit=5&q=title:jones'  


# response = requests.get(url)
# # data = json.load(response.json())
# # print(data)
# print(response.json())


response = requests.get("https://data.gov.il/api/3/action/datastore_search?resource_id=39f455bf-6db0-4926-859d-017f34eacbcb&limit=5")
print(response.status_code)



