import requests
class download :
    def __init__(self,Link,Format):
       self.Link=Link
       self.Format=Format 
    def download(self):
        data=requests.get(self.Link).content
        Formatfile=f'./data.{self.Format}'
        with open(Formatfile , "wb") as f:
            f.write(data)
Link=input("please enter your link :")
Format=input ("please enter your format :")
download = download(Link,Format)
download.download()
