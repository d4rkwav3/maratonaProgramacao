class RNA():
    samples: str = []
    test_results = []
    m = "AUG"
    f = ("UUC", "UUU")
    i = ("AUA", "AUC", "AUU")

    def __init__(self, samples: list):
        self.samples = samples
        self.mfi_match()

    def compare_sequence(self, subsample: str):
        m = f = i = ""

        for char in subsample[:3]:
            m += char
        for char in subsample[3:6]:
            f += char
        for char in subsample[6:9]:
            i += char

        if m == self.m and (f == self.f[0] or f == self.f[1]) and (i == self.i[0] or i == self.i[1] or i == self.i[2]):
            return True
        else:
            return False

    def mfi_match(self):
        for ribbons in self.samples:
            if ribbons.count(self.m) > 0:
                match_index = ribbons.find(self.m)
                if self.compare_sequence(ribbons[match_index:match_index + 9]):
                    self.test_results.append('S')
            else:
                self.test_results.append('N')
                   
    def show_results(self):
        for r in range(len(self.test_results)):
            
            if r < (len(self.test_results) -1):
                print(self.test_results[r])

            elif r == (len(self.test_results) - 1):
                print(self.test_results[r], end='')

ribbons: str = []
number_of_inputs = int(input())

for t in range(number_of_inputs):
    ribbons.append(input())

test = RNA(ribbons)
test.show_results()