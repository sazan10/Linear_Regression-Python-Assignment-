# Linear_Regression-Python-Assignment-
To find price of houses
```
import urllib.request
import random
def download_file(url):
    while True:
        try:
            file=open("assignment.csv","r")
            break
        except:
            full_name= "assignment.csv"
            urllib.request.urlretrieve(url, full_name)
    text=file.read()
    data=text.split("\n")
    sum_x=0
    sum_y=0
    prod=0
    sum_prod=0
    sumx_square=0
    sumy_square=0
    for line in data[0:(len(data)-1)]:
        x_y=line.split(",")
        results = list(map(int, x_y))
        sum_y+=(results[0])
        sum_x+=(results[1])
        sumx_square+=results[1]*results[1]
        sumy_square+=results[0]*results[0]
        prod=results[1]*results[0]
        sum_prod+=prod
    m= (sum_y*sumx_square - sum_x*sum_prod)/((len(data) - 1)*sumx_square - sum_x*sum_x)
    c= ((len(data) - 1) * sum_prod - sum_x*sum_y)/((len(data) - 1)*sumx_square - sum_x*sum_x)
    print (m)
    print (c)
    file.close()
download_file("https://s3.amazonaws.com/back-end-training/house-prices.csv")
```
