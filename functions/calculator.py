def add(x,y):
    result = x+y
    return result

def divide(s,r):
    result = s/r
    return result

def subtract(b,g):
    result = b-g
    return result

def multiply(k,h):
    result = k*h
    return result

def remainder(r,y):
    result = r%y
    return result

def power_of(v,h):
    result = v**h
    return result

def get_sum(*numbers):
    total=0
    for s in numbers:
        total +=s
    return total

def multiply_many(*values):
    total =1
    for i in values:
        total*=i
    print(total)

def create_sentence(**words):
    print(words)
    sentence =''
    for i in words.values():
        sentence +=words
        sentence +=" "
    return sentence 

def sum_and_greet(*args,**kwargs):
    total=0
    for x in args:
        total+=0
    f = kwargs["firstname"]
    l =kwargs["lastname"]
    greeting =f"Hello {f} {l} total of your numbers is {total}"
    return greeting


def is_prime(num):
    if num <= 1:
        return "is not prime number"
    elif num == 2:
        return "it is a prime number"
    elif num % 2 == 0:
        return "is not prime number"
    for i in range(3, num):
        if num % i == 0:
            return "is not a prime number"
    return "it is a prime number"


