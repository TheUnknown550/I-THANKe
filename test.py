import time
x=int(input("how long do you want the timer to be: "))
start=time.time()
while time.time() - start < 60:
    y=time.time()-start
    print(x-y,end='\r')