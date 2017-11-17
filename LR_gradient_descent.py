import urllib.request
import random
import normalization
def download_file(url):
    list_x=[]
    list_y=[]
    while True:
        try:
            file=open("assignment.csv","r")
            break
        except:
            full_name= "assignment.csv"
            urllib.request.urlretrieve(url, full_name)
    text=file.read()
    data=text.split("\n")
    for line in data[0:(len(data)-1)]:
        x_y=line.split(",")
        results = list(map(int, x_y))
        list_x.append(results[1])
        list_y.append(results[0])
        #print(results)
    return list_x,list_y

def gradient_descent(x,y,alpha,theta0,theta1,p):
    m=len(x)
    for i in range(10000):
        delta0=0
        delta1=0
        for l in range(m):
            pred=theta0+theta1*x[l]
            delta0=delta0+(pred-y[l])
            delta1=delta1+(pred-y[l])*x[l]
        del0=2*(delta0/m)
        del1=2*(delta1/m)
        theta0=theta0-alpha*del0
        theta1=theta1-alpha*del1
    print(theta1,theta0*p)

a,b =download_file("https://s3.amazonaws.com/back-end-training/house-prices.csv")
p=max(a)
x_norm,y_norm= normalization.normalize(a,b)
gradient_descent(x_norm,y_norm,0.5,0,0,p)
