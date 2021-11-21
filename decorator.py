def mayusculas(func):
    def wrapper(texto):
        return func(texto).upper()
    return wrapper

@mayusculas
def mensaje(name):
    return f'{name}, recibiste un mensaje'

def run():
    print(mensaje("Victor"))

if __name__=='__main__':
    run()