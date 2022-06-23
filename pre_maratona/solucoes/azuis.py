class RNA():
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

    def __init__(self, samples: list):
        self.samples = samples
        self.search_match()

    def search_match(self):
        for each in self.samples:
            match_found = False
            mfi = each.find(self.m)
            
            if mfi >= 0:
                subsample = each[mfi:mfi + 9]
                if len(subsample) == 9:
                    for match in range(len(self.possible_matchs)):
                        if subsample == self.possible_matchs[match]:
                            match_found = True
                            break
                        else:
                            continue

            if match_found:
                self.results.append('S')
            else:
                self.results.append('N')

    def show_results(self):
        for test in range(len(self.results)):
            print(self.results[test])
        '''if test < (len(self.results) -1):
            print(self.results[test])
        elif test == (len(self.results) - 1):
            print(self.results[test], end='')'''

test_samples = []
runs = int(input())

for tests in range(runs):
    sample = input()
    test_samples.append(sample.strip())

blue_eyes = RNA(test_samples)
blue_eyes.show_results()