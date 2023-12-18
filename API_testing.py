#This is to demonsration of API method(CRUD-GET,POST,PUT,DELETE) implementation using 'Requests' library provided by Python

# ways to convert json response string to dictionary.
#json.loads(response)
#json.load(response)
#response.json()



import requests
import json

#http GET method

get_url="http://216.10.245.166/Library/GetBook.php"
par={'AuthorName':'sanjay'}
get_res=requests.get(get_url,params=par)

print(get_res.status_code)
print(get_res.url)
print(get_res.text)
print(get_res.json())
print(f'The response type is : {type(get_res)}')

#other http methods similar to GET :

print("OPTIONS method : ")
response_data=requests.options("http://216.10.245.166/Library")
print(response_data)

print("HEAD method :")
response_data=requests.head(get_url)
print(response_data)

#History to check redirection :
print("Checking history of the request :  ")
get_res=requests.get(get_url,params=par)
print(get_res.text)
print(get_res.history)

#requests.get('htt://google.com')   #requests.exceptions.InvalidSchema: No connection adapters were found for 'htt://google.com'














