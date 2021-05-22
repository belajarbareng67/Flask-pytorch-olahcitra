import requests

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('C://Users//Satria Putra//python//olahcitra//hiu.jpg','rb')})

print(resp.json())
#print(resp)
