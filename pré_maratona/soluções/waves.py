class Tower_Network():
    tower_network = []
    network_report = []

    def __init__(self, test_cases: list):
        self.tower_network = test_cases

    # def convert(self):
    #     for test in range(len(self.tower_network)):
    #         for 

    def check_connections(self):
        connection = []
        bad_tower = []

        for test in range(len(self.tower_network)): #itera pelos testes
            for tower in range(len(self.tower_network[test])): #itera pelas torres do teste
                for status in self.tower_network[test][tower]: #verifica o status de conexão da torre em questão com as demais
                    if status.startswith("1"):
                        connection.append(1)
                        break
                    # else:
                    #     for conn in range(len(status)):
                            

towers_report = []
current_report = []
num_of_tests = int(input())

for tests in range((num_of_tests) + 1):
    if (len(current_report) > 0) and (len(towers_report) < num_of_tests):
        towers_report.append(current_report)
        current_report = []

    if (len(current_report) == 0) and (len(towers_report) < num_of_tests):
        towers_tested = int(input())

        for tower in range(towers_tested):
            report = input()
            current_report.append(report.strip())

check_up = Tower_Network(towers_report)
check_up.check_connections()