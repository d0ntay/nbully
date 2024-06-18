import csv

def escalate(port):
    with open('port_list.csv', newline='')as csvfile:
        content = int(csv.DictReader(csvfile))
        for line in content:
            if line == port:
                print('boom')

