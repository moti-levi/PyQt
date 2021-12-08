# import urllib
# import urllib.request

urlAddress = 'https://data.gov.il/api/3/action/datastore_search?resource_id=39f455bf-6db0-4926-859d-017f34eacbcb&limit=5'  
url2='https://data.gov.il/api/3/action/datastore_search?resource_id=39f455bf-6db0-4926-859d-017f34eacbcb&q=Rav&limit=50'
# url2 = 'https://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3&limit=5'
# fileobj = urllib.urlopen(url)
# print (fileobj.read())


import urllib.request


s=urllib.request.urlopen(url2).read().decode('utf-8')
print(s)
# with urllib.request.urlopen(urlAddress) as url:
#     s = url.read()
#     # I'm guessing this would output the html source code ?
#     print(s)
      