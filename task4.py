# task4.py

def read_names_from_file(filename):
    with open(filename, 'r') as file:
        names = file.readlines()
    return [name.strip() for name in names]

if __name__ == '__main__':
    names = read_names_from_file('/home/pi/ee347/lab-4-advanced-python-group-18/task3.txt')
    for name in names:
        print(name)
