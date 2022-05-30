import random

def timer(fn):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.8f}s to execute'.format(fn.__name__, execution_time))
        return to_execute
    
    return inner

def gen_test_case(n):
    array = [random.randrange(100) for i in range(n)]
    array.sort()
    index = random.randrange(0, len(array))
    target = array[index]
    if random.random() < 0.25:
        target = int(random.random()*100)
    
    try:
        array.index(target)
    except(ValueError):
        found = False
    else:
        found = True
    
    return array, target, found

@timer
def binary_search(x:int, array:list) -> bool:
    if len(array) == 0:
        return False
    else:
        return binary_search_rec(x, array, ini=0, end=len(array)-1)

def binary_search_rec(x, array, ini, end) -> bool:
    if ini > end:
        return False
    
    mid = (ini+end)//2
    
    if array[mid] == x:
        return True
    elif array[mid] > x:
        return binary_search_rec(x, array, ini, mid-1)
    elif array[mid] < x:
        return binary_search_rec(x, array, mid+1, end)
    
if __name__ == "__main__":
    
    for i in range(10):
        array, target, found = gen_test_case(35)
        
        bs = binary_search(target, array)
        
        print(array, target, found, bs)
        assert(bs == found)
    
            