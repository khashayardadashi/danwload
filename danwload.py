import requests
class dawnload :
    def __init__(self,Link,Format):
       self.Link=Link
       self.Format=Format 
    def dawnload(self):
        data=requests.get(self.Link).content
        Formatfile=f'./data.{self.Format}'
        with open(Formatfile , "wb") as f:
            f.write(data)
Link=input("please enter your link :")
Format=input ("please enter your format :")
dawnload = dawnload(Link,Format)
dawnload.dawnload()
