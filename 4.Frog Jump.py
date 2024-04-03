# Frog Jump: to find how many group of numbers are needed in order to find Y

def solution1(x,y,D):
    v = (y-x)//D
    if x+v*D >=y:
        return v
    else:
        return v+1
    

x = 1258
y = 465413213548
D = 1000
print(solution1(x,y,D))