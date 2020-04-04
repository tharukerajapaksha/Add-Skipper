import requests

from bs4 import BeautifulSoup

user_input = str (input("Enter Your Url Here : "))

req = requests.get(user_input)

cont = req.content



b = BeautifulSoup(cont)

all= b.find_all ("a")

link = ""

name = " "

a = 0

count = 0
while a < 150 :

    all = b. find_all ("a",href = True) [a]

    link = all ["href"]

    name = all.text

    name_display = all.text

    name = name.split (" ")

    if name [0] == "Download" and name [3] == "480p":

        print (name_display," ",link)

        
    if name == " " :

         break   

   

    a = a+1

