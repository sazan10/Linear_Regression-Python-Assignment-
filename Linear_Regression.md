# Linear_Regression-Python-Assignment-
To find price of houses

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
        sum_y+=int(x_y[0])
        sum_x+=int(x_y[1])
        sumx_square+=int(x_y[1])*int(x_y[1])
        sumy_square+=int(x_y[0])*int(x_y[0])
        prod=int(x_y[1])*int(x_y[0])
        sum_prod+=prod
    m= (sum_y*sumx_square - sum_x*sum_prod)/((len(data) - 1)*sumx_square - sum_x*sum_x)
    c= ((len(data) - 1) * sum_prod - sum_x*sum_y)/((len(data) - 1)*sumx_square - sum_x*sum_x)
    print (m)
    print (c)
    file.close()
download_file("https://s3.amazonaws.com/back-end-training/house-prices.csv")
