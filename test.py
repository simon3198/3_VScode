import random

def add_randint(a):
    for idx in range(len(a)):
        rand_int = random.randint(0,10)
        a[idx] += rand_int
    pass

if __name__ == "__main__":
    a = [i for i in range(0,5)]
    print(a)
    
    add_randint(a)
    print(a)
    print("finish")