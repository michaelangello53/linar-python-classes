import time
stocks=[10,20,30,10,100,10]
money=0
def trade():
    global money
    for i in range(len(stocks)):
        try:
            if stocks[i+1]>stocks[i]:
                print("trading stocks....")
                money-=stocks[i]      
                money+=[i+1]
            time.sleep(1)    
        except:
            return
trade()            
print("you made"+str(money)+"$")