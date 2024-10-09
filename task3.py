# task3.py

def add_name_to_file(filename, name):
    with open(filename, 'a') as file:
        file.write(name + '\n')

if __name__ == '__main__':
    for _ in range(3):
        name = input('Enter your name: ')
        add_name_to_file('/home/pi/ee347/lab-4-advanced-python-group-18/task3.txt', name)
    print("3 names have been added to the file.")
