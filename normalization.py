def normalize(x,y):
    max_x=max(x)
    max_y=max(y)
    for i in range(len(x)):
        x[i]=(x[i])/max_x
        y[i]=(y[i])/max_x
    return x,y
