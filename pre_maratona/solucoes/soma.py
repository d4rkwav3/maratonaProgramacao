def soma (string: str):
    string.strip()
    num = string.split()
    a = int(num[0])
    b = int(num[1])
    return a + b

numbers = []
results = []

calc = (int(input()))

for c in range(calc):
    numbers.append(input())

for n in range(len(numbers)):
    results.append(soma(numbers[n]))
'''
for t in range(len(numbers)):
    print(numbers[t])
'''
for p in range(len(results)):
    #print(results[p])
    if p < (len(results) -1):
        print(results[p])
    elif p == (len(results) - 1):
        print(results[p], end='')