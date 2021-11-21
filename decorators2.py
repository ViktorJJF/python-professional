from datetime import date, datetime


def execution_time(func):
    def wrapper(*args,**kwargs):
        initial_time=datetime.now()
        func(*args,**kwargs)
        final_time=datetime.now()
        print(f"Pasaron {(final_time-initial_time).total_seconds()} segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range (1,100000000):
        pass

@execution_time
def suma(a:int,b:int)->int:
    return a+b

@execution_time
def saludo(name:str)->str:
    return f'Bienvenido {name}'

def run():
    suma(5,5)
    saludo("Viktor")

if __name__=='__main__':
    run()