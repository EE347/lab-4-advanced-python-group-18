import csv


def add_names_to_csv(filename):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        while True:
            name = input('Enter a name (or type "quit" to stop): ')
            if name.lower() == 'quit':
                break
            writer.writerow([name])

def read_names_from_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        names = [row[0] for row in reader]
    return names

if __name__ == '__main__':
    filename = 'task5.csv'
    add_names_to_csv(filename)
    names = read_names_from_csv(filename)
    for name in names:
        print(name)
