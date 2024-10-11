import random
import pandas as pd
import matplotlib.pyplot as plt

def coinflip(n, p):
    count = 0;
    pvalue = p*10;
    for _ in range(n):
        result = random.randint(0, 9)
        if result < pvalue:
            count +=1
    return count

if __name__ == "__main__":
    h1 = coinflip(10, 0.5)
    h2 = coinflip(100, 0.5)
    h3 = coinflip(1000, 0.5)
    
    
x = ["10", "100","1000"]
y = [h1/10, h2/100, h3/1000]

plt.bar(x,y,label="Bars 1",color="black")

plt.xlabel("N trials")
plt.ylabel("fraction of heads in N trials")
plt.title("p = 0.5")
plt.legend()
plt.show()
