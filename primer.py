def is_prime(number:int) -> bool:
    counter=0
    for i in range(1,number+1):
        if number%i==0:
            counter+=1
    return counter<=2

def run():
    print(is_prime(59))

if __name__=='__main__':
    run()