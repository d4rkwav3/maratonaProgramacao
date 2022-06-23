class DNA:
    given_ribbon = ""
    other_ribbon = ""
    m = ("AUG")
    f = ("UUC", "UUU")
    i = ("AUA", "AUC", "AUU")

    def __init__(self, sample: str):
        self.given_ribbon = sample
        #self.make_other_half()

    def compare (self, codon: str):
        ribbon1 = self.given_ribbon.count(codon)
        #ribbon2 = self.other_ribbon.count(codon)

        if ribbon1 > 0: #or ribbon2 > 0:
            return True
        else:
            return False

    def make_other_half (self):
        temp_list = []
        for each_nitro_base in self.given_ribbon:
            if each_nitro_base == 'A':
                temp_list.append('U')
            elif each_nitro_base == 'U':
                temp_list.append('A')
            elif each_nitro_base == 'C':
                temp_list.append('G')
            elif each_nitro_base == 'G':
                temp_list.append('C')
        self.other_ribbon = ''.join(temp_list)

    def receive_sample (self, sample: str):
        self.given_ribbon = sample

    def find_mfi (self):
        match_found = False
        m = self.compare(self.m)
        f_1 = self.compare(self.f[0])
        f_2 = self.compare(self.f[1])
        i_1 = self.compare(self.i[0])
        i_2 = self.compare(self.i[1])
        i_3 = self.compare(self.i[2])
        if m and (f_1 or f_2) and (i_1 or i_2 or i_3):
            match_found = True
        if match_found:
            return 'S'
        else:
            return 'N'


test_samples = []
test_results = []
number_of_tests = int(input())

for n in range(number_of_tests):
    test_samples.append(input())

for n in range(len(test_samples)):
    test = DNA(test_samples[n])
    test_results.append(test.find_mfi())

for n in range(len(test_results)):
    #print(test_results[n])
    if n < (len(test_results) -1):
        print(test_results[n])
    elif n == (len(test_results) - 1):
        print(test_results[n], end='')
