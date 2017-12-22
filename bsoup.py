from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
all_images = bsObj.findAll("img")
print(all_images)
arr = []
for img in all_images:
    arr.append(img) # push every iteration of img to arr
    print(img) # verify
print(arr) # print entire array
print(len(arr)) #prints length of items in array; 6
