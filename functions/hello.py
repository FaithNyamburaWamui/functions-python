def hello(name):
    print(f"Hello {name}")

def year_of_birth(name,age):
    year = 2024-age
    print(f"Hello {name}, you were born in {year}")

def my_country(country="Uganda"):
    print(f"Hello AkiraChix from {country}")



def numbers(x):
    for i in range(1,12):
        if i % 2==0:
            print(i)
            continue


def greet(*names):
    for i in names:
        print(f"Hello {names}")