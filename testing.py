f = open('PrimeNumber.txt', 'r')
count = 0

for i in range(100):
    x = int(f.readline())
    print(count)
    for i in range(2, int(x**(0.5))):
        if x % i == 0:
            print(x, "False")
            break
    else:
        print(x, "True")
        count += 1

print(count)