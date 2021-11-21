def remove_with_set(some_list):
    return list(set(some_list))

def remove_duplicates(list):
    without_duplicates=[]
    for element in list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    # x = {'apple', 'banana', 'cherry'}
    # y = {'google', 'microsoft', 'apple'}
    # z = x - y
    # print(z)
    print(remove_duplicates([1,2,3,3,4,5]))
    print(remove_with_set([1,2,3,3,4,5]))

if __name__=='__main__':
    run()