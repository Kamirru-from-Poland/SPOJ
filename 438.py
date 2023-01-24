TRUE = "TAK"
FALSE = "NIE"

def prime_number_test(x):
    if x < 2: return FALSE
    for i in range(2,x):
        if x%i == 0: return FALSE
    return TRUE

if __name__ == '__main__':
    i = int(input())
    for i in range(i):
        x = int(input())
        print(prime_number_test(x))