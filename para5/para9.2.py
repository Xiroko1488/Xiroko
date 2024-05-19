import requests

response = requests.post("https://httpbin.org/post",data="Vasya data",
                         headers={"h1":"Vasya title"})
print(response.text)