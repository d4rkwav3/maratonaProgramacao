m = "AUG"
f = ("UUC", "UUU")
i = ("AUA", "AUC", "AUU")

match1 = m + f[0] + i[0]
match2 = m + f[0] + i[1]
match3 = m + f[0] + i[2]
match4 = m + f[1] + i[0]
match5 = m + f[1] + i[1]
match6 = m + f[1] + i[2]

possible_matchs = [match1, match2, match3, match4, match5, match6]
samples = []
results = []
runs = int(input())

for tests in range(runs):
    sample = input()
    samples.append(sample.strip())

for i in samples:
    match_found = False
    mfi = i.find(m)
    
    if mfi >= 0:
        s = i[mfi:mfi + 9]
        if len(s) == 9:
            for b in range(len(possible_matchs)):
                if s == possible_matchs[b]:
                    match_found = True
                    break
                else:
                    continue

    if match_found:
        results.append('S')
    else:
        results.append('N')

for r in range(len(results)):
    print(results[r])
    '''if r < (len(results) -1):
        print(results[r])
    elif r == (len(results) - 1):
        print(results[r], end='')'''