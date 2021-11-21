from time import sleep

def fibo_gen(max=None):
    n1=0
    n2=1
    counter=0
    while True:
        if counter==0:
            counter+=1
            yield n1
        if counter==1:
            counter+=1
            yield n2
        else:
            aux=n1+n2
            n1,n2=n2,aux
            if max and max <= aux:
                raise StopIteration
            yield aux
            
if __name__=="__main__":
    try:
        for element in fibo_gen():
            print(element)
            sleep(0.05)
    except:
        print("llegamos al final...")