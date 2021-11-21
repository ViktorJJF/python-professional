def my_closure(str):
    def repeat(number):
        return str*number
    return repeat

def run():
    repeat=my_closure("Victor")
    print(repeat(35))

if __name__=='__main__':
    run()